from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from school.models import Student, School
from school.serializers import StudentSerializer, SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_fields = ('nationality', 'school',)
    search_fields = ('first_name', 'last_name',)
    ordering_fields = ('age', 'first_name', 'last_name',)

    def filter_queryset(self, queryset):
        if 'school_pk' in self.kwargs:
            queryset = queryset.filter(school_id=self.kwargs['school_pk'])
        queryset = super().filter_queryset(queryset)
        return queryset


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
