from rest_framework import viewsets

from school.models import Student, School
from school.serializers import StudentSerializer, SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        filters = {}
        if 'school_pk' in self.kwargs:
            filters['school_id'] = self.kwargs['school_pk']
        return Student.objects.filter(**filters)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
