from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('classes/<int:class_id>/', views.classinfo, name='classinfo'),
    path('assignment/<int:assignment_id>', views.assignmentinfo, name='assignmentinfo'),
    path('posting/<int:posting_id>', views.postinginfo, name='postinginfo'),

    path('createclass/', views.createclass, name='createclass'),
    path('classes/<int:class_id>/createassignment/', views.createassignment, name='createassignment'),
    path('assignment/<int:assignment_id>/createposting/', views.createposting, name='createposting'),

]