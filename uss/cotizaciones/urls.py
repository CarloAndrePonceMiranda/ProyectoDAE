from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    CotizacionList,
    CotizacionDetail,
    CotizacionCreation,
    CotizacionUpdate,
    CotizacionDelete
)
urlpatterns = [
    url(r'^$',views.principal, name='home'),
    url(r'^listadeclientes/', login_required(CotizacionList.as_view()), name='list'),
    url(r'^(?P<pk>\d+)$', login_required(CotizacionDetail.as_view()), name='detail'),
    url(r'^nuevo', login_required(CotizacionCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)', login_required(CotizacionUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)', login_required(CotizacionDelete.as_view()), name='delete'),
]