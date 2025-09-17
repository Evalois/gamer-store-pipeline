# Lojinha Gamer - Runbook (local)

## Quick start (Docker Compose)
1. Install Docker and Docker Compose (or Docker Desktop).
2. From project root run:
   ```bash
   docker compose up --build
   ```
3. API: http://localhost:8000 (OpenAPI: /docs)
   Frontend: http://localhost:3000

## Create admin user
- POST to http://localhost:8000/api/v1/auth/signup with JSON body:
  { "username": "admin", "email": "", "password": "admin123" }

## ML model (local)
To train a toy model (for demo) run on host or inside a Python container:
```bash
python3 ml/train.py
# then copy ml_models/rf_demand.joblib to backend container path /app/ml_models/
```

## GitHub / CI
- This repo includes a placeholder GitHub Actions workflow at .github/workflows/ci.yml
- To push to GitHub:
  1. Create a new repo on GitHub.
  2. git init ; git add . ; git commit -m "Initial"
  3. git branch -M main
  4. git remote add origin git@github.com:<you>/<repo>.git
  5. git push -u origin main
