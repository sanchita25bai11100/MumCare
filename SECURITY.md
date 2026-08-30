# Security Policy

## Overview

MumCare is an academic/prototype project exploring AI-assisted maternal healthcare.

Because the project deals with potentially sensitive healthcare information, security and privacy are treated as core design considerations.

## Security Principles

MumCare is designed around:

- 🔐 Secure authentication and authorization
- 🛡️ Protection of sensitive information
- 🔑 Secret and API-key management
- 📦 Controlled access to uploaded documents
- 🧾 Auditability of important system actions
- 🚫 No sensitive information in source code or logs
- 👤 User consent and data minimization

## Reporting a Vulnerability

If you discover a security issue in this project, please avoid publicly exposing sensitive information.

Instead, document the issue clearly and provide enough information to reproduce it so that it can be reviewed and addressed responsibly.

## Sensitive Data

Do not commit any of the following to this repository:

- API keys
- Passwords
- Authentication tokens
- Private credentials
- Real medical reports
- Personally identifiable health information
- Production database credentials

Use environment variables for secrets.

The repository provides `.env.example` as a configuration template.

## AI Safety

MumCare is designed as an AI-assisted support system.

AI-generated information should not be treated as a medical diagnosis or prescription.

Potentially serious situations should be escalated to qualified healthcare professionals.

## Project Status

MumCare is currently an academic/prototype project and should not be considered production-ready medical software.
