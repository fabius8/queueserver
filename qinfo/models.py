from django.db import models
import django_filters

# Create your models here.
class QueueInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    timestamp = models.CharField(max_length=100, verbose_name='timestamp')
    queue = models.IntegerField(verbose_name='queue', default=0)
    state = models.CharField(max_length=100, verbose_name='state')

class QueueInfoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = QueueInfo
        fields = ['name']