# Documentation index

| Document | Role | Evidence and limits |
|---|---|---|
| [README](../README.md) | Application purpose, setup, data flow, deployment warning | Based on `app.py`, dependencies, and deployment files |
| [Security notes](../SECURITY.md) | API key, image privacy, and network exposure | Guidance, not a security audit |
| [Application source](../app.py) | Streamlit UI and Gemini integration | Inspect before handling sensitive uploads |
| [Dependencies](../requirements.txt) | Python packages | Source list; not an installation verification |
| [Project metadata](../pyproject.toml) | Python requirement and launch script | Launch command disables XSRF/CORS and binds all interfaces |
| [Dockerfile](../Dockerfile) and [Procfile](../Procfile) | Hosting configuration | Do not expose publicly without security changes |
| [Styles](../styles/custom.css) | UI style rules | Presentation only |
| [Static helper](../static/js/websocket_fix.js) | Browser-side WebSocket helper | Review source before deployment |
