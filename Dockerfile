FROM debian:bullseye

ENV container=docker
ENV PYTHONPATH=/usr/lib/python3/dist-packages

# Install Python and build tools
RUN apt update && apt install -y \
    python3 python3-pip python3-setuptools dh-python debhelper fakeroot build-essential \
 && apt clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt/python-daemon

# Copy source
COPY . .
RUN chmod +x debian/postinst

# Build the .deb package
RUN dpkg-buildpackage -us -uc -b

# Move up and install the built .deb package
WORKDIR /opt
RUN dpkg -i python-daemon_*.deb || apt -f install -y

# Set environment variable for Python path to ensure it can find the module
ENV PYTHONPATH=/usr/lib/python3/dist-packages
WORKDIR /opt/python-daemon
RUN pwd
# Run the installed daemon package
CMD ["python3", "-m", "mydaemon.main"]
