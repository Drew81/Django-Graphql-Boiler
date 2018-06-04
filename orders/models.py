from django.db import models

TOD_CHOICES = (
    ("1", "Morning"),
    ("2", "afternoon"),
    ("3", "Evening")
)
# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	grade = models.IntegerField()

	def __str__(self):
		return self.name

 
class Detail(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)
	a_level = models.IntegerField()
	b_level = models.IntegerField()
	c_level = models.IntegerField()
	tantrum_level = models.IntegerField()
	date_time = models.DateTimeField(auto_now_add=True, blank=True)
	tod = models.CharField(max_length=9, choices=TOD_CHOICES, default="Morning")

	def __str__(self):
		return self.tod


class Note(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	triggers = models.CharField(max_length=100)

	def __str__(self):
		return self.triggers

