FROM selenium/standalone-chrome:latest

USER root

# Installe Python + pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copie des fichiers et install Python requirements
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]




