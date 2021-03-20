from rest_framework import serializers 
from api.models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id',
                'title',
                'description',
                'completed')
