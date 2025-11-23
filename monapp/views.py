from django.http import JsonResponse
from django.views import View
from .models import Student

class HelloView(View):
    def get(self, request):
        return JsonResponse({"message": "Hello, CI/CD with Django!"})

class StudentView(View):
    def get(self, request):
        students = list(Student.objects.values())
        return JsonResponse({"students": students})
    
    def post(self, request):
        # Pour les tests - création d'un étudiant
        student = Student.objects.create(name="Charlie", address="Algeria")
        return JsonResponse({"id": student.id, "name": student.name, "address": student.address})