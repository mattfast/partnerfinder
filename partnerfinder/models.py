from django.db import models

class Instructor(models.Model):
	username = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

class Student(models.Model):
	username = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

class Course(models.Model):
	name = models.CharField(max_length=100)

class TimeSlot(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

class Availability(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

class Enrollment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Instruction(models.Model):
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class PreviousCourse(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

class Assignment(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

class Posting(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
	created = models.DateTimeField()
	wants_automatic = models.BooleanField()
	note = models.TextField()





