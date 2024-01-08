from django import forms
from app.models import *


class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        #fields=['topic_name']




class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #exclude=['topic_name']
        #labels={'topic_name':'tn'}
        #widgets={'name':forms.PasswordInput}
        #fields=['topic_name','name']


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'