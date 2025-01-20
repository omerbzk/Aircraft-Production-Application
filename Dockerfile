FROM python:3.9

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . /app/

# Statik dosyaları topla
RUN python manage.py collectstatic --noinput

# Django yönetim komutlarını çalıştır ve veritabanı migrasyonlarını uygula
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]