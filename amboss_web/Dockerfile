FROM python:3.10-slim

# Set environment variable
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 fonts-liberation \
    libxss1 libappindicator3-1 libasound2 \
    libatk-bridge2.0-0 libgtk-3-0 libnss3 \
    libx11-xcb1 libxcb-dri3-0 libgbm1 && \
    rm -rf /var/lib/apt/lists/*

# Add Google's GPG key
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /etc/apt/keyrings/google.gpg

# Add Chrome repo
RUN echo "deb [signed-by=/etc/apt/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome (fixed version)
RUN apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver (matching version)
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/124.0.6367.91/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start Flask app
CMD ["python", "app.py"]
