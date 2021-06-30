from django import forms
from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id','fullname','mobile','position']
        
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['mobile'].MinimumLengthValidator = 10
