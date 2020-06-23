from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from school.models import Student, School


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedIdentityField(
        view_name='school-students-list',
        lookup_url_kwarg='school_pk'
    )

    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(CountryFieldMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        ordering = ('id',)
