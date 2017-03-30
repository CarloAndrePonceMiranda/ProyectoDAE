from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ClienteList,
    ClienteDetail,
    ClienteCreation,
    ClienteUpdate,
    ClienteDelete
)
urlpatterns = [
    url(r'^$',views.principal, name='home'),
    url(r'^listadeclientes/', login_required(ClienteList.as_view()), name='list'),
    url(r'^(?P<pk>\d+)$', ClienteDetail.as_view(), name='detail'),
    url(r'^nuevo', login_required(ClienteCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)', login_required(ClienteUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)', login_required(ClienteDelete.as_view()), name='delete'),
]