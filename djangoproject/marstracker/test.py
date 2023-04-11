import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Player
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class PlayerTest(TestCase):

    def setUp(self):
        self.player = Player.objects.create(first_name = "test", last_name = "testov")
       

    def test_create_player(self):
        #player = Player.objects.create(first_name = "test", last_name = "testov")
        self.assertEqual(Player.objects.count(),1)
        self.assertEqual(self.player.first_name,"test")
        self.assertEqual(self.player.last_name,"testov")
    
    def test_get_player(self):
        player = Player.objects.get(id=self.player.id)
        self.assertEqual(player.first_name,"test")
        self.assertEqual(player.last_name,"testov")

    def test_update_player(self):
        self.player.first_name = "update_test"
        self.player.save()
        player = Player.objects.get(id=self.player.id)
        self.assertEqual(player.first_name,"update_test")

    def test_delete_player(self):
        self.player.delete()
        self.assertEqual(Player.objects.count(), 0)

class UserAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password = 'testpassword')

    def test_login(self):
        response = self.client.post(reverse_lazy('marstracker:login'), {'username':'testuser','password':'testpassword'})
        self.assertEqual(response.status_code,302)
        self.assertTrue('_auth_user_id' in self.client.session)
        self.assertRedirects(response,reverse_lazy('marstracker:index'))
    
    def test_login_invalid_credentials(self):
        response = self.client.post(reverse_lazy('marstracker:login'), {'username':'testuser','password':'wrongpassword'})
        self.assertEqual(response.status_code,200)
        self.assertFalse('_auth_user_id' in self.client.session)

class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse_lazy('marstracker:logout'))
        self.assertEqual(response.status_code, 302) # check if the user was redirected
        self.assertFalse('_auth_user_id' in self.client.session) # check if the user is logged out
