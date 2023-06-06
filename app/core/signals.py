from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Carga

@receiver(pre_save, sender=Carga)
def calcular_total(sender, instance, **kwargs):
    if instance.tarifa_peso:
        instance.total = instance.peso * instance.tarifa_peso.valor
    elif instance.tarifa_volume:
        instance.total = instance.volume * instance.tarifa_volume.valor
