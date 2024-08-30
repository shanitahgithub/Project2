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

# Specify the base image
FROM node:alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json /app/

# Clean npm cache and install dependencies
RUN npm cache clean --force
RUN npm config set registry https://registry.npmjs.org/
RUN npm install --verbose

# Copy the app files
COPY . /app/

# Build the app
RUN npm run build

# Expose the port
EXPOSE 3000

# Run the app
CMD ["npm", "start"]