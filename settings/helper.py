"""
Helper functions for settings

Authors: Chris Mann
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from dotenv import load_dotenv  # Pour les variables d'.env
from urllib.parse import urlparse

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Prendre les variables d'environnement
load_dotenv()

# REQUIRED = ["DATABASE_URL", "SITE_NAME", "SECRET_KEY", "WAGTAILTRANSFER_SECRET_KEY", "HOST_NAME"]
REQUIRED = ["ALLOWED_HOSTS", "SECRET_KEY",]

needs_required = []
for i in REQUIRED:
    if not os.getenv(i) != "":
        needs_required.append(i)

if needs_required != []:
    raise ValueError("Merci de mettre les variables suivantes dans .env: %s" % ", ".join(needs_required))

DEBUG = True if os.getenv("DEBUG") == "True" else False
DEBUG_TOOLBAR = True if os.getenv("DEBUG_TOOLBAR") == "True" else False

HOST_NAME = os.getenv("HOST_NAME", "localhost")

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1, localhost").replace(" ", "").split(",")
CSRF_TRUSTED_ORIGINS = []
for host in ALLOWED_HOSTS:
    CSRF_TRUSTED_ORIGINS.append("https://" + host)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///%s/db.sqlite3" % BASE_DIR)  # Lire depuis .env

STATIC_ROOT = os.path.join(BASE_DIR, os.getenv("STATIC_ROOT","static"))

MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv("MEDIA_ROOT","media"))

SITE_URL = os.getenv("SECRET_KEY")