#Using python image
FROM python:3.10-slim

#used to tell the working directory
WORKDIR /app

#for installing packages
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#copy all the codes to of the application to google cloud
COPY . .

#exposing port 8080 for executing file
ENV PORT 8080

#for running the application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app