from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Student(models.Model):
    """
    A model to store all student related details
    """
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    ]

    name = models.CharField(_("Name"), max_length=50, unique=True)
    age = models.IntegerField(_("Age"), blank=True)
    gender = models.CharField(_("Gender"), choices=GENDER_CHOICES,
                              max_length=30)
    reporting_teacher = models.ForeignKey("portal_user.Teacher",
                                          on_delete=PROTECT)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name


class MarkList(models.Model):
    """
    A model to store all student's Mark list related details
    """
    FIRST_TERM = "One"
    SECOND_TERM = "Two"
    TERM_CHOICES = [
        (FIRST_TERM, "First Term"),
        (SECOND_TERM, "Second Term")
    ]

    student = models.ForeignKey("portal_user.Student",
                                on_delete=CASCADE)
    term = models.CharField(_("Term"), choices=TERM_CHOICES,
                            max_length=30)
    maths = models.IntegerField(_("Maths"), validators=[MinValueValidator(0),
                                MaxValueValidator(50)], blank=True)
    science = models.IntegerField(_("Science"), validators=[
                                  MinValueValidator(0), MaxValueValidator(50)],
                                  blank=True)
    history = models.IntegerField(_("History"), validators=[
                                  MinValueValidator(0), MaxValueValidator(50)],
                                  blank=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True,
                                        blank=False)

    def __str__(self):
        return self.student.name + "," + self.term

    def get_full_marks(self):
        return self.maths + self.science + self.history
