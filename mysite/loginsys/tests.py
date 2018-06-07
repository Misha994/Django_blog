from django.test import TestCase
from .forms import *


class User_Form_Test(TestCase):

    def test_UserForm_valid(self):
        form = SignupForm(data={'username': 'testing',
                                'first_name': 'testusername',
                                'last_name': 'testlastname',
                                'email': 'test@gmail.con',
                                'password1': '1qwertyu',
                                'password2': '1qwertyu',
                                'phone_number': 12334})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = SignupForm(data={'username': 'testing',
                                'first_name': 'testusername',
                                'last_name': 'testlastname',
                                'email': 'test@gmail.con',
                                'password1': '1qwertyu',
                                'password2': '1qwertyu',
                                'phone_number': 12334})
        self.assertFalse(form.is_valid())
