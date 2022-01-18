"""sample implementations for IntegrationPlugin"""
from plugin import IntegrationPluginBase
from plugin.mixins import AppMixin, GlobalSettingsMixin, UrlsMixin, NavigationMixin

from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url, include

from .views import RemoteOrderIndex


class MouserAPIKeyValidator(RegexValidator):

    def __call__(self, value):
        pass

class BoneMealPlugin(AppMixin, GlobalSettingsMixin, UrlsMixin, NavigationMixin, IntegrationPluginBase):
    """
    An full integration plugin
    """

    PLUGIN_NAME = "BoneMealPlugin"
    PLUGIN_SLUG = "bonemeal"
    PLUGIN_TITLE = "BoneMeal"

    NAVIGATION_TAB_NAME = "BoneMeal"
    NAVIGATION_TAB_ICON = 'fas fa-microchip'

    def view_test(self, request):
        """very basic view"""
        return HttpResponse(f'Hi there {request.user.username} this works')

    def setup_urls(self):

        return [
            url(r'^hi/', self.view_test, name='hi'),
            url(r'^list/', RemoteOrderIndex.as_view(), name='list'),
        ]

    SETTINGS = {
        'BONEMEAL_MOUSER_CART_API_KEY': {
            'name': _('Mouser Cart API Key'),
            'description': _('Used to fetch order information from Mouser'),
            'default': '',
            'validator': MouserAPIKeyValidator(),
        },
    }

    NAVIGATION = [
        {'name': 'List Remote Orders', 'link': 'plugin:bonemeal:list'},
    ]
