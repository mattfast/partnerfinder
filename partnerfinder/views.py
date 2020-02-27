from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404

from .models import *


def index(request):
    return render(request, 'index.html')

def courses(request):
	course_list = Course.objects.order_by('name')
	context = {'course_list': course_list}
	return render(request, 'courses.html', context)

def courseinfo(request, course_id):
	return render(request, 'courseinfo.html')

def assignmentinfo(request, assignment_id):
	return render(request, 'assignmentinfo.html')

def postinginfo(request, posting_id):
	return render(request, 'postinginfo.html')

def createcourse(request):
	return render(request, 'courseinfo.html')

def createassignment(request, course_id):
	return render(request, 'assignmentinfo.html')

def createposting(request, assignment_id):
	return render(request, 'postinginfo.html')