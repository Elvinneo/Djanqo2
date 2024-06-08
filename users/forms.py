from django import forms
from .models import Userss



class UserForm(forms.ModelForm):
    class Meta:
        model=Userss
        fields=['name','surname','email','addresstolive','address','specialty','age','hobbies','university']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'addresstolive': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'specialty': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'hobbies': forms.TextInput(attrs={'class':'form-control'}),
            'university': forms.TextInput(attrs={'class':'form-control'}),
        }



        
        

