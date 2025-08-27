# Base n8n image
FROM n8nio/n8n:latest

# Switch to root for permission operations
USER root

# Create directory and set permissions
RUN mkdir -p /home/node/.n8n

# Copy workflows (optional: pre-load workflows)
COPY ./workflows /home/node/.n8n/workflows

# Fix permissions for node user
RUN chown -R node:node /home/node/.n8n

# Switch back to node user
USER node

# Set working directory
WORKDIR /home/node/.n8n

# Start n8n
CMD ["n8n", "start"]
