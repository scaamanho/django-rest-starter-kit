from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework import generics, views, status
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import mixins

from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_url_kwarg = 'title'


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    #permission_classes = (IsAdminOrReadOnly, )

class TodoCustomView(generics.GenericAPIView):
    serializer_class = TodoSerializer
    @swagger_auto_schema(manual_parameters = [openapi.Parameter('complete', openapi.IN_QUERY, description="completed", type=openapi.TYPE_BOOLEAN),])
    def get(self, request, *args, **kwargs):
        complete = request.query_params.get('complete', False)
        query = Todo.objects.filter(completed=complete)
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Not Implemented'}, status=status.HTTP_204_NO_CONTENT)
    def put(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Not Implemented'}, status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(responses= {200 : "{'message':'result'}",
                                    204 : "{'message':'Not Implemented'}",
                                    400 : "{'message':'error'}"})
    def delete(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Not Implemented'}, status=status.HTTP_204_NO_CONTENT)

class TodoCustomCompleted(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Todo.objects.filter(completed=True)
    serializer_class = TodoSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)