"""
Views for the portfolio application.

Each view renders a template and passes a context dictionary containing
information about the user’s professional background. Placeholders are
used where appropriate so the user can easily customize content. Feel
free to extend the context with additional fields or query a database if
you wish to persist information dynamically.
"""

from __future__ import annotations

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """Render the home (landing) page."""
    context: dict[str, object] = {
        'name': 'Jorge Cardona',  # Replace with your name
        'title': 'Ingeniero de Sistemas',
        'tagline': 'Desarrollador web y emprendedor',
        'description': (
            'Soy un profesional apasionado por la tecnología y el desarrollo web. '
            'Me encanta construir aplicaciones que mejoren la vida de las personas '
            'y ayuden a las empresas a crecer.'
        ),
        'company_url': 'https://ambugroupllc.com',  # URL de tu empresa
        'github_url': 'https://github.com/tuusuario',  # Sustituye por tu perfil de GitHub
    }
    return render(request, 'home.html', context)


def experience(request: HttpRequest) -> HttpResponse:
    """Render the experience page."""
    experiences = [
        {
            'cargo': 'Desarrollador web full‑stack',
            'empresa': 'Ambu Group LLC',
            'periodo': '2022 – presente',
            'descripcion': (
                'Desarrollo y mantenimiento de aplicaciones web utilizando Django, HTML, '
                'CSS y JavaScript. Implementación de interfaces limpias y responsivas, '
                'integración con bases de datos y despliegue en la nube.'
            ),
            'link': 'https://ambugroupllc.com',
        },
        {
            'cargo': 'Administrador de granjas de crecimiento de redes sociales',
            'empresa': 'Proyecto personal',
            'periodo': '2021 – presente',
            'descripcion': (
                'Gestión de granjas de crecimiento no humano para redes sociales, '
                'utilizando estrategias automatizadas para incrementar seguidores y engagement '
                'de forma constante y natural.'
            ),
            'link': '',
        },
    ]
    context: dict[str, object] = {
        'experiences': experiences,
    }
    return render(request, 'experience.html', context)


def education(request: HttpRequest) -> HttpResponse:
    """Render the education page."""
    educations = [
        {
            'titulo': 'Ingeniería de Sistemas',
            'institucion': 'Universidad de Ejemplo',
            'periodo': '2017 – 2021',
            'descripcion': 'Formación en desarrollo de software, bases de datos y redes.',
        },
        {
            'titulo': 'Curso de Django Avanzado',
            'institucion': 'Plataforma Online',
            'periodo': '2022',
            'descripcion': 'Profundización en el framework Django para la creación de aplicaciones web completas.',
        },
    ]
    context: dict[str, object] = {'educations': educations}
    return render(request, 'education.html', context)


def skills(request: HttpRequest) -> HttpResponse:
    """Render the skills page."""
    skills_list = [
        'Python',
        'Django',
        'HTML5 & CSS3',
        'JavaScript (ES6+)',
        'Bootstrap y Tailwind CSS',
        'Git & GitHub',
        'SQL y ORM',
        'Docker',
        'Gestión de granjas de crecimiento en redes sociales',
    ]
    context: dict[str, object] = {'skills': skills_list}
    return render(request, 'skills.html', context)


def contact(request: HttpRequest) -> HttpResponse:
    """Render the contact page."""
    # Remove non‑numeric characters from the WhatsApp number to build the wa.me link
    raw_phone = '+57 320 282 8836'
    sanitized = ''.join(filter(str.isdigit, raw_phone))
    context: dict[str, object] = {
        'whatsapp': raw_phone,
        'whatsapp_link': sanitized,
        'instagram': '@jorgecardona16',
        'email': 'jorge80831@gmail.com',
    }
    return render(request, 'contact.html', context)