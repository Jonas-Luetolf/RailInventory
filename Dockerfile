# Basisimage für Python 3.8
FROM python:3.10.5-slim-buster

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Kopieren Sie die Anforderungen in den Arbeitsbereich und installieren Sie sie
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Kopieren Sie den Rest des Codes in das Arbeitsverzeichnis
COPY forms forms
COPY application application
COPY main.py main.py
COPY config.py config.py

# Portnummer, auf dem der Container ausgeführt wird
EXPOSE 80



# Starten Sie die Anwendung
CMD ["gunicorn", "0.0.0.0:80", "main:app"]

