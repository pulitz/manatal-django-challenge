from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.PositiveSmallIntegerField()


def max_students_validator(value):
    school = School.objects.get(pk=value)
    if school.students.count() >= school.max_students:
        raise ValidationError(
            _('Maximum students reached')
        )


class Student(models.Model):
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students',
                               validators=[max_students_validator])
