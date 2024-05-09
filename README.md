# IGD Data Storage Application

## Table of contents
* [Overview](#overview)
* [Technologies Used](#technologies-used)
* [Requirements](#requirements)
* [How It Works](#howitworks)
* [Setup Instructions](#setupinstructions)
* [Usage](#usage)

## Overview
This simple web application allows visitors to make a decision whether to share their data or not. Users are presented with two clear options: "Grant" or "Reject".

- **Grant Permission:**
  - If a visitor selects "Grant", their IP address, ID, date, and time of the selected option are stored in the database. This information is then displayed on subsequent visits, ensuring transparency and accountability regarding data storage, ensuring GDPR compliance and user accountability.

- **Reject Permission:**
  - Opting for "Reject" hashes the visitor's IP address and stores it in the database. On future visits, if the hashed IP matches, a message indicating rejection is displayed. The application informs the user of their previous rejection decision, upholding user privacy rights.

- **Erase Data:**
  - Additionally, the application offers users the ability to erase their data, providing an easy way to remove granted permissions or rejections and return to the main page with the two initial options.

## Technologies Used
- **Python Flask:** A lightweight web application framework used for backend development. Flask allows for the rapid development and deployment of web applications.
- **MongoDB:** A NoSQL database used for storing user data. MongoDB offers flexibility and scalability, making it suitable for applications with varying data structures.
- **Redis:** An open-source, in-memory data structure store used as a caching layer. Redis helps improve application performance by storing frequently accessed data in memory.
- **HTML and JavaScript:** Standard markup and scripting languages used for frontend development. HTML provides the structure of web pages, while JavaScript adds interactivity and dynamic behavior.
- **Docker:** A containerization platform used to package applications and their dependencies into containers. Docker enables consistent deployment across different environments, improving portability and scalability.
- **Nginx:** A high-performance web server and reverse proxy server used to handle HTTP requests and serve static content. Nginx is known for its efficiency and scalability, making it ideal for handling high-traffic loads. It also provides features like load balancing, SSL termination, and caching to improve performance and security.
- **AWS EC2:** Amazon Web Services (AWS) Elastic Compute Cloud (EC2) provides scalable computing capacity in the cloud. AWS EC2 instances host the deployed application, ensuring scalability, reliability, and cost-effectiveness. They provide the computational power needed to run the application and can be easily scaled up or down based on demand.
- **CERT-Bot:** An open-source tool used for automating the process of obtaining SSL certificates from certificate authorities (CAs) like Let's Encrypt. It simplifies the management of SSL/TLS certificates, ensuring secure communication between the web server and clients.

## Requirements
IGD Data Storage requires Docker Engine latest version

## How It Works
- Summarize Flow
- Design Diagram

## Setup Instructions

1. Clone the repository:
```
git clone https://github.com/Iguana2024/sprint3.git
```

2. Install Docker on your machine if not already installed.
```shell
# Check if Docker is installed:
docker --version
# Check if the Docker service is running:
sudo systemctl status docker
```
[Get](https://docs.docker.com/engine/install/) the official guidelines for installing Docker.

3. Build and run the Docker container:
```
docker-compose up --build
```

4. Access the application in a web browser at `https://localhost:90`

## Usage

## Documentation

## Credits