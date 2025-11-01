# ORBIT Frontend

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create `.env` file:
```
VITE_API_URL=http://localhost:8000
```

3. Start development server:
```bash
npm run dev
```

4. Open browser:
```
http://localhost:5173
```

## Project Structure

```
frontend/
├── src/
│   ├── components/     # React components
│   ├── hooks/          # Custom hooks
│   ├── types/          # TypeScript types
│   ├── utils/          # Utilities
│   ├── App.tsx         # Main app component
│   └── main.tsx        # Entry point
├── index.html
├── vite.config.ts
└── package.json
```

## Components

- `QuestionDisplay` - Displays question and handles responses
- `ResultsPage` - Shows match recommendations
- `App` - Main application logic and routing

## Development

- Hot reload enabled
- TypeScript strict mode
- Tailwind CSS for styling

