from django.contrib.postgres.search import SearchVector, SearchQuery
from .models import Equipment, Department
from  work_orders.models import ScheduledWorkOrder, UnscheduledWorkOrder

def search_all_models_full_text(term):
    search_query = SearchQuery(term)

    results = {
        'Equipment': Equipment.objects.annotate(
            search=SearchVector('asset_tag', 'serial_no', 'model', 'purchase_order_number', 'name', 'description')
        ).filter(search=search_query),
        'Department': Department.objects.annotate(
            search=SearchVector( 'name' )
        ).filter(search=search_query),
        'ScheduledWorkOrder': ScheduledWorkOrder.objects.annotate(
            search=SearchVector('work_order_num', 'purchase_order')
        ).filter(search=search_query),
        'UnscheduledWorkOrder': UnscheduledWorkOrder.objects.annotate(
            search=SearchVector('work_order_num', 'purchase_order', 'problem', 'update')
        ).filter(search=search_query),
        # Add additional models with relevant fields here
    }
    return results
