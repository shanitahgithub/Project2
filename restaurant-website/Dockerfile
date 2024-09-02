# Specify the base image with the desired Node.js version
FROM node:20.14.0

# Set the working directory
WORKDIR /restaurant-website

# Copy the package.json and package-lock.json files
COPY package*.json ./

RUN npm install
# Install the dependencies with verbose output for debugging
RUN npm install --verbose

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
