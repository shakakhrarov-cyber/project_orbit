# ORBIT - Setup Guide

## Prerequisites Check

Run these commands to check what's installed:
```bash
which python3
which pip3
which node
which npm
which docker
```

## Backend Setup (Without Docker)

### Step 1: Install Python Dependencies
```bash
cd /Users/shakakhrarov/ORBIT/backend
pip3 install -r requirements.txt
```

### Step 2: Set Up PostgreSQL
You need PostgreSQL running. Options:
- Install PostgreSQL locally: `brew install postgresql@15`
- Use a cloud database (adjust DATABASE_URL in .env)
- Or skip for now and use SQLite for testing (see below)

### Step 3: Set Up Redis (Optional for MVP)
- Install Redis: `brew install redis`
- Or skip for now (we'll add a fallback)

### Step 4: Configure Environment
```bash
cd /Users/shakakhrarov/ORBIT/backend
cp .env.example .env
# Edit .env with your database URL
```

### Step 5: Run Migrations
```bash
cd /Users/shakakhrarov/ORBIT/backend
python3 -m alembic upgrade head
```

### Step 6: Seed Data
```bash
cd /Users/shakakhrarov/ORBIT/backend
python3 scripts/seed_data.py
```

### Step 7: Start Server
```bash
cd /Users/shakakhrarov/ORBIT/backend
python3 -m uvicorn main:app --reload
```

## Frontend Setup

### Step 1: Install Dependencies
```bash
cd /Users/shakakhrarov/ORBIT/frontend
npm install
```

### Step 2: Start Dev Server
```bash
cd /Users/shakakhrarov/ORBIT/frontend
npm run dev
```

## Quick Start (Simplified - SQLite for Testing)

If you don't have PostgreSQL set up, we can modify the backend to use SQLite for testing:

1. Update `backend/config.py` to use SQLite temporarily
2. Run migrations
3. Seed data
4. Start server

## Troubleshooting

### "command not found" errors
- Use `python3` instead of `python`
- Use `pip3` instead of `pip`
- Use `python3 -m alembic` instead of `alembic`
- Use `python3 -m uvicorn` instead of `uvicorn`

### Docker not found
- Docker is optional - you can run everything locally
- If you want Docker: Install Docker Desktop from https://www.docker.com/products/docker-desktop
- Modern Docker uses `docker compose` (with space) instead of `docker-compose`

### Port already in use
- Backend default: port 8000
- Frontend default: port 5173
- Change ports in config if needed

