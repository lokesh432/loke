from django.forms import ModelForm
from testapp.models import Student


class UserModelForm(ModelForm):
     class Meta:
         model=Student
         fields='__all__'
