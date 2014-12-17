from django.test import TestCase
from .models import Entry

class EntryModelTest(TestCase):
    def test_string_rep(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)

    def test_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural),
                         "entries")

class ViewTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
