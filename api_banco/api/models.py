from django.db import models

# Create your models here.

class Usuario(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30,unique=True)
    contrasena=models.CharField(max_length=16)
    nombre = models.CharField(max_length=30)
    apellidos=models.CharField(max_length=60)
    #------------------
class Persona(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    salario=models.IntegerField()
    direccion=models.CharField(max_length=60)
    personas_sustento=models.IntegerField()
    #----------------------
class Empresa(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    salario_anual=models.IntegerField()
    cant_trabajadores=models.IntegerField()
    nombre_director=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    codigo=models.CharField(max_length=60)
    nombre_empresa=models.CharField(max_length=30)
    #----------------
class Solicitud(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto=models.IntegerField()
    estado=models.CharField(max_length=30,default='pendiente')
    descripcion=models.CharField(max_length=180)
    fecha=models.DateTimeField(auto_now_add=True)




