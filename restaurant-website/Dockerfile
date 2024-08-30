# # Specify the base image
# FROM node:alpine

# # Set the working directory
# WORKDIR /app

# # Copy the package.json and package-lock.json files
# COPY package*.json ./

# # Install the dependencies
# RUN npm install

# # Copy the app files
# COPY . .

# # Build the app
# RUN npm run build

# # Expose the port
# EXPOSE 3000

# # Run the app
# CMD ["npm", "start"]


# Specify the base image with the desired Node.js version
FROM node:20.14.0-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the application files
COPY . .

# Build the app
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Set the environment to production (optional)
ENV NODE_ENV=production

# Run the app
CMD ["npm", "start"]

