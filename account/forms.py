from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .mixins import CustomClassMixin

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']

        if data == '' or data == None:
            return data
            
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
    
class UserEditForm(CustomClassMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        if data == '' or data == None:
            return data
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data
    
    
class ProfileRegistrationForm(CustomClassMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'mobile', 'photo', ]
        widgets = {
            'date_of_birth' : forms.DateInput(attrs={'type': 'date'})
        }

    def clean_mobile(self):
        data = self.cleaned_data['mobile']
        
        if data == '' or data == None:
            return data
        
        if Profile.objects.filter(mobile=data).exists():
            raise forms.ValidationError('Phone number already in use.')
        return data
    
class ProfileEditForm(CustomClassMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'mobile', 'photo', ]
        widgets = {
            'date_of_birth' : forms.DateInput(attrs={'type': 'date'})
        }

    def clean_mobile(self):
        data = self.cleaned_data['mobile']

        if data == '' or data == None:
            return data
        
        qs = Profile.objects.exclude(id=self.instance.id).filter(mobile=data)

        if qs.exists():
            raise forms.ValidationError('Phone number already in use.')
        return data