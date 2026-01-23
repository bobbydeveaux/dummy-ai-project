# dummy-ai-project - Third Documentation

A demonstration project showcasing AI-powered development workflows and automated task management using Kubernetes Custom Resource Definitions (CRDs).

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
