from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Message, Application


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name',
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user','is_approved','has_applied','is_active', 'is_suspended']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


# class SkillForm(ModelForm):
#      class Meta:
#          model = Skill
#          fields='__all__'
#          exclude=['owner']
#      def __init__(self, *args, **kwargs):
#         super(SkillForm, self).__init__(*args, **kwargs)

#         for name,field in self.fields.items():
#             field.widget.attrs.update({'class':'input'})

class MessageForm(ModelForm):

    class Meta:
        model= Message
        fields=['name','email','subject', 'body','phone','education_level', 'age', 'county']
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ApplicationForm(ModelForm):
    class Meta:
        model= Application
        fields=['name','email','phone','education_level', 'age', 'county','valid_passport', 'valid_good_conduct', "job_title"]
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})