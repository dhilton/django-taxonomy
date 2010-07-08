import re
from django import forms

from taxonomy.models import Taxonomy, TaxonomyTerm, Taxon



class TaxonomyForm(forms.Form):
       """
       Displays the current live taxonomy and allows you
       to select and terms that match your current object
       and create Taxon between them.   
       """
	
       def __init__(self, *args, **kwargs):
            super(TaxonomyForm,self).__init__(*args, **kwargs)
            self.taxonomies = Taxonomy.objects.all()
            self.fields = {}
            for obj in self.taxonomies:
		self.fields[obj.name] = forms.ModelMultipleChoiceField(queryset=obj.taxonomyterm_set.all(), widget=forms.CheckboxSelectMultiple() )


