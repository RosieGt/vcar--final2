from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carro(models.Model):

    codigo = models.CharField("Codigo", max_length=100)
    marca = models.CharField("Marca", max_length=100)
    modelo = models.CharField("Modelo", max_length=100)
    img = models.ImageField("Imagem", upload_to='imagens', null=True, blank=True)
    comprar = models.DateField("Data de compra")

    def __str__(self):
        return "{} - {}".format(self.marca, self.modelo)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        
class Cliente(models.Model):

    nome = models.CharField("Nome", max_length=250)
    cpf = models.CharField("CPF", max_length=15)
    data_nascimento = models.DateField("Data de nascimento")

    def __str__(self):
        return "{}".format(self.nome)
    
    class Meta:
        verbose_name_plural = "Clientes" 

class Aluguel(models.Model):

    codigo = models.CharField("Codigo", max_length=100)
    data_aluguel = models.DateField("Data de aluguel")
    data_entrega = models.DateField("Data da entrega")
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2)
    devolucao = models.BooleanField("Devolvido")
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente_alugueis', verbose_name="Cliente")
    carro = models.ForeignKey(Carro, on_delete=models.DO_NOTHING, related_name='carro_alugueis', verbose_name="carro") 

    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.cliente.nome, self.carro.modelo)

    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"

class Perfil(models.Model):

    nome_completo = models.CharField("Nome", max_length=250, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.nome)
    
    class Meta:
        verbose_name_plural = "Perfis"                       