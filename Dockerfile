FROM python:3.9

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . /app/

# Django yönetim komutlarını çalıştır
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]