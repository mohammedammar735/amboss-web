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

# Install ChromeDriver dynamically based on the installed Chrome version
# This is crucial because the ChromeDriver version must match the Chrome version
RUN CHROME_VERSION=$(google-chrome --product-version) && \
    echo "Detected Chrome version: ${CHROME_VERSION}" && \
    # Extract the major version from the Chrome version string
    CHROME_MAJOR_VERSION=$(echo ${CHROME_VERSION} | cut -d. -f1) && \
    echo "Detected Chrome major version: ${CHROME_MAJOR_VERSION}" && \
    # Get the corresponding ChromeDriver version from the LATEST_RELEASE file hosted by Google
    # We use a fallback echo with an error message and check if the version was fetched successfully
    CHROMEDRIVER_VERSION=$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION} || echo "Error fetching chromedriver version for Chrome ${CHROME_MAJOR_VERSION}") && \
    if [ "$CHROMEDRIVER_VERSION" = "Error fetching chromedriver version for Chrome ${CHROME_MAJOR_VERSION}" ]; then \
        echo "Could not find a matching chromedriver version from Google Storage. This may happen if Chrome just updated and the corresponding chromedriver is not yet available or if there's a network issue." && exit 1; \
    fi && \
    echo "Corresponding ChromeDriver version: ${CHROMEDRIVER_VERSION}" && \
    # Download the matching ChromeDriver, unzip it to /usr/local/bin/, make it executable, and clean up
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
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
