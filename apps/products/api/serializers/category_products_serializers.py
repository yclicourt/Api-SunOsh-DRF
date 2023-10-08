from apps.products.models import Category

from rest_framework import serializers


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def validate_name(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar un nombre")
        return value
    
    def validate_subcategory(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una subcategoria")
        return value
    
    def validate_image(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una image")
        return value

    def validate(self, data):

        if 'name' not in data.keys():
            raise serializers.ValidationError({
                "name": "Debe ingresar un nombre."
            })


        if 'subcategory' not in data.keys():
            raise serializers.ValidationError({
                "subcategory": "Debe ingresar las subcategorias."
            })
        
        if 'image' not in data.keys():
            raise serializers.ValidationError({
                "image": "Debe ingresar una imagen para la categoria."            
            })
        
        
        return data
    
    def to_representation(self, instance):

        return  {
            'id': instance.id,
            'name':instance.name,
            'subcategory':instance.subcategory.name if instance.subcategory is not None else '',
            'image':instance.image.url if instance.image != '' else '',
        
        }
