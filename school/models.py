from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from hashids import Hashids

hashid = Hashids(settings.STUDENT_ID_SALT, min_length=8)


class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


def max_students_validator(school):
    if school.students.count() >= school.max_students:
        raise ValidationError(
            _('Maximum students reached')
        )


class Student(models.Model):
    student_id = models.CharField(max_length=20, null=True, unique=True, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    age = models.PositiveSmallIntegerField()
    nationality = CountryField()

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students',
                               validators=[max_students_validator])

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.student_id}: {self.full_name}'


@receiver(models.signals.post_save, sender=Student)
def student_post_save_handler(sender, instance, *args, **kwargs):
    if not instance.student_id:
        instance.student_id = hashid.encode(instance.pk)
        instance.save()
