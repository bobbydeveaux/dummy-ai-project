# dummy-ai-project - Third Documentation

A demonstration project showcasing AI-powered development workflows and automated task management using Kubernetes Custom Resource Definitions (CRDs).

## Installation

This section provides step-by-step instructions to install and configure the dummy-ai-project on your system.

### System Requirements

- **Kubernetes**: Version 1.19 or higher
- **kubectl**: Kubernetes command-line tool
- **GitHub CLI (gh)**: For GitHub API operations and PR management
- **Git**: Version 2.0 or higher
- **Operating System**: Linux, macOS, or Windows with WSL2

### Prerequisites

Before installing, ensure you have:

1. **A running Kubernetes cluster** with CRD support (minikube, kind, or cloud provider)
2. **kubectl configured** with access to your cluster
3. **GitHub repository access** with appropriate permissions
4. **GitHub CLI authenticated** with your GitHub account

### Installation Steps

1. **Verify Kubernetes cluster access**
   ```bash
   kubectl cluster-info
   kubectl version --client
   ```

2. **Install GitHub CLI** (if not already installed)

   On macOS:
   ```bash
   brew install gh
   ```

   On Linux:
   ```bash
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt update
   sudo apt install gh
   ```

   On Windows:
   ```bash
   winget install --id GitHub.cli
   ```

3. **Authenticate GitHub CLI**
   ```bash
   gh auth login
   ```

4. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/dummy-ai-project.git
   cd dummy-ai-project
   ```

5. **Install Custom Resource Definitions**
   ```bash
   # Apply CRD definitions to your cluster
   kubectl apply -f config/crds/
   ```

6. **Create the project namespace**
   ```bash
   kubectl create namespace test-project-hovwr
   ```

7. **Verify installation**
   ```bash
   # Check that CRDs are installed
   kubectl get crds | grep coo.dev

   # Verify namespace exists
   kubectl get namespace test-project-hovwr
   ```

### Post-Installation Verification

After installation, verify that everything is working correctly:

```bash
# List all CooTask resources
kubectl get cootasks -n test-project-hovwr

# Check CRD details
kubectl describe crd cootasks.coo.dev

# Test creating a sample task
kubectl apply -f - <<EOF
apiVersion: coo.dev/v1alpha1
kind: CooTask
metadata:
  name: test-task
  namespace: test-project-hovwr
spec:
  title: "Test installation"
  assignedAgent: "test-agent"
  issueNumber: 1
EOF

# Verify the task was created
kubectl get cootask test-task -n test-project-hovwr

# Clean up test task
kubectl delete cootask test-task -n test-project-hovwr
```

### Troubleshooting

**Issue: CRD not found**
- Ensure your Kubernetes version supports CRDs (v1.19+)
- Check if CRDs were applied: `kubectl get crds`

**Issue: Permission denied**
- Verify your kubectl context has admin privileges
- Check RBAC permissions: `kubectl auth can-i create crd`

**Issue: GitHub CLI authentication failed**
- Run `gh auth login` again and follow the prompts
- Ensure you have appropriate repository permissions

### Uninstall

To remove the project from your cluster:

```bash
# Delete all CooTask resources
kubectl delete cootasks --all -n test-project-hovwr

# Delete the namespace
kubectl delete namespace test-project-hovwr

# Remove CRDs (optional, use with caution)
kubectl delete crd cootasks.coo.dev
```

## Overview

This project serves as a reference implementation for AI-assisted software development, featuring automated sprint management, task assignment, and pull request workflows orchestrated through Kubernetes CRDs.

## Configuration

The system can be configured through environment variables and Kubernetes settings to customize the behavior of the AI-powered development workflow.

### Environment Variables

- **GITHUB_TOKEN**: GitHub API token for repository access and PR operations
  - Required for: Creating PRs, updating issues, managing labels
  - Scopes needed: `repo`, `workflow`

- **KUBERNETES_NAMESPACE**: Namespace for CooTask CRDs
  - Default: `test-project-hovwr`
  - Used for task isolation and organization

- **DEFAULT_BRANCH**: Main branch name for pull requests
  - Default: `main`
  - Target branch for all PRs

### Kubernetes Configuration

The system uses Custom Resource Definitions (CRDs) for task management. Configure your cluster:

```yaml
apiVersion: coo.dev/v1alpha1
kind: CooTask
metadata:
  namespace: test-project-hovwr  # Configure your namespace
