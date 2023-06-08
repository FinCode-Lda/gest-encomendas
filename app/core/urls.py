from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (PessoaViewSet, TransportadorViewSet, RemetenteViewSet,
                    ReceptorViewSet, ViaturaViewSet, RotaViewSet,
                    CategoriaCargaViewSet, TarifaPesoViewSet,
                    TarifaVolumeViewSet, ServicoViewSet, CargaViewSet)

router = DefaultRouter()
router.register('pessoas', PessoaViewSet)
router.register('transportadores', TransportadorViewSet)
router.register('remetentes', RemetenteViewSet)
router.register('receptores', ReceptorViewSet)
router.register('viaturas', ViaturaViewSet)
router.register('rotas', RotaViewSet)
router.register('categorias-carga', CategoriaCargaViewSet)
router.register('tarifas-peso', TarifaPesoViewSet)
router.register('tarifas-volume', TarifaVolumeViewSet)
router.register('servicos', ServicoViewSet)
router.register('cargas', CargaViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]
