from .models import Device, Model
from . serializers import DeviceSereileizer, ModelSereileizer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response

# Create your views here.
# Device Serilizer
class DevicesView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        device = request.data["device"]
        devices = Device.objects.filter(category__name=device).distinct()
        serilizer = DeviceSereileizer(devices, many=True)

        return Response(serilizer.data)


#Device search view
class DeviceSearch(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, format=None):
        model = request.data["query"]
        models = Device.objects.filter(models__name__contains=model)
        serilizer = DeviceSereileizer(models, many=True)

        return Response(serilizer.data)