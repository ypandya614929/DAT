from django import forms


class TextAnalyseForm(forms.Form):
   text = forms.CharField(max_length = 255)
  
class FeedbackForm(forms.Form):
	name = forms.CharField(max_length = 255)
	email = forms.CharField(max_length = 255)
	msg = forms.CharField(max_length = 255)

class TweetAnalyseForm(forms.Form):
   data = forms.CharField(widget=forms.Textarea)