from django import forms
from .models import categories

class create_listing(forms.Form):
    crop_name = forms.CharField(label="Product Name", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'id':'pro_deatils','placeholder':'Product Name'}))
    crop_info = forms.CharField(label="Product Description", widget=forms.Textarea(attrs={'class':'form-control', 'id':'comment', 'row':'2','placeholder':'Product Description'}))
    crop_image = forms.URLField(label="Product Image URL", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'id':'pro_deatils','placeholder':'Product Image URL'}))
    crop_cat_id = forms.ChoiceField(label="Product Categories", choices  = list((a.cat_name,a.cat_name) for a in categories.objects.all()), widget=forms.Select(attrs={'class':'form-control','placeholder':'Product Categories'}))
    crop_quantity = forms.IntegerField()
