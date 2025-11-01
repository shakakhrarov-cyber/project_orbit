# ORBIT Backend - Quick Start Guide

## Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose (optional)

## Setup

### Option 1: Using Docker Compose (Recommended)

1. Copy environment file:
```bash
cp .env.example .env
```

2. Start services:
```bash
docker-compose up -d
```

3. Run migrations:
```bash
docker-compose exec backend alembic upgrade head
```

4. Seed data:
```bash
docker-compose exec backend python scripts/seed_data.py
```

5. Access API:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

### Option 2: Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up database:
```bash
createdb orbit_db
```

3. Copy environment file:
```bash
cp .env.example .env
```

4. Update `.env` with your database credentials

5. Run migrations:
```bash
alembic upgrade head
```

6. Seed data:
```bash
python scripts/seed_data.py
```

7. Run server:
```bash
uvicorn main:app --reload
```

## Project Structure

```
backend/
├── api/              # API routes
├── core/             # Business logic
├── models/           # Database models
├── utils/            # Utilities
├── scripts/          # Seed scripts
├── seed_data/        # JSON seed files
├── alembic/          # Database migrations
├── main.py          # FastAPI app
└── config.py        # Configuration
```

## API Endpoints

- `POST /session/start` - Start interview session
- `POST /response` - Submit answer
- `GET /session/{id}/result` - Get match results
- `GET /docs` - API documentation

## Testing

Run tests:
```bash
pytest
```

## Development Notes

- Database migrations: `alembic revision --autogenerate -m "description"`
- Apply migrations: `alembic upgrade head`
- Rollback: `alembic downgrade -1`

