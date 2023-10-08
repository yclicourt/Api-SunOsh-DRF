from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from apps.base.utils import validate_files
from apps.products.api.serializers.general_serializers import(
    TextButtonSerializer
)

class TextButtonViewSet(viewsets.ModelViewSet):
    serializer_class = TextButtonSerializer
    parser_classes = (JSONParser,MultiPartParser, )

    def get_queryset(self,pk=None):
        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        text_button_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": text_button_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        
        data = validate_files(request.data,'image')
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Texto del boton creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            
            data = validate_files(request.data, 'image', True)
            text_button_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if text_button_serializer.is_valid():
                text_button_serializer.save()
                return Response({'message':'Texto del boton actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':text_button_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        text_button = self.get_queryset().filter(id=pk).first()      
        if text_button:
            text_button.state = False
            text_button.save()
            return Response({'message':'Texto del boton eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Texto del boton con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)