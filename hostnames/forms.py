from django import forms
from .models import HostNames
from urlparse import urlparse

class LoginForm(forms.ModelForm):
    """
    Form for login.
    """
    url = forms.URLField(required=True, min_length=5, max_length=30)
    username = forms.CharField(label='Username', required=True, min_length=5, max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True, min_length=5, max_length=30)

    class Meta:
        model = HostNames
        fields = ['url', 'username', 'password']    # Fields to be used for creating form

    def save(self, commit=True):
        '''Overriding save to allow 
        '''
        user = super(LoginForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            # Adding hostname to the db
            user.hostname = str(urlparse(user.url).hostname)
            user.save()
        return user