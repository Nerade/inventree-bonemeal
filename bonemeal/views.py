from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView

from InvenTree.views import InvenTreeRoleMixin
from order.models import PurchaseOrder

class RemoteOrderIndex(InvenTreeRoleMixin, ListView):
    """ List view for all purchase orders """

    model = PurchaseOrder
    template_name = 'bonemeal/remote_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        """ Retrieve the list of purchase orders,
        ensure that the most recent ones are returned first. """

        queryset = PurchaseOrder.objects.all().order_by('-creation_date')

        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        return ctx