from django import forms
from .models import BugReport, FeatureRequest

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']