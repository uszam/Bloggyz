from django.test import TestCase
from models import Post

class PostTests(TestCase):
    def test_str(self):
        my_title = Post(title='Ini adalah basic title untuk basic test case')
        self.assertEquals(str(my_title), 'Ini adalah basic title untuk basic test case')
