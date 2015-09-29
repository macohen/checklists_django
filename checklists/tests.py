from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Checklist, ChecklistTodo
from checklists_django.urls import *

# Create your tests here.

class TestChecklist(TestCase):

    def setUp(self):
        self.checklist = Checklist.objects.create(title='Checklist Master')

    def test_it_should_have_a_title(self):
        expected_title='Checklist Master'
        self.assertEquals(expected_title, self.checklist.title)

    def test_it_should_print_title(self):
        self.assertEquals('Checklist Master', str(self.checklist))

    def test_it_should_have_a_dateCreated(self):
        self.assertIsNotNone(self.checklist.dateCreated)

class TestChecklistTodo(TestCase):
     def test_it_should_have_a_description(self):
         expected_description = 'Description'
         self.assertEquals(expected_description, self.todo.todoDescription)

     def setUp(self):
         self.checklist = Checklist.objects.create(title='Checklist Master')
         self.todo = ChecklistTodo.objects.create(todoDescription='Description', checklistId=self.checklist)

     def test_it_should_print_description(self):
         self.assertEquals('Description', str(self.todo))


class TestApiRouter(APITestCase):
    def test_get_all_checklists(self):
        """
            Ensure we can get checklists via API when there are no data in the database
        """
        response = self.client.get('/checklists/')
        self.assertEqual(response.data, [])

    def test_serialize_checklist(self):
        serializer = ChecklistSerializer(Checklist(checklistId=1, title='Test'))
        self.assertEquals({'checklistId' : 1, 'title' : 'Test'}, serializer.data)

    def test_create_one_checklist(self):
        data = {'title' : 'One Checklist'}
        response = self.client.post('/checklists/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Checklist.objects.count(), 1)
        self.assertEqual(Checklist.objects.get().title, 'One Checklist')



