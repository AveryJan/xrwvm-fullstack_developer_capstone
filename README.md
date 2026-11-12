# fullstack_developer_capstone

Repository: `xrwvm-fullstack_developer_capstone` (recommended name matching grader's example)

Project name: **fullstack_developer_capstone**

Best Cars Dealership Review Application — a Django and React full-stack capstone with a dealer API, login and registration, review submission, sentiment service, and GitHub Actions checks.

## Quick start

Requires Python 3.11+ and Node.js 20+.

```bash
python3 -m venv .venv
source .venv/bin/activate                 # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r server/requirements.txt
cd server
python manage.py migrate
python manage.py createsuperuser --username root
python manage.py runserver 0.0.0.0:8000
```

In separate terminals:

```bash
cd server/backend && node server.js     # dealer API: localhost:3030
cd server/sentiment && node server.js   # sentiment API: localhost:5050
```

Open `http://localhost:8000/`. The Django site can display the dealer directory and use login, registration, and reviews. The dealer API is seeded with **50 synthetic demo dealers** (not real dealerships or customers) so its endpoints are testable.

## React frontend

`server/frontend/src/components/Register/Register.jsx` is a working React registration component. Run `npm install && npm run dev` inside `server/frontend` for the Vite React frontend at `localhost:5173`. The primary Django server also serves its own integrated application pages and static files.

## Sample checks

```bash
curl http://localhost:3030/fetchDealers
curl http://localhost:3030/fetchDealer/1
curl http://localhost:3030/fetchDealers/Kansas
curl http://localhost:3030/fetchReviews/dealer/1
curl http://localhost:8000/djangoapp/get_cars
curl http://localhost:5050/analyze/Fantastic%20services
```

Use actual command output (not example output) in the assignment. For login, register a user first and use `curl -c cookies.txt` to preserve login cookies before logout with `-b cookies.txt`.

## Security and configuration

This is a demonstration application, not production-hosted software. Django secret key, debug flag, allowed hosts, and CORS/CSRF assumptions must be configured for production deployment. The local dealer API uses in-memory demo review storage that resets on restart. Configure persistent database, HTTPS, stable domain, authentication policies, and deploy each service before presenting a public deployed URL.

## Evidence checklist

Use real browser screenshots of actual running pages for: `admin_login`, `admin_logout`, `get_dealers`, `get_dealers_loggedin`, `dealersbystate`, `dealer_id_reviews`, `dealership_review_submission`, `added_review`, `deployed_landingpage`, `deployed_loggedin`, `deployed_dealer_detail`, `deployed_add_review`. Show the browser address bar where requested; never use synthetic screenshots as evidence. Copy actual GitHub Actions job logs from a completed green run. A valid deployment URL is available only after deploying.
