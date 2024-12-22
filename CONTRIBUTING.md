# Contributing to Quantum Server

Thank you for your interest in contributing to Quantum Server! This document provides guidelines and instructions for contributing to the project.

## Development Guidelines

### Code Style and Standards

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Keep functions focused and concise
- Document functions with clear docstrings
- Use type hints where appropriate

### Directory Structure

```
quantum_server/
├── tests/          # Test files
├── .github/        # GitHub specific files
│   ├── workflows/  # GitHub Actions
│   └── templates/  # Issue and PR templates
└── chat_with_qwq.py # Main application code
```

### Commit Message Conventions

Follow the Pull Request template.

## Pull Request Process

1. **Fork and Clone**: Fork the repository and clone it locally
2. **Branch**: Create a branch from `main` using a descriptive name
   ```bash
   git checkout -b feat/new-feature
   # or
   git checkout -b fix/bug-description
   ```
3. **Develop**: Make your changes, following our development guidelines
4. **Test**: Ensure all tests pass and add new ones for your changes
5. **Submit**: Push your changes and create a Pull Request

### PR Requirements

- Must be reviewed by at least one maintainer
- Must pass all automated tests
- Must have adequate test coverage
- Must pass linting checks
- Must align with project's design philosophy
- Must include documentation updates if relevant
- Must be signed using the SSH key of the contributor

## Commit signing

### Why Sign Commits?

Signing commits ensures their authenticity and confirms that they were made by you.

How to Sign Commits Using SSH:

1. Configure Git to sign commits using SSH:
```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519
git config --global commit.gpgSign true
```

2. When committing:
```bash
git commit -S -m "Your commit message"
```

3. Ensure your SSH public key is added to GitHub.

## Issue Reporting

### Bug Reports:

1. Use the Bug Report Template when submitting a bug.
2. Provide:
   - Steps to reproduce
   - Expected and actual behavior
   - Environment details (Python version, OS, etc.)
   - Relevant logs or error messages

### Feature Requests:

1. Use the Feature Request Template
2. Include:
   - Rationale for the feature
   - Proposed solution
   - Impact on user experience and maintainability

## Quality Assurance

### Testing Requirements

- Write unit tests for new functionality using pytest
- Ensure tests are meaningful and not just for coverage
- Aim for at least 80% test coverage for new code

### Code Quality Tools

Before submitting a PR, run:

```bash
# Format code
black .

# Run linter
flake8 --exclude=./venv

# Run tests
pytest tests/
```

Consider setting up pre-commit hooks for these checks.

## API Design Standards

### API Guidelines

- Follow RESTful principles
- Use consistent response formats
- Implement proper error handling
- Provide clear API documentation
- Support proper content negotiation
- Ensure proper security headers

### Endpoint Structure

- Keep endpoints intuitive and consistent
- Use proper HTTP methods
- Implement comprehensive error responses
- Document all endpoints using OpenAPI/Swagger

## Branching and Release Strategy

### Branch Structure

- `main`: Stable production code
- `develop`: Integration branch for features
- `feature/*`: New features
- `fix/*`: Bug fixes
- `release/*`: Release preparation

### Release Process

1. Features are merged into `develop`
2. Release branch created from `develop`
3. Version bumped and changelog updated
4. Release branch merged to `main`
5. `main` tagged with version
6. Changes back-merged to `develop`

## Getting Help

- Open an issue for questions
- Join our community discussions
- Check existing documentation and issues

## Code of Conduct

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
