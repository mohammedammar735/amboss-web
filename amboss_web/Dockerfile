FROM python:3.10-slim

# Set environment variable to prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for Chrome, utilities, Xvfb, and common build tools
# Added: build-essential, pkg-config, zlib1g-dev, libffi-dev, libssl-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget unzip curl gnupg2 fonts-liberation \
    libxss1 libappindicator3-1 libasound2 \
    libatk-bridge2.0-0 libgtk-3-0 libnss3 \
    libx11-xcb1 libxcb-dri3-0 libgbm1 \
    xvfb \
    build-essential pkg-config \
    zlib1g-dev libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Add Google's GPG key and Chrome repo
# Using a more robust way to add the key
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /etc/apt/trusted.gpg.d/google.gpg && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update

# Install Google Chrome Stable
RUN apt-get install -y google-chrome-stable

# Install ChromeDriver from a specific chrome-for-testing URL
# WARNING: Hardcoding the ChromeDriver version like this can lead to incompatibility
# when Google Chrome Stable updates to a newer version.
# This step is kept from your previous attempt as it seemed to bypass the dynamic fetch issue.
RUN CHROMEDRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/136.0.7103.92/linux64/chromedriver-linux64.zip" && \
    echo "Downloading ChromeDriver from: ${CHROMEDRIVER_URL}" && \
    mkdir -p /tmp/chromedriver && \
    wget -O /tmp/chromedriver.zip ${CHROMEDRIVER_URL} && \
    unzip /tmp/chromedriver.zip -d /tmp/chromedriver && \
    # Note: The extracted path might vary slightly depending on the zip content.
    # Check the exact path after unzip if this mv command fails.
    # Based on the URL, 'chromedriver-linux64/chromedriver' seems likely.
    mv /tmp/chromedriver/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver*

# Set the working directory inside the container
WORKDIR /app

# Copy the application code from the 'amboss_web' subdirectory to the working directory
# This assumes your Dockerfile is at amboss_web/Dockerfile and the build context
# is the root of the repository containing the amboss_web folder.
COPY amboss_web/requirements.txt /app/requirements.txt
COPY amboss_web/. /app/

# Install Python dependencies
# This step should now have the necessary build tools available and requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Start the app
CMD ["python", "app.py"]
