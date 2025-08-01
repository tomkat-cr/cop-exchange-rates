# CHANGELOG

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a Changelog](http://keepachangelog.com/).



## Unreleased
---

### New

### Changes

### Fixes

### Breaks


## 1.1.1 (2025-07-31)
---

### Changes
- Enhance README with detailed setup instructions and API documentation in both English and Spanish.
- ".gitignore" to include IDE configurations.
- Modify .nvmrc for Node.js version 20
- Update Python version 3.13


## 1.1.0 (2025-07-26)
---

### New
- Add poetry configuration to make the project ready to be used as a package [GS-204].
- Add JSON formatting for CLI output [GS-204].
- Add request timeout handling [GS-204].

### Changes
- Rename "src" folder to "cop_exchange_rates" to match the project name [GS-204].

### Fixes
- Update dependencies to latest versions to fix Snyk alerts [GS-204].


## 1.0.0 (2023-01-22)
---

### New
- Ngrok for local dev environment test with the Telegram BOT.

### Changes
- OWNER envvar renamed to TELEGRAM_CHAT_ID.
- Move vercel.json to parent folder

### Fixes
- CLI python run doesn't find a src.index module error.


## 0.1.1 (2023-01-21)
---

### New
- npm commands + bank_value_percent resp entry

### Fixes
- npm deploy command v1 & v2


## 0.1.0 (2023-01-18)
---

### New
- Ideation and initial development
- "bank_value" added on both endpoints
- README links + code cleaning
