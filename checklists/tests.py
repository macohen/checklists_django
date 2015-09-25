from django.test import TestCase
from .models import Checklist, TodoItem

# Create your tests here.

class TestChecklist(TestCase):

    def setUp(self):
        self.checklist = Checklist.objects.create(title='Checklist Master')

    def test_it_should_have_a_title(self):
        expected_title='Checklist Master'
        self.assertEquals(expected_title, self.checklist.title)

    def test_add_todo_item(self):
        todo_item = TodoItem.objects.create(description='Description')
        self.checklist.todo_item = todo_item
        checklists = Checklist.objects.all()
        self.assertEquals(1, len(checklists))
        self.assertIsNotNone(self.checklist.todo_item)
        self.assertEquals('Description', self.checklist.todo_item.description)

class TestTodoItem(TestCase):
    def test_it_should_have_a_description(self):
        expected_description = 'Description'
        todo = TodoItem.objects.create(description='Description')
        self.assertEquals(expected_description, todo.description)


