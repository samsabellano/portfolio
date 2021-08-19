from django import forms
from .models import (Comment)



# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_fullname', 'comment_email', 'comment_description']

        widgets = {
            'comment_fullname': forms.TextInput(
                attrs={
                    'class': '_comment_input_fields mb-4',
                    'placeholder': 'Fullname'
                }
            ),
            'comment_email': forms.EmailInput(
                attrs={
                    'class': '_comment_input_fields mb-4',
                    'placeholder': 'Email'
                }
            ),
            'comment_description': forms.Textarea(
                attrs={
                    'class': '_comment_input_fields _custom_textarea mb-4',
                    'placeholder': 'Your message'
                }
            ),

        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for input_field in self.fields:
            self.fields[input_field].required = True
            self.fields[input_field].label = ''