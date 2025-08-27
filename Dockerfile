# Base n8n image
FROM n8nio/n8n:latest

# Create a directory for custom workflows (optional)
WORKDIR /home/node/.n8n

# Copy exported workflows into the container
# (Keep them in ./workflows in your repo)
COPY ./workflows /home/node/.n8n/workflows

# Ensure permissions for n8n user
RUN chown -R node:node /home/node/.n8n

USER node

# Start n8n
CMD ["n8n", "start"]
