from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class ExtendedUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


        class Meta:
            model = User
            fields = ('username', 'first_name',
                      'last_name', 'password1', 'password2')