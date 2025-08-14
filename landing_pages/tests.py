from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

from .models import LandingPageEntry

User= get_user_model()

class LandingPageEntryTestCase(TestCase):
    
    fixtures= ["entry-data.json", "user.json"]

    def setUp(self):
        self.inactive_count=3
        for i in range(0, self.inactive_count):
            LandingPageEntry.objects.create(
                name="Safaet",
                email="abcd@gmail.com",
                active=False
        )
    
    def test_inactive(self):
        # obj_list=LandingPageEntry.objects.all()
        # inactive_items= [x for x in obj_list if not x.active]
        # assert len(inactive_items) == 1
        
        qs= LandingPageEntry.objects.filter(active=False)
        self.assertTrue(qs.exists())
        self.assertEqual(qs.count(), self.inactive_count)

    
    def test_active(self):
        qs= LandingPageEntry.objects.filter(active=True)
        self.assertTrue(qs.exists())
        self.assertGreaterEqual(qs.count(), 5)
    

    def test_user_exist(self):
        qs=User.objects.all()
        self.assertTrue(qs.exists())