spec:
  assignedAgent: "crd-designer"  # Agent assignment
  issueNumber: 28                # GitHub issue number
```

### Agent Configuration

Different AI agents can be configured for specific task types:

- **crd-designer**: CRD-related tasks and documentation updates
- **feature-developer**: New feature implementation
- **bug-fixer**: Bug fixes and issue resolution
- **test-writer**: Test creation and maintenance

Configure agent assignment through task labels in GitHub or directly in CooTask specs.

### GitHub Integration Settings

- **Repository**: Configure in `.git/config`
- **PR Settings**: Draft PRs are created by default, then marked ready after implementation
- **Review Flow**: PRs require human review before merging

## Architecture

The project implements a multi-agent system where specialized AI agents handle different aspects of software development through a Kubernetes-native workflow.

### System Components

1. **CooTask Custom Resources**: Kubernetes CRDs that represent development tasks with lifecycle management
2. **AI Agent Orchestration**: Intelligent agents assigned to specific task types (crd-designer, api-developer, etc.)
3. **GitHub Integration**: Automated PR creation, issue tracking, and status synchronization
4. **Workflow Engine**: Coordinates the flow from task creation through implementation to review

### Development Workflow

The system follows a structured 5-step workflow for each task:

1. **Draft PR Creation**: Agent creates a draft PR with detailed implementation plan
2. **Status Update**: Task status updated to "InProgress" with PR information
3. **Implementation**: Agent implements changes according to the plan
4. **Ready for Review**: PR marked ready and status updated to "PendingReview"
5. **Review & Merge**: Human review, feedback incorporation, and merge

### Agent Roles

Different agents specialize in different types of tasks:

- **crd-designer**: Designs and implements Kubernetes CRD schemas and API definitions
- **api-developer**: Implements REST APIs and backend services
- **frontend-developer**: Creates user interfaces and client-side applications
- **devops-engineer**: Handles infrastructure, deployment, and CI/CD workflows

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

### Usage

Tasks are created as CooTask CRDs and automatically processed by designated AI agents. Each task follows a structured workflow from assignment through implementation to review.

## Workflow Example

Here's how a typical task flows through the system:

1. Issue #17 created: "Add Third README with project description"
2. CooTask CRD created and assigned to crd-designer agent
3. Agent creates draft PR with implementation plan
4. Agent analyzes requirements and implements changes
5. Changes committed and PR marked ready for review
6. Human reviewer provides feedback
7. Agent addresses feedback and updates PR
8. PR merged, task marked complete

### Quick Start Example

To see the system in action with your own task:

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

### Current Structure

- **Documentation**: README files demonstrating documentation workflows

### Planned Architecture Components

As this project evolves, the following directories will be added:

- **CRD Definitions**: Kubernetes Custom Resource Definitions for task management
- **Agent Scripts**: AI agent implementation and orchestration logic
- **Workflow Configs**: GitHub Actions and automation configurations

## Benefits of This Approach

- **Consistency**: Standardized workflows ensure consistent development practices
- **Traceability**: Every change linked to tasks, PRs, and reviews
- **Automation**: Reduces manual overhead in task management and PR creation
- **Scalability**: Easy to add new agents and task types
- **Observability**: Clear visibility into task status and progress through Kubernetes
- **Efficiency**: Automated task management reduces overhead
- **Transparency**: Full visibility into task status and progress

## Contributing

This project follows an automated development workflow where tasks are assigned to AI agents for implementation and human review.

### For Human Contributors

1. Review PRs created by AI agents
2. Provide constructive feedback
3. Approve and merge completed work
4. Create new issues for tasks

### For AI Agents

1. Monitor assigned tasks via CooTask CRDs
2. Create implementation plans in draft PRs
3. Implement changes following best practices
4. Respond to review feedback
5. Update task status throughout lifecycle

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
