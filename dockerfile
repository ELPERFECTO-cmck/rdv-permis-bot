FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

# Installer Firefox + Geckodriver + dépendances
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget curl unzip gnupg2 \
    libgtk-3-0 libdbus-glib-1-2 libxt6 libx11-xcb1 libnss3 libxrandr2 libxcomposite1 libxdamage1 libxext6 libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Installer Geckodriver
RUN GECKO_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d '"' -f 4) && \
    wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/$GECKO_VERSION/geckodriver-$GECKO_VERSION-linux64.tar.gz && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz

# Installer Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]






