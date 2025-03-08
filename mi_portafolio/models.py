from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# MODELO USUARIOS


class LoginUs(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name="loginus_groups", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="loginus_permissions", blank=True)

    class Meta:
        db_table = "login_usuarios"

    def __str__(self):
        return f"Usuario: {self.username}"

# MODELOS BASES DE DATOS


class bd_1(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField()
    mensaje = models.TextField(blank=False)

    class Meta:
        db_table = "contacto_usuarios"

    def __str__(self):
        return f"Usuario {self.nombre}"


class bd_2(models.Model):
    nombre_completo = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15, unique=True)
    pais = models.CharField(max_length=10)
    mensaje = models.TextField()

    class Meta:
        db_table = "contacto_Profesionales"

    def __str__(self):
        return f"Usuario {self.nombre_completo}"


# MODELOS BASES BLOG

class Post(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "base_post"

    def __str__(self):
        return self.titulo


class Comentario(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    respuestas_a = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="respuestas")

    class Meta:
        db_table = "conbase_comentario"

    def __str__(self):
        if self.respuestas_a:
            return f"Respuesta de {self.nombre} a {self.respuestas_a.nombre} en {self.post.titulo}"
        return f"Comentario de {self.nombre} en {self.post.titulo}"
