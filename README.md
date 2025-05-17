# SmartAgroInsights

A monorepo for Soil Analysis App:

- **frontend/**: React app (Create React App), deployed as a static site.
- **backend/**: Python serverless functions on Vercel for parsing, AI analysis, and PDF generation.

## Deployment

1. Initialize Git and push to GitHub:
   ```bash
   cd SmartAgroInsights
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. Connect your GitHub repo to Vercel:
   - In Vercel dashboard, import the GitHub repository.
   - Vercel will automatically detect the frontend and backend.
   - The frontend build command is `npm run build --prefix frontend`.
   - Python backend functions will be deployed from `backend/`.

## Local Development

- **Frontend**:  
  ```bash
  cd frontend
  npm install
  npm start
  ```

- **Backend** (individual functions):  
  ```bash
  cd backend
  python parser.py
  # or run others similarly
  ```