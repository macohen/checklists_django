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

    # def test_add_todo_item(self):
    #     todo_item = TodoItem.objects.create(description='Description')
    #     self.checklist.todo_item = todo_item
    #     checklists = Checklist.objects.all()
    #     self.assertEquals(1, len(checklists))
    #     self.assertIsNotNone(self.checklist.todo_item)
    #     self.assertEquals('Description', self.checklist.todo_item.description)

    def test_it_should_print_title(self):
        self.assertEquals('Checklist Master', str(self.checklist))

class TestTodoItem(TestCase):
    def test_it_should_have_a_description(self):
        expected_description = 'Description'
        self.assertEquals(expected_description, self.todo.description)

    def setUp(self):
        self.todo = ChecklistTodo.objects.create(description='Description')

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

#    def test_get_one_checklist(self):
#        data = {'title' : 'One Checklist'}
#        response = self.client.post('/checklists/',data, format='json')

#        response = self.client.get('/checklists/')
#        self.assertEquals(data.get('title'), response.data.get('title'))

    # def test_create_two_checklists(self):
    #     checklist_one = Checklist(title='Checklist One')
    #     checklist_two = Checklist(title='Checklist Two')
    #     #cl_serializers = [ ChecklistSerializer (checklist_one), ChecklistSerializer(checklist_two)]
    #     cl_serializer = ChecklistSerializer([checklist_one, checklist_two], many=True)
    #
    #     response = self.client.post('/checklists/',  cl_serializer.data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Checklist.objects.count(), 2)
    #     checklists = Checklist.objects.get()
    #     self.assertEqual(Checklist.objects.get()[0].title, 'Checklist One')
    #     self.assertEqual(Checklist.objects.get()[1].title, 'Checklist Two')




