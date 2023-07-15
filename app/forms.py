
from django import forms
from app.forms import*
from app.models import*
class TopicModelForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
class WebpageModelForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        widgets={'topic_name':forms.RadioSelect}
        help_texts={'topic_name':'select required data'}
        labels={'name':'N'}

class AccessRecordModelForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'
        