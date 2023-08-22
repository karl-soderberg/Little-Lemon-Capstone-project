from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name='Icecream', price=10, inventory=10)
        itemstr = item.get_item()
        
        self.assertEqual(itemstr, 'Icecream : 10')
        