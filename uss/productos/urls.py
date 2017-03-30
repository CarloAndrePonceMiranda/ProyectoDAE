from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ProductoList,
    ProductoDetail,
    ProductoCreation,
    ProductoUpdate,
    ProductoDelete
)
urlpatterns = [
    url(r'^$',views.principal, name='home'),
    url(r'^listadeproductos/', login_required(ProductoList.as_view()), name='list'),
    url(r'^(?P<pk>\d+)$', login_required(ProductoDetail.as_view()), name='detail'),
    url(r'^nuevo', login_required(ProductoCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)', login_required(ProductoUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)', login_required(ProductoDelete.as_view()), name='delete'),
]