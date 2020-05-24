FROM python:3.8-slim
WORKDIR /build

COPY . .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

CMD ["gunicorn", "app:app", "-k", "gevent", "-b", "0.0.0.0:80"]