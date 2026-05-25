# ai-design-team

> **AI design team — multi-agent system for UI/UX design, prototyping, and review**

![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat)
![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-FF6B35?style=flat)
![Stars](https://img.shields.io/github/stars/hmzainjamil/ai-design-team?style=flat)
![Last Commit](https://img.shields.io/github/last-commit/hmzainjamil/ai-design-team?style=flat)

---

## CONCEPTS

| Concept | Description |
|---|---|
| **Design Agent** | Generates wireframes and component specs |
| **Review Agent** | Audits designs for accessibility and consistency |
| **Prototype Agent** | Converts specs to working HTML/CSS |
| **Brand Agent** | Enforces brand guidelines across all outputs |
| **Orchestrator** | Coordinates all agents in design pipeline |
| **Figma Export** | Outputs design tokens compatible with Figma |
| **WCAG Audit** | Checks AA/AAA accessibility compliance |
| **Style Guide** | Auto-generates living style documentation |

---

## 🔥 Hot Commands

```bash
# Activate skill
claude --skill ai-design-team 'your task'

# Quick workflow
claude 'design automation task'

# Get capabilities
claude 'what can ai-design-team do?'
```

## ■ tip
> Mention **design** or **team** in your prompt to auto-activate this skill.

---

## ☠️ STARTUPS / BUSINESSES

- **Agencies**: automate design workflows for clients at scale
- **Founders**: ship team features 10x faster
- **Freelancers**: deliver agent work with AI precision

---

## Features

- Design automation
- Team automation
- Agent automation
- Ui automation
- Ux automation
- Prototype automation

---

## Installation

```bash
git clone https://github.com/hmzainjamil/ai-design-team.git
cd ai-design-team
```

---

## Usage

```bash
# Activate skill in Claude Code
claude --skill ai-design-team "your task here"

# Quick workflow
claude "design automation task"

# Get help
claude "what can ai-design-team do?"
```

---

## Configuration

| Variable | Description | Default |
|---|---|---|
| `API_KEY` | Primary API key | Required |
| `MODEL` | AI model to use | claude-3-5-sonnet |
| `DEBUG` | Enable verbose debug | false |
| `MAX_TOKENS` | Max token budget | 8192 |
| `TIMEOUT` | Request timeout (sec) | 30 |
| `LOG_LEVEL` | Logging verbosity | info |

---

## Architecture

```
ai-design-team/
├── README.md           # Documentation
├── SKILL.md            # Claude Code skill definition
├── scripts/            # Automation scripts
├── templates/          # Output templates
├── examples/           # Usage examples
└── docs/               # Extended documentation
```

---

## Examples

### Basic

```bash
# Simple task
claude --skill ai-design-team "design task"

# Verbose
claude --skill ai-design-team --verbose "detailed team task"
```

### Advanced Pipeline

```bash
# Chain skills
claude --skill ai-design-team "step 1" | claude --skill summarize

# Batch run
for item in $(cat list.txt); do
  claude --skill ai-design-team "process $item"
done
```

---

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| Auth fails | Invalid API key | Re-export key in shell profile |
| Timeout | Network or large payload | Increase TIMEOUT value |
| Empty output | Prompt too vague | Add more context |
| Rate limit | Too many requests | Add delay between calls |
| Model error | Unsupported version | Update MODEL variable |
| Import error | Missing dependency | Run pip install -r requirements.txt |

---

## Comparison

| Feature | This Skill | Alt A | Alt B |
|---|---|---|---|
| Claude Code native | ✅ | ❌ | ✅ |
| Auto-activation | ✅ | ✅ | ❌ |
| Free to use | ✅ | ❌ | ✅ |
| Production ready | ✅ | ✅ | ❌ |
| Active maintenance | ✅ | ❌ | ❌ |

---

## Changelog

| Version | Changes |
|---|---|
| v2.0 | Claude 4 support, auto-activation |
| v1.5 | Added keyword triggers |
| v1.0 | Initial release |

---

## Contributing

1. Fork → feature branch → commit → PR
2. Follow conventional commits: `feat:`, `fix:`, `docs:`
3. Add tests for new features

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/ai-design-team&type=Date)](https://star-history.com/#hmzainjamil/ai-design-team&Date)

---

## 📜 License

MIT — free to use, modify, distribute.

---

Made with ❤️ by [@hmzainjamil](https://github.com/hmzainjamil)
