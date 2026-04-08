"""
WSGI config for the portfolio project.

This module exposes the WSGI callable as a module-level variable named
``application``. It is used by Django’s deployment utilities and by
WSGI servers. No modifications are typically required here.
"""

from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()