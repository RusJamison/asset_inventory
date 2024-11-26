from django import forms
from .models import UnscheduledWorkOrder, ScheduledWorkOrder


class ScheduledWorkOrderForm(forms.ModelForm):
    work_order_num = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    next_scheduled_action_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    last_serviced_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = ScheduledWorkOrder
        fields= ['work_order_num','scheduled_action','purchase_order','freq_interval','last_serviced_at','next_scheduled_action_date']


class UnScheduleWorkOrderForm(forms.ModelForm):
    problem = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control"})
    )
    update = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control"}),required=False
    )
    date_of_update = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required=False)
    closed_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','required':False}), required=False)
    work_order_report = forms.FileField(widget=forms.FileInput(), required=False)
    class Meta:
        model = UnscheduledWorkOrder
        fields = []
        fields= ['work_order_num','problem','work_carried','work_order_report',
                 'purchase_order','update','status', 'closed_at', 'date_of_update'
                 ]
