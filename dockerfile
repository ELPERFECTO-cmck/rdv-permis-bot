FROM seleniarm/standalone-chromium:latest

# Installe Python & pip
USER root
RUN apt-get update && apt-get install -y python3 python3-pip

# Copie des fichiers
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]



