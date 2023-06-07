from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.models import Carga

@receiver(pre_save, sender=Carga)
def calculate_total(sender, instance, **kwargs):
    if instance.tarifa_peso:
        instance.total = instance.peso * instance.tarifa_peso.preco
    elif instance.tarifa_volume:
        instance.total = instance.volume * instance.tarifa_volume.preco
