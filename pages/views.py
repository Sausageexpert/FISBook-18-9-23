from django.shortcuts import render, redirect
from django.urls import reverse 
from django.utils import timezone
from forums.models import Forum,Events
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import get_user_model
from users.forms import CustomUserChangeForm
from django.http import HttpResponse, JsonResponse
# Create your views here.
CustomUser = get_user_model()

def home(request):
    if request.user.is_authenticated:
        forums = request.user.forums.all()
        users_events = request.user.events_added.all().order_by('date').filter(Q(date__gte=timezone.now()))
        events = Events.objects.filter(forum__in=forums).order_by('date').filter(Q(date__gte=timezone.now()))
        context={'forums':forums,'users_events':users_events,'events':events,}
        return render(request,'home.html',context)
    else:
        return redirect(reverse('users:login'))
    
    
def explore(request):
    forums = Forum.objects.filter(is_public=True)
    events = Events.objects.filter(is_public=True).order_by('date').filter(Q(date__gte=timezone.now()))
    context = {'forums':forums,'events':events}
    return render(request,'explore.html',context)
    
def get(request, forum):
    forums = Forum.objects.filter(name__icontains=forum)
    forumsData=[]
    for forum in forums:
        forumsData.append({'name':forum.name, 'id':forum.id})
    return JsonResponse({'forums': forumsData})

def user(request,reg_no):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        user = CustomUser.objects.get(reg_no = reg_no)
        newPass = request.POST.get('newPass')
        user.set_password(newPass)
        user.save()
        return HttpResponse('success')
    else:    
        form = CustomUserChangeForm(instance = request.user)
        user = CustomUser.objects.get(reg_no=reg_no)
        context = {'reg_no':reg_no,'user':user,'form':form,}
        return render(request,'user.html',context)
    