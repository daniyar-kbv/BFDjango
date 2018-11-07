from django.forms import ModelForm
from main2.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', ]
