#!/bin/bash

# Remove existing packages
sudo dpkg --remove --force-remove-reinstreq mongo-tools
sudo dpkg --remove --force-remove-reinstreq mongodb-server-core
sudo apt-get --fix-broken install

# Add MongoDB repository
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
sudo apt-get install gnupg
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

# Update and install MongoDB
sudo apt-get update
sudo apt-get install -y mongodb-org

# Download the file
curl -L -o tempfile "https://raw.githubusercontent.com/mongodb/mongo/master/debian/init.d"

# Append the contents of the downloaded file to /etc/init.d/mongod
sudo cat tempfile >> /etc/init.d/mongod

# Remove the temporary file
rm tempfile

# Set permissions and start MongoDB
sudo chmod +x /etc/init.d/mongod
sudo service mongod start

