from apps.products.models import Gallery,Contact,CarrouselBanner,SocialMedia,OurCompany,OurValue,NewsEmpresa,TextPage,TextButton,TextNavbar,SubCategoryProduct

from rest_framework import serializers


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ('state','created_date','modified_date','deleted_date')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ('state','created_date','modified_date','deleted_date')

class CarrouselBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarrouselBanner
        exclude = ('state','created_date','modified_date','deleted_date')

class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialMedia
        exclude = ('state','created_date','modified_date','deleted_date')

class OurCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = OurCompany
        exclude = ('state','created_date','modified_date','deleted_date')

class OurValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurValue
        exclude = ('state','created_date','modified_date','deleted_date')

class NewsEmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsEmpresa
        exclude = ('state','created_date','modified_date','deleted_date')

class TextPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextPage
        exclude = ('state','created_date','modified_date','deleted_date')

class TextButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextButton
        exclude = ('state','created_date','modified_date','deleted_date')

class TextNavbarSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextNavbar
        exclude = ('state','created_date','modified_date','deleted_date')

class SubCategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategoryProduct
        exclude = ('state','created_date','modified_date','deleted_date')


