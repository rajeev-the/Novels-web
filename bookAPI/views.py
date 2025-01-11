

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Novel
from .serializers import NovelSerializer

class NovelList(APIView):
    def get(self, request):
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NovelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
