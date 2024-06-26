###code monk backend assignment
Short description or introduction of the project.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Examples](#examples)
- [Deployment](#deployment)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Briefly describe what the project is about and its purpose.

## Getting Started

Instructions on setting up the project locally.

### Prerequisites

List any software or tools that need to be installed.

### Installation

Step-by-step instructions to get the development environment set up.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rajashekar361/assignment-codemonk.git
   cd repository
2.**Build Docker containers:**
   ```bash

docker-compose build
docker-compose up -d db
```

3.** Apply migrations:**
   ```bash

python manage.py makemigrations authentication
python manage.py migrate authentication
python manage.py makemigrations paragraphs
python manage.py migrate paragraphs
```
**RUnserver **
```bash
python manage.py runserver
```

# Example of API Endpoints section in code format
# List all available API endpoints with a brief description.

# User Registration
- Endpoint: `/Signup/`
- Method: `POST`
- Payload Example:
  ```json
  {
    "email": "john@website.com",
    "name": "John Doe",
    "password": "your_password"
  }
  ```
  output
  ```json
  {
  "status": true,
  "status_code": 201,
  "message": "Successfully Registered.",
  "data": {
    "email": "john@website.com",
    "name": "John Doe"
  }
}

### User Login

- **Endpoint:** `/Login/`
- **Method:** `POST`
- **Payload Example:**
  ```json
  {
    "email": "john@website.com",
    "password": "your_password"
  }


output
{
  "success": true,
  "message": "Login successful"
}

### Store Paragraphs

- **Endpoint:** `/paragraphs/store/`
- **Method:** `POST`
- **Payload Example:**
  ```json
  {
    "paragraphs": [
      "Lorem ipsum dolor sit amet........",
      "Consectetur adipiscing elit.........."
    ]
  }
{
  "message": "Paragraphs and words stored successfully"
}
### Search Paragraphs

- **Endpoint:** `/paragraphs/search`
- **Parameter:** `word` (word to search)
- **Response Example:**
  ```json
  [
    { "paragraph_id": 1 },
    { "paragraph_id": 2 }
  ]
