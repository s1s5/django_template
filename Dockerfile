FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py ./
COPY djtemplate ./djtemplate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
