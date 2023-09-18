from django.shortcuts import render, redirect
from .models import Forum,Events,Notices
from chat.models import Room
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse
from .forms import ScheduleForm
# Create your views here.

def forum(request,forum_id):

    if request.method == 'POST':
        if "chat" in request.POST:
            room = Forum.objects.get(id=forum_id)
            roomName = room.name
            user = request.user.first_name
            if Room.objects.filter(name=roomName).exists():
                return redirect('/chat/' + roomName + '/?user=' + user)
            else:
                newRoom = Room.objects.create(name=roomName)
                newRoom.save()
                return redirect('/chat/' + roomName + '/?user=' + user)
        else:
            form = ScheduleForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.save()
                event.users_added.set([request.user])
                currentForum = Forum.objects.get(id = forum_id)
                event.forum.set([currentForum])
                return redirect('/forums/'+forum_id)
            else:
                return HttpResponse(f'Form error: {form.errors}')
    else:
        forum = Forum.objects.get(id=forum_id)
        events = Events.objects.filter(forum__id = forum_id).order_by('date').filter(Q(date__gte=timezone.now()))
        notices = Notices.objects.filter(forum__id=forum_id)
        form = ScheduleForm()
        context = {'forum':forum,'events':events,'notices':notices,'form':form}
        return render(request,'forum.html',context)

def test(request):
    return render(request, 'test.html')

def event(request,event_id):
    if request.method=='POST':
            room = Events.objects.get(id=event_id)
            roomName = room.title
            user = request.user.first_name
            if Room.objects.filter(name=roomName).exists():
                return redirect('/chat/' + roomName + '/?user=' + user)
            else:
                newRoom = Room.objects.create(name=roomName)
                newRoom.save()
                return redirect('/chat/' + roomName + '/?user=' + user)
    else:    
        event = Events.objects.get(id=event_id)
        context = {'event':event,'forum':forum}
        return render(request,'event.html',context)

def member_list(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    user_forums = request.user.forums.all()
    if forum.is_public or forum in user_forums:
        members = forum.users.all()
        mods = forum.mods.all()
        context = {'members':members,'mods':mods}
        return render(request,'members.html',context)
    else:
        valid = False
        context = {'valid':valid}
        return render(request,'invalid.html',context)
        
''' if request.method == 'POST':
        if request.POST.get('chat')==True:
            room = Forum.objects.get(id=forum_id)
            roomName = room.name
            user = request.user.first_name
            if Room.objects.filter(name=roomName).exists():
                return redirect('/chat/' + roomName + '/?user=' + user)
            else:
                newRoom = Room.objects.create(name=roomName)
                newRoom.save()
                return redirect('/chat/' + roomName + '/?user=' + user)
        else:
            form = ScheduleForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('success')'''