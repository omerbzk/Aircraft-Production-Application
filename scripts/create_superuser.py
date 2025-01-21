import os
from django.contrib.auth.models import User

# Django'nun ayarlarını yükleyin
import django
django.setup()

# Süper kullanıcıyı oluştur
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'newAdmin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'newAdmin@example.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', '1a3d5m7i9n11')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")
else:
    print(f"Superuser '{username}' already exists.")
