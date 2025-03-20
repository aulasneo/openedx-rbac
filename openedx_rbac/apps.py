"""
openedx_rbac Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginURLs, PluginSettings


class OpenedxRbacConfig(AppConfig):
    """
    Configuration for the openedx_rbac Django application.
    """

    name = 'openedx_rbac'
    
    plugin_app = {
        PluginURLs.CONFIG: {
            'cms.djangoapp': {
                PluginURLs.NAMESPACE: 'get_permissions',
                PluginURLs.REGEX: r'^api/v1/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },

        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                'common': {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            },
            'cms.djangoapp': {
                'common': {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            }
        }
    }
