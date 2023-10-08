from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.base.utils import validate_files
from apps.products.api.serializers.general_serializers import(
    GallerySerializer
)

class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    parser_classes = (JSONParser,MultiPartParser, )

    def get_queryset(self,pk=None):
        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        gallery_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": gallery_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        
        data = validate_files(request.data,'image')
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Galleria creada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            
            data = validate_files(request.data, 'image', True)
            gallery_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if gallery_serializer.is_valid():
                gallery_serializer.save()
                return Response({'message':'Galleria actualizada correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':gallery_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        gallery = self.get_queryset().filter(id=pk).first()      
        if gallery:
            gallery.state = False
            gallery.save()
            return Response({'message':'Galleria eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe una Galleria con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)