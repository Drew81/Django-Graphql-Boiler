import graphene 
from graphene_django.types import DjangoObjectType
from .models import  Student, Detail, Note



class StudentType(DjangoObjectType):
	class Meta:
		model = Student

class DetailType(DjangoObjectType):
	class Meta:
		model = Detail

class NoteType(DjangoObjectType):
	class Meta:
		model = Note

class Query(object):
	all_students = graphene.List(StudentType)
	all_details = graphene.List(DetailType)
	all_notes = graphene.List(NoteType)

	def resolve_all_students(self, info, **kwargs):
		return Student.objects.all()

	def resolve_all_details(self, info, **kwargs):
		return Detail.objects.select_related('student').all()

	def resolve_all_notes(self, info, **kwargs):
		return Note.objects.select_related('student').all()