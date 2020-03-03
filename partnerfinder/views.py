from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import *

import datetime


def index(request):
    return render(request, 'index.html')

def courses(request):
	course_list = Course.objects.order_by('name')
	context = {'course_list': course_list}
	return render(request, 'courses.html', context)

def courseinfo(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	assignment_list = Assignment.objects.filter(course=course).order_by('name')
	context = {'assignment_list': assignment_list, 'course': course}
	return render(request, 'courseinfo.html', context)

def assignmentinfo(request, assignment_id):
	assignment = get_object_or_404(Assignment, pk=assignment_id)
	posting_list = get_list_or_404(Posting, assignment=assignment)
	context = {'posting_list': posting_list, 'assignment_name': assignment.name}
	return render(request, 'assignmentinfo.html', context)

def postinginfo(request, posting_id):
	posting = get_object_or_404(Posting, pk=posting_id)
	context = {'posting': posting}
	return render(request, 'postinginfo.html', context)

def courseform(request):
	return render(request, 'courseform.html')

def assignmentform(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	context = {'course': course}
	return render(request, 'assignmentform.html', context)

def postingform(request, assignment_id):
	assignment = get_object_or_404(Assignment, pk=assignment_id)
	context = {'assignment': assignment}
	return render(request, 'postingform.html', context)

def createcourse(request):
	try:
		name = request.POST['name']
		course = Course.objects.create(name = name)
	except (KeyError):
		context = {'error_message': "You did not enter a course name."}
		return render(request, 'courseform.html', context)

	return HttpResponseRedirect(reverse('courseinfo', args = (course.id,)))

def createassignment(request, course_id):
	try:
		name = request.POST['name']
		course = get_object_or_404(Course, pk=course_id)
		assignment = Assignment.objects.create(name = name, course = course)
	except (KeyError):
		context = {'error_message': "You did not enter an assignment name."}
		return render(request, 'assignmentform.html', context)

	return HttpResponseRedirect(reverse('assignmentinfo', args = (assignment.id,)))

def createposting(request, assignment_id):
	try:
		note = request.POST['note']
		time = datetime.datetime.now()
		assignment = get_object_or_404(Assignment, pk=assignment_id)
		posting = Assignment.objects.create(note = note, created = time, assignment = assignment)
	except (KeyError):
		context = {'error_message': "You did not enter a note."}
		return render(request, 'postingform.html', context)

	return HttpResponseRedirect(reverse('postinginfo', args = (posting.id,)))



