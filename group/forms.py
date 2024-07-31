from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    goals_hours = forms.IntegerField(label='그룹 목표 시간 (시간)', max_value=23, required=True, min_value=0)
    goals_minutes = forms.IntegerField(label='그룹 목표 시간 (분)', max_value=59, required=True, min_value=0)
    
    class Meta:
        model = Group
        fields = ['title', 'information', 'password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['goals_hours'].initial = self.instance.goals // 60
            self.fields['goals_minutes'].initial = self.instance.goals % 60

    def save(self, commit=True):
        self.instance.goals = self.cleaned_data['goals_hours'] * 60 + self.cleaned_data['goals_minutes']
        return super().save(commit)