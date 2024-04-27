from django.test import TestCase
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Pizza", price=45.99, inventory=50)
        self.menu2 = Menu.objects.create(title="Chicken and Chips", price=45.00, inventory=60)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        response = self.client.get('/api/menu-items/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
        
            