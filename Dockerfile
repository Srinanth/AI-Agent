# Use n8n base image
FROM n8nio/n8n:latest

# Copy workflows (optional)
COPY ./workflows /home/node/.n8n/workflows

# Set permissions
USER root
RUN chown -R node:node /home/node/.n8n
USER node

# Set working directory
WORKDIR /home/node/.n8n

# Don't override the entrypoint; n8n image already defines it
# Just let Render pass the command if needed
