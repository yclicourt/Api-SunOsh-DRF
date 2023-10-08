from apps.products.models import Product

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')

    def validate_name(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar un nombre")
        return value

    """ def validate_image(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una imagen para el producto.")
        return value """

    def validate_description(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una descripcion del Producto.")
        return value
    
    def validate(self, data):

        if 'name' not in data.keys():
            raise serializers.ValidationError({
                "name": "Debe ingresar un nombre del Producto."
            })


        if 'description' not in data.keys():
            raise serializers.ValidationError({
                "description": "Debe ingresar una descripcion para el producto."
            })
        
        if 'image' not in data.keys():
            raise serializers.ValidationError({
                "image": "Debe ingresar una imagen para el producto."            
            })
        
        return data
    
    
    def to_representation(self, instance):
        return  {
            'id': instance.id,
            'name':instance.name,
            'image':instance.image.url if instance.image != '' else '',
            'description':instance.description,
        }