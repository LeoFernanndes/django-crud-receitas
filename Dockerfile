
FROM python:3.8
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt
CMD ["/code/entrypoint.sh"]
COPY . /code/