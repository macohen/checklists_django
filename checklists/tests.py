import django
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Checklist, ChecklistTodo
from .views import ChecklistSerializer

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
    def setUp(self):
        self.checklist = Checklist.objects.create(title='Checklist Master')
        self.todo = ChecklistTodo.objects.create(todoDescription='Description', checklistId=self.checklist)

    def test_it_should_have_a_description(self):
        expected_description = 'Description'
        self.assertEquals(expected_description, self.todo.todoDescription)

    def test_it_should_print_description(self):
        self.assertEquals('Description', str(self.todo))

    def test_get_full_checklists(self):
        todos = self.checklist.checklisttodo_set.all()
        self.assertEqual(1, todos.count())
        self.assertEquals('Description' , todos[0].todoDescription)


class TestApiRouterWithNoData(APITestCase):
    def test_get_all_checklists_when_empty_db(self):
        """
            Ensure we can get checklists via API when there are no data in the database
        """
        response = self.client.get('/checklists/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

class TestApiRouter(APITestCase):
    def test_serialize_checklist(self):
        now = django.utils.timezone.now()
        serializer = ChecklistSerializer(Checklist(checklistId=1, title='Test', dateCreated = now))
        self.assertEquals({'checklistId' : 1, 'title' : 'Test' }, serializer.data)

    def test_create_one_checklist_no_todos(self):
        data = {'title': 'One Checklist'}
        self.response = self.client.post('/checklists/', data, format='json')

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Checklist.objects.count(), 1)
        self.assertEqual(Checklist.objects.get().title, 'One Checklist')
        self.assertIsNotNone(Checklist.objects.get().dateCreated)

    # def test_create_one_checklist_one_todo(self):
    #     data = {'title' : 'One Checklist', 'todos' : ['Todo One']}
    #     self.response = self.client.post('/checklists/', data, format='json')
    #     self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Checklist.objects.count(), 1)
    #     self.assertEqual(Checklist.objects.get().title, 'One Checklist')
    #     self.assertIsNotNone(Checklist.objects.get().dateCreated)
    #     self.assertIsNotNone(1, Checklist.objects.get().)







