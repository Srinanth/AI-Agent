FROM n8nio/n8n:latest

COPY ./workflows /home/node/.n8n/workflows

# Set permissions
USER root
RUN chown -R node:node /home/node/.n8n
USER node

WORKDIR /home/node/.n8n
