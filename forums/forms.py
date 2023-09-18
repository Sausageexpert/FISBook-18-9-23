from .models import Events
from django import forms

class ScheduleForm(forms.ModelForm):
    class Meta():
        model = Events
        fields = ['forum', 'title', 'about', 'date', 'is_public', 'users_added']