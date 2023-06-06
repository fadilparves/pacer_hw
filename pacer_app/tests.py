from django.test import TestCase, Client
from pacer_app.models import Score
import json
from django.urls import reverse

# initialize the APIClient app
client = Client()

# Create your tests here.

class ScoreTestCase(TestCase):
    
    def test_score(self):
        response = client.get(reverse('score', kwargs={'user_id': 1}), {'input': 0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['user_id'], 1)
        self.assertEqual(response.json()['score'] >= 0, True)
        self.assertEqual(response.json()['score'] <= 100, True)
        self.assertEqual(response.json()['date'] != '', True)