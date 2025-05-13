FROM python:3.10-slim

# Set environment variable to prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for Chrome, utilities, and Xvfb
# xvfb is needed for running headless Chrome in environments without a graphical display
# --no-install-recommends is used to keep the image size smaller
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget unzip curl gnupg2 fonts-liberation \
    libxss1 libappindicator3-1 libasound2 \
    libatk-bridge2.0-0 libgtk-3-0 libnss3 \
    libx11-xcb1 libxcb-dri3-0 libgbm1 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Add Google's GPG key and Chrome repo for installing Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update

# Install Google Chrome Stable
RUN apt-get install -y google-chrome-stable

# Install ChromeDriver from a specific chrome-for-testing URL
# WARNING: Hardcoding the ChromeDriver version like this can lead to incompatibility
# when Google Chrome Stable updates to a newer version.
RUN CHROMEDRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/136.0.7103.92/linux64/chromedriver-linux64.zip" && \
    echo "Downloading ChromeDriver from: ${CHROMEDRIVER_URL}" && \
    wget -O /tmp/chromedriver.zip ${CHROMEDRIVER_URL} && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Set the working directory inside the container
WORKDIR /app

# Copy the application code from your local directory to the working directory in the container
COPY . /app

# Install the Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your application when the container starts
# Ensure your Python application is configured to use headless Chrome when running in this environment
CMD ["python", "app.py"]
