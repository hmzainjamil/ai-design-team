# Security notes

The app accepts an API key in the UI and uploads design images to Google's Gemini API for analysis. Treat uploaded images, prompts, and generated content as potentially sensitive.

- Check the provider's current data-handling terms before uploading confidential or unpublished designs.
- Do not commit API keys or place them in shared screenshots, logs, or public deployments.
- The checked-in Dockerfile and Procfile bind to `0.0.0.0` and disable Streamlit XSRF protection and CORS. Do not expose that configuration to an untrusted network.
- Require authentication at the application or trusted proxy boundary, enable suitable request protections, restrict origins, and test user/session isolation before hosting.
- Review dependency and deployment changes before running the app in a shared environment.

This note reports source-visible configuration; it is not a penetration test or deployment approval.
