from django.db import models
from apps.base.models import BaseModel

# Create your models here.


class Product(BaseModel):
    name = models.CharField('Nombre',max_length=10,blank=False, null=False,unique=True)
    image = models.ImageField('Imagen',upload_to="",blank=True, null=True)
    description = models.CharField('Descripcion',max_length=30,blank=False, null=False,unique=True)
    

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Producto."""
        return self.name
    


class SubCategoryProduct(BaseModel):
    name = models.CharField('Nombre',max_length=10,blank=False, null=False,unique=True)
    banner = models.ImageField('Banner',upload_to='',blank=True , null=True)
    image = models.ImageField('Imagen',upload_to="",blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='Producto')

    class Meta:
        """Meta definition for SubcategoriaProducto."""

        verbose_name = 'SubcategoriaProducto'
        verbose_name_plural = 'SubcategoriaProductos'

    def __str__(self):
        """Unicode representation of SubcategoriaProducto."""
        return self.name
    

class Category(BaseModel):
    name = models.CharField('Nombre',max_length=10,blank=False, null=False,unique=True)
    subcategory = models.ForeignKey(SubCategoryProduct,on_delete=models.CASCADE ,verbose_name='Subcategoria del Producto')
    image = models.ImageField('Imagen',upload_to="",blank=True, null=True)
    subcategory = models.ForeignKey(SubCategoryProduct,on_delete=models.CASCADE,verbose_name='Subcategoria')

    class Meta:
        """Meta definition for Categoria del Producto."""

        verbose_name = 'CategoriaProducto'
        verbose_name_plural = 'Categoria del Productos'

    def __str__(self):
        """Unicode representation of CategoriaProducto."""
        return self.name
    
class Gallery(BaseModel):
    location = models.CharField('Locacion',max_length=10,blank=False, null=False,unique=True)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Categoria del Producto')
    image = models.ImageField('Imagen',upload_to="",blank=True, null=True)

    class Meta:
        """Meta definition for Galeria."""

        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'

    def __str__(self):
        """Unicode representation of Galeria."""
        return self.location


class Contact(BaseModel):
    name = models.CharField('Nombre',max_length=10,blank=False,null=False,unique=True)
    lastName = models.CharField('Apellido',max_length=10,blank=False,null=False,unique=True)
    message = models.CharField('Mensaje',max_length=20,blank=False,null=False,unique=True)

    class Meta:
        """Meta definition for Contacto."""

        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        """Unicode representation of Contacto."""
        return self.name
    

class CarrouselBanner(BaseModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Categoria')
    subcategory = models.ForeignKey(SubCategoryProduct,on_delete=models.CASCADE,verbose_name='Subcategoria del Producto')
    image = models.ImageField('Imagen',upload_to="",blank=True, null=True)

    class Meta:
        """Meta definition for CarrouselBanner."""

        verbose_name = 'CarrouselBanner'
        verbose_name_plural = 'CarrouselBanners'


class SocialMedia(BaseModel):
    name = models.CharField('Nombre',max_length=10,blank=False,null=False,unique=True)
    image = models.ImageField('Imagen',upload_to="",blank=True, null=True)

    class Meta:
        """Meta definition for SocialMedia."""

        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'

    def __str__(self):
        """Unicode representation of SocialMedia."""
        return self.name

class OurCompany(BaseModel):
    title = models.CharField('Titulo',max_length=10,blank=False,null=False,unique=True)
    description = models.CharField('Descripcion',max_length=10,blank=False,null=False,unique=True)
    image = models.ImageField('Imagen',upload_to="",blank=True, null=True)

    class Meta:
        """Meta definition for OurCompany."""

        verbose_name = 'OurCompany'
        verbose_name_plural = 'OurCompanys'

    def __str__(self):
        """Unicode representation of OurCompany."""
        return self.title

class OurValue(BaseModel):
    title = models.CharField('Titulo',max_length=10,blank=False,null=False,unique=True)
    firstSubtitle = models.CharField('Primer Subtitulo',max_length=20,blank=False,null=False,unique=True)
    secondSubtitle = models.CharField('Segundo Subtitulo',max_length=20,blank=False,null=False,unique=True)

    class Meta:
        """Meta definition for OurValue."""

        verbose_name = 'OurValue'
        verbose_name_plural = 'OurValues'

    def __str__(self):
        """Unicode representation of OurValue."""
        return self.title

class NewsEmpresa(BaseModel):
    name = models.CharField('Nombre',max_length=10,blank=False,null=False,unique=True)
    image = models.ImageField('Image',upload_to="",blank=True, null=True)
    description = models.CharField('Descripcion',max_length=30,blank=False,null=False,unique=True)

    class Meta:
        """Meta definition for NewsEmpresa."""

        verbose_name = 'NewsEmpresa'
        verbose_name_plural = 'NewsEmpresas'

    def __str__(self):
        """Unicode representation of NewsEmpresa."""
        return self.name
    
class TextPage(BaseModel):
    page = models.CharField('Nombre de Pagina',max_length=10,blank=False,null=False,unique=True)
    title = models.CharField('Titulo de Pagina',max_length=20,blank=False,null=False,unique=True)
    subtitulo = models.CharField('Subtitulo de Pagina',max_length=20,blank=False,null=False,unique=True)

    class Meta:
        """Meta definition for TextPage."""

        verbose_name = 'TextPage'
        verbose_name_plural = 'TextPages'

    def __str__(self):
        """Unicode representation of TextPage."""
        return self.page
    
class TextButton(BaseModel):
    title = models.CharField('Titulo de Boton',max_length=20,blank=False,null=False,unique=True)

    class Meta:
        """Meta definition for TextButton."""

        verbose_name = 'TextButton'
        verbose_name_plural = 'TextButtons'

    def __str__(self):
        """Unicode representation of TextButton."""
        return self.title

class TextNavbar(BaseModel):
    title = models.CharField('Titulo de Navbar',max_length=20,blank=False,null=False,unique=True)

    class Meta:
        """Meta definition for TextNavbar."""

        verbose_name = 'TextNavbar'
        verbose_name_plural = 'TextNavbars'

    def __str__(self):
        """Unicode representation of TextNavbar."""
        return self.title