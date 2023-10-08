from rest_framework.routers import DefaultRouter
from apps.products.api.viewsets.carrousel_banner_views import CarrouselBannerViewSet
from apps.products.api.viewsets.contact_views import ContactViewSet
from apps.products.api.viewsets.gallery_views import GalleryViewSet
from apps.products.api.viewsets.news_empresa import NewsEmpresaViewSet
from apps.products.api.viewsets.our_company_views import OurCompanyViewSet
from apps.products.api.viewsets.social_media_views import SocialMediaViewSet
from apps.products.api.viewsets.our_value_views import OurValueViewSet
from apps.products.api.viewsets.text_page_views import TextPageViewSet
from apps.products.api.viewsets.text_button_views import TextButtonViewSet
from apps.products.api.viewsets.text_navbar_views import TextNavbarViewSet

from apps.products.api.viewsets.product_viewsets import ProductViewSet
from apps.products.api.viewsets.category_product_views import CategoryProductViewSet

router = DefaultRouter()

router.register(r'category-products',CategoryProductViewSet,basename='allcategories')
router.register(r'products',ProductViewSet,basename='products')
router.register(r'galleries',GalleryViewSet,basename='gallery')
router.register(r'contacts',ContactViewSet,basename='contact')
router.register(r'carrousel-banners',CarrouselBannerViewSet,basename='carrousel-banner')
router.register(r'social-medias',SocialMediaViewSet,basename='social-media')
router.register(r'our-companies',OurCompanyViewSet,basename='our-company')
router.register(r'our-values',OurValueViewSet,basename='our-value')
router.register(r'news-empresas',NewsEmpresaViewSet,basename='news-empresa')
router.register(r'text-pages',TextPageViewSet,basename='text-pages')
router.register(r'text-btns',TextButtonViewSet,basename='text-btns')
router.register(r'text-navbars',TextNavbarViewSet,basename='text-btns')


urlpatterns = router.urls