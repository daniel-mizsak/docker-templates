FROM python:latest

WORKDIR /workdir

COPY workdir/ .

RUN pip install -r /workdir/requirements.txt

CMD ["python", "main.py"]
