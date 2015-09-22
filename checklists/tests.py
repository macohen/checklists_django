from django.test import TestCase
from .models import Checklist

# Create your tests here.

class TestChecklist(TestCase):
    def test_it_should_have_a_title(self):
        expected_title='Checklist Master'
        checklist = Checklist.objects.create(title='Checklist Master')
        self.assertEquals(expected_title, checklist.title)

    #def test_it_should_have_one_todo_item(self):
    #    checklist = Checklist.objects.create(title='Checklist Master')
    #    self.assertGreaterEqual(1, len(checklist.todo_items))


