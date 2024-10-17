# React Calculator

This project is a simple calculator built with React, containerized using Docker. 
The application allows users to perform Reverse Polish Notation (RPN) calculations and can be run locally or inside a Docker container.

### Features
-Simple React-based calculator
-Supports basic arithmetic operations (+, -, *, /) with Reverse Polish Notation
-Responsive and interactive UI
-Dockerized for easy deployment and portability

### Prerequisites
Before you start, make sure you have the following installed:

- Docker
- Node.js (if running locally)

### Project Structure

├── public/               # Public files for the app
├── src/                  # Source files (React components, styles, etc.)
├── Dockerfile            # Docker instructions to build the image
├── .dockerignore         # Exclude files from the Docker build context
├── package.json          # Project dependencies and scripts
└── README.md             # Project documentation

### Local Development

1. Clone the repository:


2. Install dependencies:
npm install


3. Run the app locally:
npm start
The application will be available at http://localhost:3000.

### Dockerized Deployment
1. Build the Docker image:
To containerize the application, you need to build the Docker image using the provided Dockerfile:

docker build -t rpn-calculator-front .

2. Run the Docker container:
Once the image is built, run the container exposing port 3000:

docker run -p 3000:80 rpn-calculator-front
Your app will be accessible at http://localhost:3000.


## Using the Calculator

To use the calculator, follow these steps:

1. Enter the expression in Reverse Polish Notation (RPN):
- In RPN, operators come after the operands.
Example: To calculate 1 + 2, input 1 2 + .
- Make sure to separate each number and operator with a space.

2. Button Actions:
- Use the calculator buttons to enter the numbers and operators.
- Press the space button between numbers and operators.
- Press = to compute the result.
- Press C to clear the input.


## Project Scripts
npm start: Runs the app in development mode.

npm run build: Builds the app for production.

pytest test_main.py: Runs the tests.

npm run eject: Ejects the project from the default create-react-app setup.
