FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--timeout", "100", "app:app"]