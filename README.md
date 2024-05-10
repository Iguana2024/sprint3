# IGD Application

## Table of contents
* [Introduction](#introduction)
* [Overview](#overview)
* [Technologies Used](#technologies-used)
* [Requirements](#requirements)
* [Architecture Diagram](#architecture-diagram)
* [Usage](#usage)
* [Setup Instructions](#setup-instructions)
  * [Server Environment](#server-environment)
  * [Local Environment](#local-environment)
* [Understanding Codebase](#understanding-codebase)
  * [For Server Environment](#for-server-environment)
    * [home.py](#homepy)
    * [Docker](#docker)
    * [Nginx](#nginx)
    * [Templates](#templates)
  * [For Local Environment](#for-local-environment)
    * [Folder Structure (`/test/`)](#folder-structure-test)
* [Troubleshooting Guide](#troubleshooting-guide)
* [Contributing](#contributing)
* [Credits](#credits)

## Introduction
Welcome to the IGD Application! The purpose of the IGD Application is to offer users a user-friendly solution for making decisions about data sharing. By presenting clear options to grant or reject permission for data storage, the application allows users to maintain control over their personal information.

### Target Audience
- **Developers** are interested in exploring the codebase, contributing to the project, or integrating the application with other systems.
- **End-Users** who want to understand how their data is managed and stored, and who wish to control over their data sharing preferences.
- **Website and Web Platform Owners** who wish to integrate data sharing options seamlessly into their existing systems, enhancing user privacy and compliance with data protection regulations.

### Key Features
- **Clear options** for granting or rejecting permission for data storage.
- **Transparent handling** of user decisions, ensuring GDPR compliance and accountability.
- **Secure storage** and retrieval of user data using MongoDB and Redis.
- **Easy-to-use interface** for managing data sharing preferences.

This Documentation will guide you through the key aspects of the project.

## Overview
The IGD Application allows visitors to make informed decisions about sharing their data. Users are presented with two clear options: "Grant" or "Reject".

- **Grant Permission:**
  - Choosing "Grant" allows users to willingly share their data. Upon selection, the application securely stores the visitor's IP address, ID, date, and time in the database. This information is then displayed on subsequent visits, ensuring transparency, accountability, and compliance with GDPR regulations.

- **Reject Permission:**
  - Opting for "Reject" prioritizes user privacy. The application hashes the visitor's IP address and stores hash in the database. On future visits, if the hashed IP matches, a message indicating rejection is displayed. This approach respects users' privacy rights while providing clear feedback on their previous decisions.

- **Erase Data:**
  - Additionally, the application offers users the ability to erase their data, providing a seamless way to revoke granted permissions or rejections. This feature enables users to reset their preferences, returning to the main page with the two initial options.

## Technologies Used
- **Python Flask:** A lightweight web application framework used for backend development, facilitating rapid development and deployment.
- **MongoDB:** A NoSQL database offering flexibility and scalability for storing user data.
- **Redis:** An in-memory data structure store used as a caching layer to improve application performance.
- **HTML and JavaScript:** Standard markup and scripting languages used for frontend development, providing interactivity and dynamic behavior.
- **Docker:** A containerization platform enabling consistent deployment across different environments.
- **Nginx:** A high-performance web server and reverse proxy server used to handling HTTP requests and serving static content.
- **AWS EC2:** Providing scalable computing capacity in the cloud for hosting the deployed application.
- **CERT-Bot:** Automating the process of obtaining SSL certificates, ensuring secure communication between the web server and clients.
- **Git Actions:** Automating tasks and workflows in the software development process, enhancing code quality and deployment efficiency.

## Requirements
IGD Application requires Docker Engine`s latest version

## Architecture Diagram
![image](https://github.com/Iguana2024/sprint3/assets/168120052/d5aad07d-f199-4c28-9cb5-0fdf067e938d)

## Usage
- Visit the main page.
- Choose "Grant" or "Reject" to grant or reject permission to store your data.
- If "Grant" is selected, your details will be stored in the database and displayed on subsequent visits.
- If "Reject" is selected, your IP address will be hashed and stored in the database. On subsequent visits, if the hashed IP matches, a rejection message will be displayed.
- Use the "Erase Data" link to remove granted permission or rejection and return to the main page. <br>

![image](https://github.com/Iguana2024/sprint3/assets/168120052/4683639e-d566-407f-93f2-616e99aa014a)

## Setup Instructions
### Server Environment
1. Clone the repository:
```
git clone https://github.com/Iguana2024/sprint3.git
```

2. Сreate directory 'certs' and put your ssl certificates there
```shell
# Сreate directory 'certs':
mkdir certs/
# put your ssl certificates there:
cp your/certificates/path certs/
```

3. Install Docker on your machine if not already installed.
```shell
# Check if Docker is installed:
docker --version
# Check if the Docker service is running:
sudo systemctl status docker
```
[Get the official guidelines](https://docs.docker.com/engine/install/) for installing Docker.

4. Build and run the Docker container:
```
docker-compose up --build
```

5. Access the application in a web browser at `http://localhost`

### Local Environment
1. Clone the repository:
```
git clone https://github.com/Iguana2024/sprint3.git
```

2. Change the current working directory via the terminal
```shell
cd sprint3/test/
```

3. Install Docker on your machine if not already installed.
```shell
# Check if Docker is installed:
docker --version
# Check if the Docker service is running:
sudo systemctl status docker
```
[Get the official guidelines](https://docs.docker.com/engine/install/) for installing Docker.

4. Run application:
```
docker-compose up
```

5. Access the application in a web browser at `http://localhost:5000`

## Understanding Codebase
### For Server Environment
#### home.py
- The main Flask application code.
- It includes route definitions for handling different HTTP requests.
- Database interactions, such as storing user decisions and retrieving stored data, are implemented here.
- Request handling logic, including decision processing based on user input, is managed within this file.

#### Docker
- **Dockerfile** defines the configuration for building the Docker image.
- **docker-compose.yml** specifies the Docker services and configurations.
- **requirements.txt** lists the necessary dependencies required for running the application.

#### Nginx
- **nginx.conf** configures routing of HTTP requests.
- **example.conf** sets up SSL/TLS encryption and redirects HTTP traffic to HTTPS.

#### Templates
- **home.html** serves as the main page of the application, where users are presented with the choice to grant or reject permission to store data.
- **granted_permission.html** is displayed when a user grants permission to store their data, providing acknowledgment of their choice.
- **rejected_permission.html** is displayed when a user rejects permission to store their data, confirming their decision and privacy rights.

### For Local Environment
#### Folder Structure (/test/)
  - **home.py** is the file of the main application code, tailored for local testing and development purposes.
  - **Dockerfile** defines the Docker image configuration for local development environments.
  - **docker-compose.yml**: specifies Docker services and configurations for local deployment.
  - **requirements.txt**: lists necessary dependencies for running the application locally.
  - **Templates** includes HTML templates required for rendering application pages locally.

## Troubleshooting Guide
- **application not accessible:**
  - Docker container not running
  - port conflict

- **database connection issues:**
  - incorrect database configuration
  - network connectivity

- **SSL/TLS certificate issues:**
  - invalid or expired certificate
  - misconfigured nginx

- **data processing errors:**
  - incorrect data handling

## Contributing
1. Fork the repository.
2. Create a new branch: 
```
git checkout -b new-feature
```
3. Make your changes.
4. Push your branch: 
```
git push origin new-feature
```
5. Create a pull request.

## Credits
We would like to extend our appreciation to the following team members for their contributions to the implementation of this solution:
- **Yurii Belichenko**
- **Anton Antonenko**
- **Aliona Sahaidak**
- **Anna Olenych**
- **Oleksii Taranyk** 
