from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (PessoaSerializer, TransportadorSerializer, RemetenteSerializer,
                          ReceptorSerializer, ViaturaSerializer, RotaSerializer,
                          CategoriaCargaSerializer, TarifaPesoSerializer,
                          TarifaVolumeSerializer, ServicoSerializer, CargaSerializer)
from .models import (Pessoa, Transportador, Remetente, Receptor, Viatura, Rota,
                     CategoriaCarga, TarifaPeso, TarifaVolume, Servico, Carga)


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['nome', 'contacto']
    search_fields = ['nome', 'contacto']


class TransportadorViewSet(viewsets.ModelViewSet):
    queryset = Transportador.objects.all()
    serializer_class = TransportadorSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['nome', 'contacto']
    search_fields = ['nome', 'contacto']


class RemetenteViewSet(viewsets.ModelViewSet):
    queryset = Remetente.objects.all()
    serializer_class = RemetenteSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['nome', 'contacto']
    search_fields = ['nome', 'contacto']


class ReceptorViewSet(viewsets.ModelViewSet):
    queryset = Receptor.objects.all()
    serializer_class = ReceptorSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['nome', 'contacto']
    search_fields = ['nome', 'contacto']


class ViaturaViewSet(viewsets.ModelViewSet):
    queryset = Viatura.objects.all()
    serializer_class = ViaturaSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['matricula']
    search_fields = ['matricula']


class RotaViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['descricao']
    search_fields = ['descricao']


class CategoriaCargaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaCarga.objects.all()
    serializer_class = CategoriaCargaSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['descricao']
    search_fields = ['descricao']


class TarifaPesoViewSet(viewsets.ModelViewSet):
    queryset = TarifaPeso.objects.all()
    serializer_class = TarifaPesoSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['rota', 'categoria_carga', 'valor_comercial', 'preco']
    search_fields = ['rota__descricao', 'categoria_carga__descricao', 'valor_comercial', 'preco']


class TarifaVolumeViewSet(viewsets.ModelViewSet):
    queryset = TarifaVolume.objects.all()
    serializer_class = TarifaVolumeSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['rota', 'categoria_carga', 'valor_comercial', 'preco']
    search_fields = ['rota__descricao', 'categoria_carga__descricao', 'valor_comercial', 'preco']


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'price']


class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['codigo', 'status', 'remetente', 'receptor', 'rota',
                        'transportador_principal', 'viatura_principal',
                        'transportador_secundario', 'viatura_secundaria',
                        'criado_por', 'modificado_por']
    search_fields = ['codigo', 'descricao', 'status', 'remetente__nome',
                     'receptor__nome', 'rota__descricao',
                     'transportador_principal__nome', 'viatura_principal__matricula',
                     'transportador_secundario__nome', 'viatura_secundaria__matricula',
                     'criado_por__username', 'modificado_por__username']
