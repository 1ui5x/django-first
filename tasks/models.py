from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    datecreated=models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True)
    important=models.BooleanField(default=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - By - '+ self.user.username

class Monedas(models.Model):
    mon_nombre=models.CharField(max_length=100)
    mon_simbolo=models.CharField(max_length=10)
    mon_iso=models.CharField(max_length=4)
    mon_estado=models.BooleanField(default=True)
    mon_user_ingresa=models.ForeignKey(User, on_delete=models.CASCADE)
    mon_user_modifica=models.ForeignKey(User, on_delete=models.CASCADE, related_name='mon_user_modifica', null=True, blank=True)
    mon_fecha_ingresa=models.DateTimeField(auto_now_add=True)
    mon_fecha_modifica=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Paises(models.Model):
    pai_nombre=models.CharField(max_length=100)
    pai_capital=models.CharField(max_length=100)
    pai_iso=models.CharField(max_length=4)
    pai_moneda_principal=models.ForeignKey(Monedas, on_delete=models.CASCADE)
    pai_moneda_2=models.ForeignKey(Monedas, on_delete=models.CASCADE, related_name='pai_moneda_2', null=True, blank=True)
    pai_moneda_3=models.ForeignKey(Monedas, on_delete=models.CASCADE, related_name='pai_moneda_3', null=True, blank=True)  
    pai_estado=models.BooleanField(default=True)
    pai_user_ingresa=models.ForeignKey(User, on_delete=models.CASCADE)
    pai_user_modifica=models.ForeignKey(User, on_delete=models.CASCADE, related_name='pai_ modifica', null=True, blank=True)
    pai_fecha_ingresa=models.DateTimeField(auto_now_add=True)
    pai_user_modifica=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Departamentos(models.Model):
    dep_codigo=models.CharField(max_length=2)
    dep_nombre=models.CharField(max_length=100)
    dep_latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, null=True, blank=True)
    dep_longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, null=True, blank=True)
    dep_estado=models.BooleanField(default=True)
    dep_user_ingresa=models.ForeignKey(User, on_delete=models.CASCADE)
    dep_user_modifica=models.ForeignKey(User, on_delete=models.CASCADE, related_name='dep_user_modifica', null=True, blank=True)
    dep_fecha_ingresa=models.DateTimeField(auto_now_add=True)
    dep_fecha_modifica=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Municipios(models.Model):
    mun_codigo=models.CharField(max_length=4)
    mun_nombre=models.CharField(max_length=100)
    mun_departamento=models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    mun_latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    mun_longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    mun_estado=models.BooleanField(default=True)
    mun_user_ingresa=models.ForeignKey(User, on_delete=models.CASCADE)
    mun_user_modifica=models.ForeignKey(User, on_delete=models.CASCADE, related_name='mun_user_modifica', null=True, blank=True)
    mun_fecha_ingresa=models.DateTimeField(auto_now_add=True)
    mun_fecha_modifica=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Empresas(models.Model):
    emp_nit=models.CharField(max_length=20)
    emp_nombre=models.CharField(max_length=200)
    emp_direccion=models.CharField(max_length=300)
    emp_telefono=models.CharField(max_length=15)
    emp_email=models.EmailField()
    emp_municipio=models.ForeignKey(Municipios, on_delete=models.CASCADE)
    emp_estado=models.BooleanField(default=True)
    emp_user_ingresa=models.ForeignKey(User, on_delete=models.CASCADE)
    emp_user_modifica=models.ForeignKey(User, on_delete=models.CASCADE, related_name='emp_user_modifica', null=True, blank=True)
    emp_fecha_ingresa=models.DateTimeField(auto_now_add=True)
    emp_fecha_modifica=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
