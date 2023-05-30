FROM python:3.11.1

WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
