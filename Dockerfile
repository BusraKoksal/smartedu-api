#  Hangi Python sürümünü kullanacağız?
FROM python:3.11-slim

#  Docker içindeki çalışma klasörümüzü belirliyoruz
WORKDIR /app

#  Kütüphane listesini Docker'ın içine kopyalıyoruz
COPY requirements.txt /app/

#  Kütüphaneleri Docker'ın içine yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

#  Tüm proje kodlarını Docker'ın içine kopyalıyoruz
COPY . /app/

#  Projeyi dış dünyaya hangi porttan açacağız?
EXPOSE 8000

#  Proje nasıl çalışacak?
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]