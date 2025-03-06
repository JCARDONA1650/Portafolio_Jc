from django.shortcuts import render, redirect, get_object_or_404
from .forms import Formulario1, Formulario2, RegistroForm, LoginForm, ComentarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Comentario

# VISTA DE REGISTRO


def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            login(request, usuario)
            return redirect("registro_exitoso")
        else:
            messages.error(
                request, "Hubo un error en el formulario. Revisa los campos.")

    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form})


# VISTA DE REGISTRO EXITOSO
def registro_exitoso_view(request):
    return render(request, "registro_exitoso.html")


def login_exitoso_view(request):
    return render(request, "login_exitoso.html")


# VISTA DE LOGIN


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_us')

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, "¡Bienvenido!")  # Mensaje de exito
            return redirect("login_exitoso")
        else:
            # Mensaje de error
            messages.error(request, "❌ Usuario o contraseña incorrectos.")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

# VISTA DE SALIR DE LOGIN


def logout_view(request):
    logout(request)
    return redirect("index")


# VISTA DE HOME USUARIO


def home_usView(request):
    return render(request, 'home_us.html')


# VISTA DE HOME


def indexview(request):
    return render(request, 'index.html')

# VISTA DE INFORMACION


def infoview(request):
    return render(request, 'info.html')


# VISTA DE CLIENTES
def clientesviews(request):
    return render(request, 'clientes.html')


# VISTA DE FORMULARIO DE BLOG POST


def blogviews(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get("post_id")
            # ID del comentario al que se responde
            respuesta_a_id = request.POST.get("respuesta_a_id", None)

            post = get_object_or_404(Post, id=post_id)
            comentario = form.save(commit=False)
            comentario.post = post

            if respuesta_a_id:  # Si hay un comentario padre, lo asignamos
                comentario.respuestas_a = Comentario.objects.get(
                    id=respuesta_a_id)

            comentario.save()
            return redirect('blog')

    else:
        form = ComentarioForm()

    return render(request, 'blog.html', {'posts': posts, 'form': form})


# VISTA DE EORKSPACE


def workiews(request):
    return render(request, 'workspace.html')


# VISTA DE CONTACTO
def contactoviews(request):
    return render(request, 'contacto.html')


# Definicion de Formulario 1


def formularioviews(request):

    form1 = Formulario1()
    form2 = Formulario2()

    # Validacion si el usuario realizo el envio
    if request.method == 'POST':
        if 'submit_form1' in request.POST:
            form1 = Formulario1(request.POST)
            if form1.is_valid():
                form1.save()
                messages.success(
                    request, "Su Mensaje a sido Enviado con Exito")
                return redirect('formulario')
            else:
                messages.error(
                    request, "Error al enviar el mensaje, verifique datos e intente de nuevo")

        elif 'submit_form2' in request.POST:
            form2 = Formulario2(request.POST)
            if form2.is_valid():
                form2.save()
                messages.success(
                    request, "Su Mensaje a sido Enviado con Exito")
                return redirect('formulario')
            else:
                messages.error(
                    request, "Error al enviar el mensaje, verifique datos e intente de nuevo")

    return render(request, "formulario.html", {
        "form1": form1,
        "form2": form2,
    })
