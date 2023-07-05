from django.db import models
from users.models import User

STATUS_CARGA = (
    ('Pendente', 'Pendente'),
    ('Progresso', 'Progresso'),
    ('Armazenada', 'Armazenada'),
    ('Levantada', 'Levantada'),
)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    contacto = models.CharField(max_length=15)

class Transportador(Pessoa):
    pass

    def __str__(self) -> str:
        return self.nome
    
class Remetente(Pessoa):
    pass

    def __str__(self) -> str:
        return self.nome

class Receptor(Pessoa):
    pass

    def __str__(self) -> str:
        return self.nome
    
class Viatura(models.Model):
    matricula = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.matricula

class Rota(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descricao 
    
class CategoriaCarga(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categorias Carga'

    def __str__(self) -> str:
        return self.descricao
    
class TarifaPeso(models.Model):
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    categoria_carga = models.ForeignKey(CategoriaCarga, related_name='tarifa_peso', on_delete=models.CASCADE)
    valor_comercial = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Tarifas por Peso'

    def __str__(self) -> str:
        return f'{self.categoria_carga.descricao} - Valor comercial {self.valor_comercial} MT'

class TarifaVolume(models.Model):
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    categoria_carga = models.ForeignKey(CategoriaCarga, related_name='tarifa_carga', on_delete=models.CASCADE)
    valor_comercial = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Tarifa por Volume'
        verbose_name_plural = 'Tarifas por Volume'

    def __str__(self) -> str:
        return f'{self.categoria_carga.descricao} - Valor Comercial {self.valor_comercial} MT'

class Servico(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

class Carga(models.Model):
    codigo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor_comercial = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tarifa_peso = models.ForeignKey(TarifaPeso, on_delete=models.CASCADE, null=True, blank=True)
    tarifa_volume = models.ForeignKey(TarifaVolume, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    data_partida = models.DateField()
    data_chegada = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS_CARGA)
    remetente = models.ForeignKey(Remetente, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    transportador_principal = models.ForeignKey(Transportador, on_delete=models.CASCADE, related_name='transportador_principal')
    viatura_principal = models.ForeignKey(Viatura, on_delete=models.CASCADE, related_name='viatura_principal')
    transportador_secundario = models.ForeignKey(Transportador, on_delete=models.CASCADE, null=True, blank=True, related_name='transportador_secundaria')
    viatura_secundaria = models.ForeignKey(Viatura, on_delete=models.CASCADE, null=True, blank=True, related_name='viatura_secundaria')
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='criado_por')
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modificado_por')
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.codigo

class Notificacao(models.Model):
    carga = models.ForeignKey(Carga, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carga.codigo


class CargaStock(models.Model):
    carga = models.OneToOneField(Carga, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.carga.codigo} - {self.quantity}"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Stock-In'),
        ('OUT', 'Stock-Out'),
    )

    carga = models.ForeignKey(Carga, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.carga.codigo} - {self.type} - {self.quantity}"

    def save(self, *args, **kwargs):
        # update the stock when a transaction is saved
        stock, created = CargaStock.objects.get_or_create(carga=self.carga)

        if self.type == 'IN':
            stock.quantity += self.quantity
        elif self.type == 'OUT':
            if self.quantity <= stock.quantity:
                stock.quantity -= self.quantity
            else:
                raise ValueError("Stock is not sufficient")

        stock.save()

        super().save(*args, **kwargs)
