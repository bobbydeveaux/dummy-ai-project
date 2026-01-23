# dummy-ai-project - Third Documentation

A demonstration project showcasing AI-powered development workflows and automated task management using Kubernetes Custom Resource Definitions (CRDs).

## Overview

This project serves as a reference implementation for AI-assisted software development, featuring automated sprint management, task assignment, and pull request workflows orchestrated through Kubernetes CRDs.

## Architecture

The project implements a multi-agent system where specialized AI agents handle different aspects of software development through a Kubernetes-native workflow.

## Key Features

- **AI-Powered Development**: Automated code generation and implementation by AI agents
- **CRD-Based Task Management**: Kubernetes-native task tracking and assignment
- **Automated Workflows**: Seamless integration between issue creation, implementation, and review
- **Sprint-Based Organization**: Structured development cycles with automated task distribution

## Technologies

- Kubernetes Custom Resource Definitions (CRDs)
- GitHub API integration
- AI agent orchestration
- Git workflow automation

## Installation

### Prerequisites

Before installing and using this project, ensure you have the following tools installed:

1. **Kubernetes Cluster** (v1.19 or higher)
   - Local: [Minikube](https://minikube.sigs.k8s.io/), [kind](https://kind.sigs.k8s.io/), or [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - Cloud: GKE, EKS, AKS, or any Kubernetes-compatible cluster

2. **kubectl** - Kubernetes command-line tool
   ```bash
   # macOS
   brew install kubectl

   # Linux
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

   # Windows (using Chocolatey)
   choco install kubernetes-cli
   ```

3. **GitHub CLI (gh)** - Required for PR operations
   ```bash
   # macOS
   brew install gh

   # Linux
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt update
   sudo apt install gh

   # Windows (using Chocolatey)
   choco install gh
   ```

4. **Git** - Version control system
   ```bash
   # macOS
   brew install git

   # Linux
   sudo apt-get install git

   # Windows (using Chocolatey)
   choco install git
   ```

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/dummy-ai-project.git
   cd dummy-ai-project
   ```

2. **Set up Kubernetes context**
   ```bash
   # Verify kubectl is configured
   kubectl cluster-info

   # Create namespace for the project
   kubectl create namespace test-project-hovwr
   ```

3. **Install Custom Resource Definitions (CRDs)**
   ```bash
   # Apply CRD definitions (if available in the repository)
   kubectl apply -f crds/
   ```

4. **Configure GitHub CLI**
   ```bash
   # Authenticate with GitHub
   gh auth login

   # Verify authentication
   gh auth status
   ```

5. **Verify installation**
   ```bash
   # Check that CRDs are installed
   kubectl get crds | grep coo.dev

   # List any existing tasks
   kubectl get cootasks -n test-project-hovwr
   ```

### Troubleshooting

- **kubectl command not found**: Ensure kubectl is in your PATH after installation
- **CRD not found**: Verify that your Kubernetes cluster supports custom resources (v1.19+)
- **GitHub authentication failed**: Run `gh auth login` and follow the prompts
- **Namespace already exists**: This is expected if the namespace was created previously

## Getting Started

This project demonstrates automated development workflows. Tasks are managed through Kubernetes CRDs and automatically assigned to AI agents for implementation.

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/dummy-ai-project.git
   cd dummy-ai-project
   ```

2. **View existing tasks**
   ```bash
   kubectl get cootasks -n test-project-hovwr
   ```

3. **Check task status**
   ```bash
   kubectl describe cootask <task-name> -n test-project-hovwr
   ```

### Prerequisites

- Kubernetes cluster with CRD support
- GitHub repository access
- kubectl CLI tool
- gh CLI (GitHub CLI) for PR operations

### Usage

Tasks are created as CooTask CRDs and automatically processed by designated AI agents. Each task follows a structured workflow from assignment through implementation to review.

### Quick Start Example

To see the system in action, here's how a task flows through the system:

```bash
# Create a new task
kubectl apply -f - <<EOF
apiVersion: coo.dev/v1alpha1
kind: CooTask
metadata:
  name: example-task
  namespace: test-project
spec:
  title: "Add new feature"
  assignedAgent: "feature-developer"
  issueNumber: 42
EOF

# Check task status
kubectl get cootask example-task -n test-project

# The assigned agent will automatically:
# 1. Create a feature branch
# 2. Implement the changes
# 3. Create a draft PR with implementation plan
# 4. Mark PR ready for review
# 5. Update task status to PendingReview
```

## Project Structure

This is a demonstration project designed to showcase AI-powered development patterns and automated task management workflows.

## Workflow Example

A typical development workflow in this project:

1. **Task Creation**: A GitHub issue is created with a feature request or bug report
2. **Sprint Planning**: Tasks are organized into sprints using CooTask CRDs
3. **Agent Assignment**: The system assigns an appropriate AI agent (e.g., crd-designer) to the task
4. **Implementation**: The agent analyzes requirements, creates a plan, and implements the solution
5. **Pull Request**: Changes are submitted as a draft PR with an implementation plan
6. **Review**: The PR is marked ready for human review
7. **Merge**: After approval, changes are merged into the main branch

## Agent Roles

Different AI agents handle different types of tasks:

- **crd-designer**: Handles CRD-related tasks and documentation
- **feature-developer**: Implements new features and enhancements
- **bug-fixer**: Addresses bug reports and issues
- **test-writer**: Creates and maintains test suites

## Development Workflow

Tasks follow a structured lifecycle:
- `Assigned` → Agent receives the task
- `InProgress` → Agent is working on implementation
- `PendingReview` → PR created and awaiting review
- `Completed` → Task merged and closed

## Benefits

- **Consistency**: Standardized workflows ensure consistent code quality
- **Efficiency**: Automated task management reduces overhead
- **Transparency**: Full visibility into task status and progress
- **Scalability**: Can handle multiple concurrent tasks across different agents

## Contributing

This project follows an automated development workflow where tasks are assigned to AI agents for implementation and human review.

## Task Management

Tasks in this project are managed through a sophisticated CRD-based system that automates the entire development lifecycle:

### Task Lifecycle
1. **Creation**: Issues are created in GitHub and represented as CooTask CRDs
2. **Assignment**: Tasks are automatically assigned to specialized AI agents based on labels
3. **Planning**: Agents create draft PRs with detailed implementation plans
4. **Implementation**: Agents make code changes and push to the PR
5. **Review**: PRs are marked ready for human review
6. **Completion**: After approval, changes are merged and tasks marked complete

### Task Status Tracking
Tasks can be monitored through Kubernetes:
```bash
kubectl get cootasks -n <namespace>
kubectl describe cootask <task-name> -n <namespace>
```

## License

MIT
