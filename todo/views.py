from .models import Todo
from .serializers import TodoSerializer  # Serialiser
from rest_framework import generics  # Rest Framework


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
