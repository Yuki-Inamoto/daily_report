from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.test import Client

from .models import Report

class _test(TestCase):

    def setUp(self):
        u = User.objects.create_user('Mr.X','','XXX')
        u.save()
        r = Report(pub_date=timezone.now(),edit_date=timezone.now(),\
        title="TEST",content="test content", user_id = u)
        r.save()
        c = Client()
   
    def test_login_check(self):
        c = Client()
        self.assertEqual(c.login(username='Mr.X', password='XXX'), True)

    def test_dislogin_check(self):
        c = Client()
        self.assertEqual(c.login(username='Ms.Y', password='XXX'), False)

    def test_index(self):
        response = self.client.get('/daily_report/')
        self.failUnlessEqual(response.status_code, 200)
        
    def test_user_page(self):
        c = Client()
        c.login(username='Mr.X', password='XXX')
        response = self.client.get('/daily_report/user/')
        self.failUnlessEqual(response.status_code, 200)

    def test_register_out(self):
        c = Client()
        c.login(username='Mr.X', password='XXX')
        response = self.client.get('/daily_report/register/')
        self.failUnlessEqual(response.status_code, 404)
        
    def test_login_out(self):
        c = Client()
        c.login(username='Mr.X', password='XXX')
        response = self.client.get('/daily_report/login/')
        self.failUnlessEqual(response.status_code, 404)

    def test_logout_page(self):
        response = self.client.get('/daily_report/logout/')
        self.failUnlessEqual(response.status_code, 200)

    def test_read(self):
        c = Client()
        c.login(username='Mr.X', password='XXX')
        response = self.client.get('/daily_report/read-report/')
        self.failUnlessEqual(response.status_code, 200)

class SimpleTest(TestCase):

    def test_report_is_empty(self):
        reports = Report.objects.all()
        self.assertEqual(reports.count(),0)

    def test_user_ist_empty(self):
        users = User.objects.all()
        self.assertEqual(users.count(),0)

    def test_index(self):
        response = self.client.get('/daily_report/')
        self.failUnlessEqual(response.status_code, 200)

    def test_root(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 404)

    def test_login_page(self):
        response = self.client.get('/daily_report/login/')
        self.failUnlessEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get('/daily_report/logout/')
        self.failUnlessEqual(response.status_code, 404)

    def test_read(self):
        response = self.client.get('/daily_report/read-report/')
        self.failUnlessEqual(response.status_code, 404)

# Create your tests here.
