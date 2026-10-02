# AI Design Team

A Streamlit application for reviewing uploaded design images with Google's Gemini API. The app accepts design images and optional competitor images, asks the configured Gemini model for design/UX/market analyses, and displays generated feedback and social-post suggestions.

This repository is an application, not an autonomous multi-agent design squad. The displayed analysis stages do not establish independent agents or unattended brand-system production.

## Requirements and setup

The project metadata requires Python 3.10 or newer. Dependencies are listed in [`requirements.txt`](requirements.txt).

```bash
pip install -r requirements.txt
streamlit run app.py
```

Enter a Gemini API key in the application UI. Uploaded design images and prompts are sent to the configured Google Gemini service for analysis. Check the service's current data terms before submitting confidential or unpublished work.

## Configuration and deployment

The [Dockerfile](Dockerfile), [Procfile](Procfile), and [project script](pyproject.toml) bind Streamlit to `0.0.0.0` and disable XSRF protection and CORS. Do not expose this configuration to a public or untrusted network. Use an authenticated private deployment, enable appropriate request protections, and review proxy/origin settings before hosting.

The UI accepts an API key and image uploads. Do not share a deployment with untrusted users unless access controls, per-user data isolation, and key handling have been reviewed.

## Repository map

- [Application](app.py): Streamlit UI and Gemini requests
- [Styles](styles/custom.css): application styling
- [Static assets](static/): client-side WebSocket helper
- [Assets](assets/): application images and examples
- [Container setup](Dockerfile) and [Procfile](Procfile): deployment commands
- [Security notes](SECURITY.md): data and network exposure

## Status and verification

No tests or deployment checks were run for this documentation change. Source and configuration describe intended behavior; they do not prove model availability, analysis quality, secure deployment, or successful end-to-end use.
