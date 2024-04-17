from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .models import BugReport, FeatureRequest
from django import forms
from django.views import View
from django.views.generic import ListView, DetailView


def index(request):
    another_page_url = reverse('quality_control:bug_list')
    another_page_url_2 = reverse('quality_control:feature_list')
    html = f"<h1>Контроль качества</h1><p><a href='{another_page_url}'>Списиок всех багов</a></p><p><a href='{another_page_url_2}'>Запросы на улучшение</a></p>"
    return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список отчетов об ошибке</h1><ul>'
    for bug in bugs:
        bugs_html += f"<li>{bug.name}</li>"
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    featurerequests_html = '<h1>Список запросов на улучшение</h1><ul>'
    for featurerequest in bugreports:
        featurerequests_html += f"<li>{featurerequest.name}</li>"
    featurerequests_html += "</ul>"
    return HttpResponse(featurerequests_html)

def bug_detail(request, bug_id):
    bugreport = get_object_or_404(BugReport, id=bug_id)
    bugs = bugreport.tasks.all()
    response_html = f'<h1>Детали бага {{ bugreport.id }}</h1>'
    return HttpResponse(response_html)

def feature_id_detail(request, bug_id, feature_id):
    bugreport = get_object_or_404(BugReport, id=bug_id)
    featurerequest = get_object_or_404(FeatureRequest, id=feature_id, bug_id=bug_id)
    response_html = f'<h1>Детали улучшения {{ featurerequest.id }}</h1>'
    return HttpResponse(response_html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_url = reverse('quality_control:bug_list')
        features_url = reverse('quality_control:feature_list')
        html = f"<h1>Контроль качества</h1><p><a href='{bugs_url}'>Списиок всех багов</a></p><p><a href='{features_url}'>Запросы на улучшение</a></p>"
        return HttpResponse(html)

class BugReportsListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список отчетов об ошибке</h1><ul>'
        # for bugreport in bugreports:
        #     bugreports_html += f'<li><a href="{bugreport.id}/">{bugreport.name}</a></li>'
        # bugreports_html += '</ul>'
        return HttpResponse(bugs_html)

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bugreport = self.object
        featurerequests = bugreport.featurerequests.all()
        response_html = f'<h1>Детали бага {{ bugreport.id }}</h1>'
        return HttpResponse(response_html)

class FeatureRequestsListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        featurerequestss_html = '<h1>Список запросов на улучшение</h1><ul>'
        for featurerequest in features:
            featurerequestss_html += f'<li><a href="{featurerequest.id}/">{featurerequest.name}</a></li>'
        featurerequestss_html += '</ul>'
        return HttpResponse(featurerequestss_html)

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        featurerequest = self.object
        featurerequests = bugreport.featurerequests.all()
        response_html = f'<h1>Детали улучшения {{ featurerequest.id }}</h1>'
        return HttpResponse(response_html)