from .models import Equipment, Department
from django import forms


class EquipmentCreationForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control"})
    )
    price = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    serial_no = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    notes = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","rows":3}))
    in_use_as_of_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    warranty_start_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    warranty_end_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    purchase_order_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Equipment
        fields = [
            "asset_tag",
            "manufacturer",
            "model",
            "name",
            "description",
            "status",
            "price",
            "image",
            "serial_no",
        "user_manual",
            "in_use_as_of_date",
            "warranty_start_date",
            "warranty_end_date",
            "category",
            "service_provider",
        ]


class EquipmentUpdateForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control"})
    )
    class Meta:
        model = Equipment
        fields = [
            "asset_tag",
            "serial_no",
            "name",
            "description",
            "price",
            "image",
            "manufacturer",
            "user_manual",
            "model",
            "category",
            "status",
            "service_provider",
            "purchase_order_number"
        ]
