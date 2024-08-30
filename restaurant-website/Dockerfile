# Specify the base image
# FROM node:alpine

# Set the working directory
# WORKDIR /app

# Copy the package.json and package-lock.json files
# COPY package*.json ./

# Install the dependencies
# RUN npm install

# Copy the app files
# COPY . .

# Build the app
# RUN npm run build

# Expose the port
# EXPOSE 3000

# Run the app
# CMD ["npm", "start"]

# Use an official Node.js runtime as a parent image
FROM node:20.14.0

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
