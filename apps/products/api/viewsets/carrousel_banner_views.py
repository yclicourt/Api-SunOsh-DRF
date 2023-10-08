from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.base.utils import validate_files
from apps.products.api.serializers.general_serializers import(
    CarrouselBannerSerializer
)

class CarrouselBannerViewSet(viewsets.ModelViewSet):
    serializer_class = CarrouselBannerSerializer
    parser_classes = (JSONParser,MultiPartParser, )


    def get_queryset(self,pk=None):
        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        carrousel_banner_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": carrousel_banner_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        
        data = validate_files(request.data,'image')
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Carrousel del Banner Creado creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            
            data = validate_files(request.data, 'image', True)
            crrousel_banner_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if crrousel_banner_serializer.is_valid():
                crrousel_banner_serializer.save()
                return Response({'message':'Carrousel del Banner actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':crrousel_banner_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        crrousel_banner = self.get_queryset().filter(id=pk).first()      
        if crrousel_banner:
            crrousel_banner.state = False
            crrousel_banner.save()
            return Response({'message':'Carrousel del Banner  eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Carrousel del Banner con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)