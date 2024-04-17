from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index),
    # path('bugs/', views.bugs, name='bugs'),
    # path('features/', views.features, name='features'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id_detail>/', views.feature_id_detail, name='feature_id_detail'),

    # path('', views.index),
    path('', views.IndexView.as_view(), name='index'),
    # path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/', views.BugReportsListView.as_view(), name='bug_list'),
    # path('features/', views.feature_list, name='feature_list'),
    path('features/', views.FeatureRequestsListView.as_view(), name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    # path('features/<int:feature_id_detail>/', views.feature_id_detail, name='feature_id_detail'),
    path('features/<int:feature_id_detail>/', views.FeatureRequestDetailView.as_view(), name='feature_id_detail'),

]