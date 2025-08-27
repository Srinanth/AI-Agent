# Assignment Agent: AI-Powered Grading Assistant

A full-stack, automated assignment evaluation system built on modern workflow automation. This agent accepts student submissions (PDF, DOCX, PPTX), uses Large Language Models (LLMs) to generate feedback and grades based on configurable rubrics, and emails the results back to students—all without manual intervention.

### 🌐 Live Demo  
[**AssignAgent**](https://assignment-agent.vercel.app/)  

> ⚠ **Note:** This project uses free-tier hosting for both the frontend and backend, so the server may experience cold starts or temporary downtime.  
If the service seems unresponsive:  
- Try again after a few minutes.  
- Or, for the best experience, **run the project locally** using the instructions in this README.  


## 🌟 What This Project Does

This project automates the tedious process of initial assignment review. It's a powerful agent that:

1.  **Accepts Submissions:** Provides a clean React frontend for students to upload their work and select an assignment type.
2.  **Processes Files:** A FastAPI backend reliably extracts text from PDFs, Word documents, and PowerPoint presentations.
3.  **Orchestrates with n8n:** The heart of the system. n8n manages the entire workflow: receiving the submission, constructing the perfect prompt for an LLM (like OpenAI's GPT-4), and handling the AI's response.
4.  **Leverages AI:** Uses advanced LLMs to provide intelligent, context-aware feedback and grading on assignments, from essays to math problems.
5.  **Delivers Results:** Automatically sends a beautifully formatted email to the student with their feedback and grade.
6.  **Scales & Recovers:** Built with Docker for easy deployment and uses Supabase (PostgreSQL) to ensure n8n's state and workflow data are persistent and reliable.

I built this project to deeply understand and implement cutting-edge "agentic" workflow automation using n8n, exploring how to stitch together various cloud services and APIs into a robust, functional system.

## 🛠️ Tech Stack

- **Workflow Automation:** [n8n](https://n8n.io/)
- **Backend API:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend:** [React](https://reactjs.org/) + [Vite](https://vitejs.dev/)
- **Database:** [Supabase](https://supabase.com/) (PostgreSQL)
- **Containerization:** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- **LLM Provider:** Gemini Pro

## 📦 Key Components

- `/frontend` - React application for file uploads. [AI Agent frontend Repository](https://github.com/Srinanth/assignment-agent) 
- `/backend` - FastAPI server for file processing and status updates.
- `docker-compose.yml` - Defines and runs n8n and the backend service.
- `workflows/` - Exported JSON definitions of the core n8n workflows for version control.
- `.env.example` - Template for all required environment variables.

## 🤔 For Beginners: What are n8n and Docker?

### n8n
Think of **n8n** (pronounced "n-eight-n") as a visual programming tool for connecting different apps and services. Instead of writing hundreds of lines of code to make an API call, process data, and send an email, you can create a "workflow" by dragging and dropping nodes (pre-built blocks of functionality) and connecting them. It's a powerful, open-source alternative to tools like Zapier or Make.com, perfect for building complex automation and integration agents like this one.

### Docker
**Docker** is a platform that allows you to package an application with all of its dependencies (like libraries, system tools, and code) into a standardized unit called a **container**. This container can run reliably on any machine that has Docker installed. It solves the classic problem of "but it worked on my machine!" by ensuring the application environment is consistent everywhere, from a developer's laptop to a production server. The `docker-compose.yml` file is a blueprint that tells Docker how to run multiple containers (like our n8n and backend services) together.

### Supabase
**Supabase** is an open-source alternative to Firebase, built on top of powerful enterprise-grade tools. It provides a full **PostgreSQL database**, which is a robust and reliable open-source relational database system. Think of it as a super-powered, organized spreadsheet in the cloud that your applications can talk to. Instead of setting up and managing your own PostgreSQL server, Supabase hosts it for you, handling complexities like security, backups, and scaling. In this project, we use it to ensure n8n's data (like workflows and execution history) is safely stored and persists even if our application containers restart.

## 🚀 Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- A Supabase project (for PostgreSQL)
- API keys for Gemini (and an SMTP service for emails gmail is preferd)

### Local Development

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Srinanth/AI-Agent
    cd assignment-agent
    ```

2.  **Set up Environment Variables:**
    ```bash
    cp .env.example .env
    ```
    Edit the `.env` file with your actual credentials:
    - check out the sample env file in the repository

3.  **Launch the services:**
    ```bash
    docker-compose up -d
    ```
    This will start:
    - **n8n** on `http://localhost:5678`
    - **FastAPI Backend** on `http://localhost:8000`
    - The React frontend (if included in the compose setup) typically on `http://localhost:5173`

4.  **Configure n8n:**
    - Open the n8n UI (`http://localhost:5678`) and log in with the credentials you set in the `.env` file.
    - Import the core workflows from the `workflows/` directory to get started.

5.  **Test the flow:** Upload a sample assignment through the React frontend and watch the automation magic happen!

## 📋 Deployment

This system is designed to be deployed to a cloud host like Render, DigitalOcean, or an Oracle VM.

1.  **Build & Push Images:** The GitHub Actions workflow (`.github/workflows/ci-cd.yml`) automatically builds Docker images and pushes them to a container registry (like Docker Hub or GHCR) when code is pushed to the `main` branch.
2.  **Deploy to Host:** On your cloud host, pull the latest images and start them with `docker-compose.prod.yml`, making sure all production environment variables are set.
3.  **Point to Production DB:** Ensure the deployed n8n instance is configured to use your live Supabase PostgreSQL database by setting the `DB_POSTGRESDB_*` environment variables correctly.

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example |
| :--- | :--- | :--- |
| `SUPABASE_DB_HOST` | Hostname of your Supabase Postgres instance | `db.xyz.supabase.co` |
| `SUPABASE_DB_DATABASE` | Database name | `postgres` |
| `SUPABASE_DB_USER` | Database user | `postgres` |
| `SUPABASE_DB_PASSWORD`| Database password | `your-super-secret-password` |
| `Gemini_API_KEY` | Your Gemini API key | `sk-...` |
| `N8N_ENCRYPTION_KEY` | Key to encrypt credentials in DB | `random-characters-32-chars` |
| `SMTP_*` | Credentials for your email service provider | - |

### Adding New Assignment Types

1.  In n8n, duplicate and modify an existing workflow.
2.  Update the prompt template in the **HTTP Request** node to instruct the LLM on the new rubric.
3.  Export the new workflow JSON to the `workflows/` directory.
4.  Update the FastAPI backend or frontend to include the new type as an option.

## 🚢 CI/CD

This project uses GitHub Actions for Continuous Integration and Deployment (CI/CD). On every push to the `main` branch, it automatically:

- Builds the Docker images for the backend and frontend.
- Runs basic tests (if defined).
- Pushes the successfully built images to a container registry, ready for deployment.

## 🛡️ Security & Backups

- **Secrets:** All secrets are managed via environment variables and are never committed to the repository.
- **n8n Auth:** Basic authentication is enforced for the n8n UI.
- **Database:** Supabase provides a managed, secure PostgreSQL instance.
- **Backups:**
  - **Workflows:** The exported JSON files in `workflows/` serve as code-based backups.
  - **Database:** Supabase offers automated daily backups. For extra safety, consider a custom script to export n8n data periodically.

## 📄 License

This project is licensed under the MIT License.