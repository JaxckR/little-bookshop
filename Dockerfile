FROM python:3.12-slim
WORKDIR /bookshop

COPY . .
RUN pip install -r requirements.txt

RUN python src/manage.py migrate

RUN python src/manage.py collectstatic

EXPOSE 8000

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]