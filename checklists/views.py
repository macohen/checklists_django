from django.shortcuts import render, render_to_response
from .models import Checklist
from rest_framework import serializers, viewsets
from rest_framework.response import Response

# Create your views here.
class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Checklist.objects.create(**validated_data)

    class Meta:
        model = Checklist
        fields = ('checklistId','dateCreated', 'title')


class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

    def list(self, request):
        checklists = Checklist.objects.all()
        serializer = self.get_serializer(checklists, many=True)

        return Response(serializer.data)

def home(request):
    return render_to_response('index.html')