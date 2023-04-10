# FROM python:3.9
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# ADD requirements.txt .
# RUN pip install -r requirements.txt
# ADD /djangoproject/ .
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./djangoproject /code/

EXPOSE 8000

RUN echo $(ls djangoproject/)

RUN ls

RUN pwd


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]