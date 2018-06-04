from django.shortcuts import render, redirect
from .models import Student 
from .forms import StudentForm


#### Students Views

def list_students(request):
	students = Student.objects.all()
	return render(request, 'student.html', {'students': students})


def create_student(request):
	form = StudentForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('list_students')

	return render(request, 'student-form.html', {'form': form})



def update_student(request, id):
	student = Student.objects.get(id=id)
	form = StudentForm(request.POST or None, instance=student)

	if form.is_valid():
		form.save()
		return redirect('list_students')

	return render(request, 'student-form.html', {'form': form, 'student': student})


def delete_student(request, id):
	student = Student.objects.get(id=id)

	if request.method == 'POST':
		service.delete()
		return redirect('list_students')

	return render(request, 'student-delete-form.html', {'student': student})


### Details Views

def list_details(request):
	details = detail.objects.all()
	return render(request, 'detail.html', {'details': details})


def create_details(request):
	form = detailForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('list_detailss')

	return render(request, 'detail-form.html', {'form': form})



def update_detail(request, id):
	detail = Detail.objects.get(id=id)
	form = detailForm(request.POST or None, instance=detail)

	if form.is_valid():
		form.save()
		return redirect('list_details')

	return render(request, 'detail-form.html', {'form': form, 'detail': detail})


def delete_detail(request, id):
	detail = detail.objects.get(id=id)

	if request.method == 'POST':
		detail.delete()
		return redirect('list_details')

	return render(request, 'detail-delete-form.html', {'detail': detail})


# Notes views

def list_notes(request):
	notes = Note.objects.all()
	return render(request, 'note.html', {'notes': notes})

