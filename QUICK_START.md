# Run setup script
./setup.sh

# Or manually:

# Backend
cd backend
pip3 install -r requirements.txt
python3 -m alembic upgrade head  # After DB is set up
python3 scripts/seed_data.py
python3 -m uvicorn main:app --reload

# Frontend (in new terminal)
cd frontend
npm install
npm run dev

