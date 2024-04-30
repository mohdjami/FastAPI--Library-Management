# Library Management App

This is a library management app that provides routes for managing students. It allows you to perform operations such as getting a list of students, creating a new student, getting a student by ID, updating a student's information, and deleting a student.

## Routes

### Get List of Students

Endpoint: `/students`

Method: GET

Description: Retrieves a list of all students.

### Create Student

Endpoint: `/students`

Method: POST

Description: Creates a new student.

### Get Student by ID

Endpoint: `/students/{id}`

Method: GET

Description: Retrieves a specific student by their ID.

### Patch Student

Endpoint: `/students/{id}`

Method: PUT

Description: Updates information for a specific student.

### Delete Student

Endpoint: `/students/{id}`

Method: DELETE

Description: Deletes a specific student.

## Advanced Functionalities

This library management app also includes the following advanced functionalities:

### Redis for Rate Limiting

We have implemented Redis for rate limiting to ensure that the API endpoints are not abused. This helps to prevent excessive requests and maintain the performance and stability of the application.

### Docker

The app is containerized using Docker, which allows for easy deployment and scalability. Docker provides a consistent environment for running the application, making it easier to manage dependencies and ensure consistent behavior across different environments.

## Getting Started

To get started with the library management app, follow these steps:

1. Clone the repository.
2. Setup the environment Variables as given in env.example.
3. Configure the Redis connection for rate limiting.
4. Run the docker compose up command.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
