from django.test import TestCase
from .models import Student
from django.urls import reverse

class StudentTestCase(TestCase):
    def test_student_creation(self):
        """Test équivalent à shouldSaveStudent de Spring Boot"""
        student = Student.objects.create(name="Charlie", address="Algeria")
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(student.name, "Charlie")
    
    def test_student_list(self):
        """Test équivalent à shouldFindAllStudents de Spring Boot"""
        Student.objects.create(name="Charlie", address="Algeria")
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['students']), 1)
        self.assertEqual(response.json()['students'][0]['name'], "Charlie")
    
    def test_hello_endpoint(self):
        """Test de l'endpoint hello"""
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Hello, CI/CD with Django!")

class DatabaseTestCase(TestCase):
    def test_database_isolation(self):
        """Test que la base de données est bien isolée en mémoire pour les tests"""
        # Ce test devrait avoir une base vide même si d'autres tests créent des données
        self.assertEqual(Student.objects.count(), 0)