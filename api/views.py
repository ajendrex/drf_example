from example.models import Table
from rest_framework import viewsets
from api.serializers import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows registers to be viewed or edited.
    """
    queryset = Table.objects.all().order_by('number')
    serializer_class = TableSerializer