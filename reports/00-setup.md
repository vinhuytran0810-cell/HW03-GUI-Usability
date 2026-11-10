# EShop setup report

## Scope and source layout

The repository describes four components:

- `backend/`: Express API and SQLite database.
- `frontend-web/`: React/Vite storefront; pages are under `src/pages/` and authentication/cart contexts under `src/context/`.
- `frontend-admin/`: separate React/Vite admin application.
- `frontend-mobile/`: React Native/Expo application.

For browser-based customer screens, only the backend API and `frontend-web` are required. The web router defines `/register`, `/login`, `/forgot-password`, and `/profile`.

## Environment and dependencies

- OS: Windows.
- Node.js: `v24.11.1` (setup guide requires `>=18`).
- npm: `11.6.2`.
- Backend dependencies installed successfully: Express, body-parser, CORS, jsonwebtoken, and sqlite3.
- Web dependencies installed successfully: React, React DOM, React Router, Axios, Vite, Tailwind CSS, and ESLint tooling.
- No `.env` configuration is needed for this setup as currently written. The API listens on port `3000`; the web client uses that API address directly. The database file is `backend/database.sqlite`.
- `frontend-web` production build completed successfully with `npm run build`.

## Starting the web application

Run these commands in separate PowerShell terminals:

```powershell
Set-Location .\backend
npm install
node server.js
```

```powershell
Set-Location .\frontend-web
npm install
npm run dev -- --host 127.0.0.1
```

The running API reported `http://localhost:3000`; `GET /api/products` returned HTTP 200 with product data. Vite reported ready at **http://127.0.0.1:5173/**, and the page returned HTTP 200 and rendered the seeded product list in the browser.

The backend starts against SQLite and the frontend is currently running. Web URL for review: **http://127.0.0.1:5173/**.

## Screen accessibility observed in browser

| Screen | URL | Observed result |
|---|---|---|
| Registration | `http://127.0.0.1:5173/register` | Opened; registration form rendered. |
| Login | `http://127.0.0.1:5173/login` | Opened; login form rendered. Login with the README test account succeeded. |
| Forgot Password | `http://127.0.0.1:5173/forgot-password` | Opened; initial email/OTP-request step rendered. The reset flow was not submitted. |
| Profile | `http://127.0.0.1:5173/profile` | Opened. Without a session it displayed “Vui lòng đăng nhập”; after login it rendered the profile form and order-history section. |

Test account used: `test@eshop.com` / `Test1234!` (documented in the repository README).

## Environment limitations and unresolved setup warnings

- `npm install` reported audit advisories: backend **5** (1 moderate, 2 high, 2 critical) and web frontend **19** (2 low, 6 moderate, 11 high). No audit fixes were applied.
- The frontend build warned that its Browserslist/caniuse-lite data is about six months old.
- The bundled `run_servers.sh` is not suitable for this Windows environment: it is a Bash script, contains machine-specific macOS paths, and calls `killall node`. The commands above were used instead.
- Admin and mobile dependencies were not installed and those components were not started; neither is needed for the requested web screens. Admin has a separate Vite server (guide default `5174`); mobile requires Expo plus an Expo Go app or an emulator.
- **Database caution:** `backend/server.js` imports `database.js`, and `database.js` calls its initializer on import. That initializer drops and recreates the application tables before seeding them. Starting the backend therefore reinitializes `backend/database.sqlite`; this happened during this setup. Avoid starting it if the local database contains data that must be preserved.
- The setup/install created local dependency directories and refreshed npm lockfile metadata; the backend database file was also rewritten by its initializer.

## Verification performed

- Installed backend and web dependencies.
- `npm run build` in `frontend-web`: passed.
- Backend product endpoint and web root: HTTP 200.
- Opened all four requested browser routes; authenticated profile view verified using the documented test account.

No business logic was changed. No registration, forgot-password, or profile-update submission was performed.
