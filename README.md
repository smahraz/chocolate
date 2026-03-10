# Chocolate

A Discord bot that connects to the [42 Network](https://www.42.fr) API. It tracks student progress, shows profile cards, and posts project reports to a channel.

---

## Requirements

**Local:**
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (fast Python package manager)

**Docker:**
- Docker with Compose plugin

---

## Setup

### 1. Clone the repo

```bash
git clone <repo-url>
cd chocolate
```

### 2. Create your `.env`

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and set:

| Variable         | Where to get it |
|------------------|-----------------|
| `DISCORD_TOKEN`  | [Discord Developer Portal](https://discord.com/developers/applications) → your app → Bot → Token |
| `API_UID`        | [42 Intra](https://profile.intra.42.fr/oauth/applications) → your app → UID |
| `API_SECRET`     | Same 42 Intra app → Secret |

### 3. Configure the bot

Edit `config.json` to match your Discord server:

```json
{
  "roles": {
    "moderators": ["Staff"],
    "devs": ["Bot Dev"],
    "intra_access": ["Staff", "Intra"]
  },
  "channels": {
    "projects_report": [YOUR_CHANNEL_ID]
  }
}
```

- `moderators` — roles that can use moderator commands
- `devs` — roles that can use dev commands
- `intra_access` — roles that can look up 42 profiles
- `projects_report` — channel IDs where project updates get posted

---

## Run

The `run.sh` script handles everything. If `.env` is missing, it creates one from `.env.example` and asks you to fill it in before continuing.

### Locally (with uv)

```bash
./run.sh
```

### With Docker

```bash
./run.sh --docker
```

---

## Project structure

```
chocolate/
├── chocolate/
│   ├── api42/          # 42 Intra API client and auth
│   ├── cards/          # Discord embed card builders
│   ├── cogs/           # Discord command groups
│   └── tracker/        # Student progress tracker
├── config.json         # Bot roles and channel config
├── .env.example        # Environment variable template
├── Dockerfile
├── docker-compose.yml
└── run.sh              # Start script (local or Docker)
```

---

## Discord bot permissions

When adding the bot to your server, enable these intents in the Developer Portal:

- **Message Content Intent**
- **Server Members Intent**
