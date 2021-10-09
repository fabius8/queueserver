import django_tables2 as tables
from .models import QueueInfo
from .models import QueueInfoFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

class QueueTable(tables.Table):
    class Meta:
        model = QueueInfo
        template_name = 'django_tables2/bootstrap.html'

class FilteredPairListView(SingleTableMixin, FilterView):
    table_class = QueueTable
    model = QueueInfo
    template_name = 'django_tables2/bootstrap.html'
    filterset_class = QueueInfoFilter