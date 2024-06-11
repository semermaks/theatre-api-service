Sure, here is a README file for the given GitHub repository:

---

# Theatre API Service

This repository contains the Theatre API Service, a backend service for managing theatre-related data. The service is built using modern web technologies and is designed to be scalable and easy to deploy.

## Table of Contents

- [Installation](#installation)
- [Run with Docker](#run-with-docker)
- [Getting Access](#getting-access)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Theatre API Service, you need to clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/semermaks/theatre-api-service.git
cd theatre-api-service
```

## Run with Docker

Docker should be installed on your system to run the service using Docker.

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Start the service:

    ```bash
    docker-compose up
    ```

## Getting Access

To interact with the API, you need to create a user and obtain an access token.

1. Create a user via the following endpoint:

    ```
    POST /api/user/register/
    ```

2. Get an access token via the following endpoint:

    ```
    POST /api/user/token/
    ```

## API Endpoints

Here are some of the key API endpoints available in the Theatre API Service:

- **User Registration:**
  - `POST /api/user/register/` - Register a new user.
  
- **User Authentication:**
  - `POST /api/user/token/` - Obtain an access token.

- **Theatre Management:**
  - `GET /api/theatres/` - List all theatres.
  - `POST /api/theatres/` - Create a new theatre.
  - `GET /api/theatres/{id}/` - Retrieve a specific theatre by ID.
  - `PUT /api/theatres/{id}/` - Update a specific theatre by ID.
  - `DELETE /api/theatres/{id}/` - Delete a specific theatre by ID.

- **Show Management:**
  - `GET /api/shows/` - List all shows.
  - `POST /api/shows/` - Create a new show.
  - `GET /api/shows/{id}/` - Retrieve a specific show by ID.
  - `PUT /api/shows/{id}/` - Update a specific show by ID.
  - `DELETE /api/shows/{id}/` - Delete a specific show by ID.

- **Booking Management:**
  - `GET /api/bookings/` - List all bookings.
  - `POST /api/bookings/` - Create a new booking.
  - `GET /api/bookings/{id}/` - Retrieve a specific booking by ID.
  - `PUT /api/bookings/{id}/` - Update a specific booking by ID.
  - `DELETE /api/bookings/{id}/` - Delete a specific booking by ID.

## Contributing

We welcome contributions to the Theatre API Service. If you would like to contribute, please fork the repository and submit a pull request. Make sure to follow the existing code style and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to customize this README file further based on the specific details and requirements of your project.
