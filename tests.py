from django.test import TestCase
from django.contrib.auth.models import User
class AppTests(TestCase):
 def test_home(self):
  response=self.client.get('/')
  self.assertEqual(response.status_code,200)
 def test_car_models(self):
  result=self.client.get('/djangoapp/get_cars').json()
  self.assertEqual(len(result['CarModels']),15)
 def test_register_login_logout(self):
  import json
  def post(path,data):return self.client.post(path,data=json.dumps(data),content_type='application/json')
  self.assertEqual(post('/djangoapp/register',{'userName':'learner','password':'GoodPassword123'}).status_code,201)
  self.assertEqual(post('/djangoapp/login',{'userName':'learner','password':'GoodPassword123'}).json()['status'],'Authenticated')
  self.assertEqual(self.client.get('/djangoapp/logout').json()['userName'],'')
