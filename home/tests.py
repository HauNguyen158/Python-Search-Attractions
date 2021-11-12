from django.http import response
from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    # nếu trang không tồn tại trả về 404
    def test_home_page(self):
        response = self.client.get('')