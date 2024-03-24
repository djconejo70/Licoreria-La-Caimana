# from django import forms



# class ReportForm(forms.Form):
#     desde = forms.DateField(
#     label="Desde: ",
#     required=True,
#     widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
#     input_formats=["%Y-%m-%d"])
    
#     hasta = forms.DateField(
#     label="Hasta",
#     required=True,
#     widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
#     input_formats=["%Y-%m-%d"])



from django.forms import *



class ReportForm(Form):
    date_range = CharField(widget=TextInput(attrs={
        'class':'form-control',
        'autocomplete': 'off'
    }))
    