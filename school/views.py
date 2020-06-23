from rest_framework import viewsets

from school.models import Student, School
from school.serializers import StudentSerializer, SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        if 'school_pk' in self.kwargs:
            queryset = queryset.filter(school_id=self.kwargs['school_pk'])
        return queryset


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
