#!/bin/bash
# Quick setup script for ORBIT

set -e

echo "🚀 ORBIT Setup Script"
echo "===================="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.11+"
    exit 1
fi
echo "✅ Python 3 found: $(python3 --version)"

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found. Please install pip"
    exit 1
fi
echo "✅ pip3 found"

# Setup Backend
echo ""
echo "📦 Setting up backend..."
cd backend

if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found in backend/"
    exit 1
fi

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "✅ Backend dependencies installed"

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOF
DATABASE_URL=postgresql://orbit:orbit_dev@localhost:5432/orbit_db
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=
DEBUG=False
EOF
    echo "✅ Created .env file (please update with your database credentials)"
fi

cd ..

# Setup Frontend
echo ""
echo "📦 Setting up frontend..."
cd frontend

if [ ! -f "package.json" ]; then
    echo "❌ package.json not found in frontend/"
    exit 1
fi

# Check Node
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found. Please install Node.js 18+"
    echo "   Visit: https://nodejs.org/"
    exit 1
fi
echo "✅ Node.js found: $(node --version)"

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm"
    exit 1
fi
echo "✅ npm found: $(npm --version)"

echo "Installing Node dependencies..."
npm install

echo "✅ Frontend dependencies installed"

cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set up PostgreSQL and Redis (or use cloud services)"
echo "2. Update backend/.env with your database URL"
echo "3. Run migrations: cd backend && python3 -m alembic upgrade head"
echo "4. Seed data: cd backend && python3 scripts/seed_data.py"
echo "5. Start backend: cd backend && python3 -m uvicorn main:app --reload"
echo "6. Start frontend: cd frontend && npm run dev"

