

# Create your tests here.

from django.test import TestCase
from .models import Enqry

class EnqryModelTestCase(TestCase):
    def setUp(self):
        # Create some test data
        Enqry.objects.create(p_name='Test User', p_email='test@example.com', p_phone='1234567890', p_when='2024-04-22', p_events='Test Event')

    def test_enquiries_query(self):
        # Test the query to retrieve enquiries
        enquiries = Enqry.objects.all()
        self.assertEqual(enquiries.count(), 1)
