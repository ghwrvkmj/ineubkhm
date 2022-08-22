FROM python:3.9.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT booksellsite.wsgi