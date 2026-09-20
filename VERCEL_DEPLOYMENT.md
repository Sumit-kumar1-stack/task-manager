# Vercel Deployment

Deploy this repository as two Vercel projects.

## API

- Root Directory: `backend`
- Framework: FastAPI / auto-detect
- Environment: `DATABASE_URL`, `JWT_SECRET`, `CORS_ORIGINS`

Use hosted PostgreSQL for persistent data. The checked-in SQLite file is only a local-development artifact.

## Web

- Root Directory: `frontend`
- Framework: Vite
- Environment: `VITE_API_URL=https://<api-domain>`

After both projects exist, set the API's `CORS_ORIGINS` to the exact web production origin and redeploy the API.

## Verify

- `GET /health` on the API returns `{"status":"ok"}`.
- Registration and login work.
- JWT-protected task creation/listing works.
- Data survives redeployments through hosted PostgreSQL.
- Browser requests come from the configured production origin.
