FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

# Dépendances nécessaires
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg2 fonts-liberation \
    libglib2.0-0 libnss3 libgconf-2-4 libxss1 libasound2 libxtst6 libx11-xcb1 libatk-bridge2.0-0 libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Installer Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Installer ChromeDriver compatible
RUN CHROME_VERSION=$(google-chrome --version | awk '{ print $3 }' | cut -d '.' -f 1) && \
    DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Installer pip et les dépendances Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier le code
COPY . .

CMD ["bash", "start.sh"]





