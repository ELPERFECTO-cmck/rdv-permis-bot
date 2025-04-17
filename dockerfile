FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y wget gnupg2 curl unzip fonts-liberation libglib2.0-0 libnss3 libgconf-2-4 libxss1 libasound2 libxtst6 libx11-xcb1 libatk-bridge2.0-0 libgtk-3-0

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Install specific ChromeDriver version manually (matching Chrome 122 for example)
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/122.0.6261.69/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver.zip

# Set environment for headless Chrome
ENV DISPLAY=:99

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Launch the bot
CMD ["bash", "start.sh"]

