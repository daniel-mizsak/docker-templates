FROM python:latest

WORKDIR /workdir

COPY workdir/ .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
