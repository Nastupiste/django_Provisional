from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(AbstractUser):
    vip = models.BooleanField(default=False)
    saldo = models.DecimalField(
        default=0.00, max_digits=14, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.username


class Marca(models.Model):
    nombre = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.TextField(max_length=150)
    modelo = models.TextField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    unidades = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    precio = models.DecimalField(
        max_digits=14, decimal_places=2, validators=[MinValueValidator(0)])
    vip = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre+" "+self.modelo

    class Meta:
        unique_together = ['marca', 'modelo']
        # verbose_name_plural="Productos"


class Compra(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    producto = models.OneToOneField(Producto, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    unidades = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    importe = models.DecimalField(
        max_digits=14, decimal_places=2, validators=[MinValueValidator(0)])
    iva = models.FloatField(default=1.21)

    def __str__(self):
        return "Usuario: +"+self.user.username+" :"+self.producto.nombre+", unidades: "+self.unidades

    class Meta:
        unique_together = ['user', 'producto', 'fecha']

    def calcularImporte(self):
        self.importe = self.producto.precio*self.unidades*self.iva
