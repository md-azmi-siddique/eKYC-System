from rest_framework import viewsets
from . import models
from . import serializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer
            