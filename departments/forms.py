from django import forms
from . import models


class DepartmentForm(forms.ModelForm):
    """
    Form to create and edit departments.

    This form handles the 'name' and 'description' fields of the Department model,
    applying specific CSS classes for consistent styling and appearance.
    """

    class Meta:
        model = models.Department
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter department description",
                }
            ),
        }
        labels = {
            "name": "Nome",
            "description": "Descrição",
        }
