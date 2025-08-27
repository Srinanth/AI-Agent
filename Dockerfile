# Base n8n image
FROM n8nio/n8n:latest

# Switch to root for permission operations
USER root

# Create directory for n8n data
RUN mkdir -p /home/node/.n8n

# Copy your full n8n_data (credentials + workflows + other files)
COPY ./n8n_data /home/node/.n8n

# Fix permissions for node user
RUN chown -R node:node /home/node/.n8n

# Switch back to node user
USER node

# Set working directory
WORKDIR /home/node/.n8n

# Start n8n
CMD ["n8n", "start"]
