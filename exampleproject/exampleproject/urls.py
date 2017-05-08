"""exampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic
from django.http import HttpResponseNotFound
import django.contrib.auth.views as auth_views

from lifecard_akb.apps.lifecard.views import custom_password_reset
from lifecard_akb.apps.lifecard.views import CreditView as lifecard_CreditView


def required(wrapping_functions, patterns_rslt):
    if not hasattr(wrapping_functions, '__iter__'):
        wrapping_functions = (wrapping_functions,)
    return [
        _wrap_instance__resolve(wrapping_functions, instance)
        for instance in patterns_rslt
    ]


def _wrap_instance__resolve(wrapping_functions, instance):
    if not hasattr(instance, 'resolve'):
        return instance
    resolve = getattr(instance, 'resolve')

    def _wrap_func_in_returned_resolver_match(*args, **kwargs):
        rslt = resolve(*args, **kwargs)
        if not hasattr(rslt, 'func'):
            return rslt
        f = getattr(rslt, 'func')
        for _f in reversed(wrapping_functions):
            # @decorate the function from inner to outter
            f = _f(f)
        setattr(rslt, 'func', f)
        return rslt
    setattr(instance, 'resolve', _wrap_func_in_returned_resolver_match)
    return instance


mypage_patterns = required(
    login_required,
    [
    ]
)

staff_patterns = required(
    staff_member_required,
    [
    ]
)


urlpatterns = [
    url(r'^mypage/', include(mypage_patterns, namespace='mypage')),
    url(r'^staff/', include(staff_patterns, namespace='staff')),
    url(r'^admin/', admin.site.urls),
]


# media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

admin.site.site_header = '{} admin'.format(settings.PROJECT_NAME)
admin.site.index_title = '{} admin'.format(settings.PROJECT_NAME)
admin.site.site_title = '{} admin'.format(settings.PROJECT_NAME)
