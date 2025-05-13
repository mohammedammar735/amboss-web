FROM python:3.10-slim

# Set environment variable to prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for Chrome, utilities, and Xvfb
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget unzip curl gnupg2 fonts-liberation \
    libxss1 libappindicator3-1 libasound2 \
    libatk-bridge2.0-0 libgtk-3-0 libnss3 \
    libx11-xcb1 libxcb-dri3-0 libgbm1 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Add Google's GPG key and Chrome repo
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update

# Install Google Chrome Stable
RUN apt-get install -y google-chrome-stable

# ✅ Fixed: Install ChromeDriver properly from chrome-for-testing
RUN CHROMEDRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/136.0.7103.92/linux64/chromedriver-linux64.zip" && \
    echo "Downloading ChromeDriver from: ${CHROMEDRIVER_URL}" && \
    mkdir -p /tmp/chromedriver && \
    wget -O /tmp/chromedriver.zip ${CHROMEDRIVER_URL} && \
    unzip /tmp/chromedriver.zip -d /tmp/chromedriver && \
    mv /tmp/chromedriver/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver*

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the app
CMD ["python", "app.py"]
