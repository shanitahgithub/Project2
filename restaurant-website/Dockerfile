# Specify the base image with the desired Node.js version
FROM node:20.14.0

# Set the working directory inside the container
WORKDIR /restaurant-website

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install the dependencies with verbose output for debugging
RUN npm install --verbose

# Copy the rest of the application files
COPY . .

# Build the app (only necessary for production or if you have a build step)
RUN npm run build

# Expose the port the app runs on
EXPOSE 5000

# Set the environment to production (optional)
ENV NODE_ENV=production

# Run the app
CMD ["npm", "start"]
