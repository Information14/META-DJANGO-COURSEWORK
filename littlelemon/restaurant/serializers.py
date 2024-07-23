from rest_framework import serializers
from .models import Menu 



class Menuserializer(serializers.ModelSerializer): 
    class Meta: 
        model = Menu
        fields = ['id', 'name', 'price', 'menu_item_description']