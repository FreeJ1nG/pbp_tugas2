from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class ShowHtmlTests(TestCase):
  def test_request(self):
    response = self.client.get(reverse('mywatchlist:show_html'))
    self.assertEqual(response.status_code, 200)
    
class ShowXmlTests(TestCase):
  def test_request(self):
    response = self.client.get(reverse('mywatchlist:show_xml'))
    self.assertEqual(response.status_code, 200)
    
class ShowJsonTests(TestCase):
  def test_request(self):
    response = self.client.get(reverse('mywatchlist:show_json'))
    self.assertEqual(response.status_code, 200)
