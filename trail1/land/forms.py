from django import forms

class create_listing(forms.Form):
    area = forms.IntegerField()
    land_info = forms.CharField(label="Product Description", widget=forms.Textarea(attrs={'class':'form-control', 'id':'comment', 'row':'2','placeholder':'Product Description'}))
    land_image = forms.URLField(label="Product Image URL", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'id':'pro_deatils','placeholder':'Product Image URL'}))
    