import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelmanagement.settings")
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin123"
    )
    print("Superuser created.")
else:
    print("Superuser already exists.")
