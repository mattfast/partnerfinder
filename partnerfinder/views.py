from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404

from .models import *


def index(request):
    return render(request, 'index.html')

def classes(request):
	return render(request, 'classes.html')

def classinfo(request, class_id):
	return render(request, 'classinfo.html')

def assignmentinfo(request, assignment_id):
	return render(request, 'assignmentinfo.html')

def createclass(request):
	return render(request, 'classinfo.html')

def createassignment(request, class_id):
	return render(request, 'assignmentinfo.html')

def createposting(request, assignment_id):
	return render(request, 'postinginfo.html')