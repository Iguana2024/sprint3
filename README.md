# IGD Data Storage Application

## Table of contents
* [Overview](#overview)
* [Technologies Used](#technologies-used)
* [Requirements](#requirements)
* [Architecture Diagram](#architecture-diagram)
* [Usage](#usage)
* [Setup Instructions](#setup-instructions)
  * [Server Running](#server-running)
  * [Locally Running](#locally-running)
* [Understanding Codebase](#understanding-codebase)
  * [home.py](#homepy)
  * [Docker](#docker)
  * [Nginx](#nginx)
  * [Templates](#templates)
  * [Running Locally](#running-locally)
* [Troubleshooting Guide](#troubleshooting-guide)
* [Contributing](#contributing)
* [Credits](#credits)

## Overview
This simple web application allows visitors to make informed decisions about sharing their data. Users are presented with two clear options: "Grant" or "Reject".

- **Grant Permission:**
  - Choosing "Grant" allows users to willingly share their data. Upon selection, the application securely stores the visitor's IP address, ID, date, and time in the database. This information is then displayed on subsequent visits, ensuring transparency, accountability, and compliance with GDPR regulations.

- **Reject Permission:**
  - Opting for "Reject" prioritizes user privacy. The application hashes the visitor's IP address and stores hash in the database. On future visits, if the hashed IP matches, a message indicating rejection is displayed. This approach respects users' privacy rights while providing clear feedback on their previous decisions.

- **Erase Data:**
  - Additionally, the application offers users the ability to erase their data, providing a seamless way to revoke granted permissions or rejections. This feature enables users to reset their preferences, returning to the main page with the two initial options.

## Technologies Used
- **Python Flask:** A lightweight web application framework used for backend development. Flask allows for the rapid development and deployment of web applications.
- **MongoDB:** A NoSQL database used for storing user data. MongoDB offers flexibility and scalability, making it suitable for applications with varying data structures.
- **Redis:** An open-source, in-memory data structure store used as a caching layer. Redis helps improve application performance by storing frequently accessed data in memory.
- **HTML and JavaScript:** Standard markup and scripting languages used for frontend development. HTML provides the structure of web pages, while JavaScript adds interactivity and dynamic behavior.
- **Docker:** A containerization platform used to package applications and their dependencies into containers. Docker enables consistent deployment across different environments, improving portability and scalability.
- **Nginx:** A high-performance web server and reverse proxy server used to handle HTTP requests and serve static content. Nginx is known for its efficiency and scalability, making it ideal for handling high-traffic loads. It also provides features like load balancing, SSL termination, and caching to improve performance and security.
- **AWS EC2:** Amazon Web Services (AWS) Elastic Compute Cloud (EC2) provides scalable computing capacity in the cloud. AWS EC2 instances host the deployed application, ensuring scalability, reliability, and cost-effectiveness. They provide the computational power needed to run the application and can be easily scaled up or down based on demand.
- **CERT-Bot:** An open-source tool used for automating the process of obtaining SSL certificates from certificate authorities (CAs) like Let's Encrypt. It simplifies the management of SSL/TLS certificates, ensuring secure communication between the web server and clients.
- **Git Actions:** A feature of Git that allows for automating tasks and workflows in the software development process. Git Actions helps improve code quality and deployment efficiency.

## Requirements
IGD Data Storage requires Docker Engine`s latest version

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
### Server Running
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
[Get](https://docs.docker.com/engine/install/) the official guidelines for installing Docker.

4. Build and run the Docker container:
```
docker-compose up --build
```

4. Access the application in a web browser at `http://localhost`

### Locally Running
1. Clone the repository:
```
git clone https://github.com/Iguana2024/sprint3.git
```

2. Change the current working directory via the terminal
```shell
cd test/
```

3. Install Docker on your machine if not already installed.
```shell
# Check if Docker is installed:
docker --version
# Check if the Docker service is running:
sudo systemctl status docker
```
[Get](https://docs.docker.com/engine/install/) the official guidelines for installing Docker.

4. Run application:
```
docker-compose up
```

5. Access the application in a web browser at `http://localhost:5000`

## Understanding Codebase
### home.py
- The main Flask application code.
- It includes route definitions for handling different HTTP requests.
- Database interactions, such as storing user decisions and retrieving stored data, are implemented here.
- Request handling logic, including decision processing based on user input, is managed within this file.

### Docker
- **Dockerfile** defines the configuration for building the Docker image.
- **docker-compose.yml** specifies the Docker services and configurations.
- **requirements.txt** lists the necessary dependencies required for running the application.

### Nginx
- **nginx.conf** configures routing of HTTP requests.
- **example.conf** sets up SSL/TLS encryption and redirects HTTP traffic to HTTPS.

### Templates
- **home.html** serves as the main page of the application, where users are presented with the choice to grant or reject permission to store data.
- **granted_permission.html** is displayed when a user grants permission to store their data, providing acknowledgment of their choice.
- **rejected_permission.html** is displayed when a user rejects permission to store their data, confirming their decision and privacy rights.

### Running Locally
- **Folder Structure (`/test/`)**:
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
