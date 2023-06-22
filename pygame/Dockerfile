FROM python:3.9

WORKDIR /workdir

COPY ./workdir/ .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["python", "main.py"]