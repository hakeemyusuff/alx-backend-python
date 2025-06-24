FROM python:3.10

WORKDIR /app

COPY Requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

RUN echo "docker run -p 8000:8000 messaging_app_image"
