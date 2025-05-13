FROM python:3.10-slim

ENV CHROME_VERSION=124.0.6367.91

RUN apt-get update && \
    apt-get install -y wget unzip curl gnupg2 fonts-liberation libxss1 libappindicator3-1 libasound2 libatk-bridge2.0-0 libgtk-3-0 libnss3 libx11-xcb1 libxcb-dri3-0 libgbm1 && \
    curl -sSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/124.0.6367.91/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/bin && \
    chmod +x /usr/bin/chromedriver && \
    rm /tmp/chromedriver.zip

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
