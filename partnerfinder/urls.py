from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.courseinfo, name='courseinfo'),
    path('assignment/<int:assignment_id>', views.assignmentinfo, name='assignmentinfo'),
    path('posting/<int:posting_id>', views.postinginfo, name='postinginfo'),

    path('createcourse/', views.createcourse, name='createcourse'),
    path('courses/<int:course_id>/createassignment/', views.createassignment, name='createassignment'),
    path('assignment/<int:assignment_id>/createposting/', views.createposting, name='createposting'),

]