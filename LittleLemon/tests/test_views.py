from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer
from django.urls import reverse


class MenuViewTest(TestCase): 
    def setUp(self):
        Menu.objects.create(name='Icecream', price=10, inventory=10)
        Menu.objects.create(name='Cake', price=20, inventory=20)
        Menu.objects.create(name='Bread', price=30, inventory=30)
        
    def test_getall(self): 
        client = Client() 
        response = client.get(reverse('menu')) 
        menu = Menu.objects.all() 
        serializer = MenuSerializer(menu, many=True) 
        self.assertEqual(response.data, serializer.data) 
        self.assertEqual(response.status_code, 200) 