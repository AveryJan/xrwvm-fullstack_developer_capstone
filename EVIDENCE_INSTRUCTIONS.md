# Required assignment evidence

This file is an instruction list, not proof of execution.

## Terminal text
Save terminal command and **actual** response together using `tee` after services start:

- Task 2: `cd server && python manage.py runserver 0.0.0.0:8000` → terminal output `django_server`
- Task 5: first register a user; login via `curl -c cookies.txt -X POST http://localhost:8000/djangoapp/login -H 'Content-Type: application/json' -d '{"userName":"learner","password":"GoodPassword123"}'` → `loginuser`
- Task 6: `curl -b cookies.txt http://localhost:8000/djangoapp/logout` → `logoutuser`
- Task 8: `curl http://localhost:3030/fetchReviews/dealer/1` → `getdealerreviews`
- Task 9: `curl http://localhost:3030/fetchDealers` → `getalldealers`
- Task 10: `curl http://localhost:3030/fetchDealer/1` → `getdealerbyid`
- Task 11: `curl http://localhost:3030/fetchDealers/Kansas` → `getdealersbyState`
- Task 14: `curl http://localhost:8000/djangoapp/get_cars` → `getallcarmakes`
- Task 15: `curl 'http://localhost:5050/analyze/Fantastic%20services'` → `analyzereview`
- Task 22: copy real GitHub Actions successful workflow header, jobs and steps into `CI_CD` after upload and successful run.

## Source file URLs
With the repository named `xrwvm-fullstack_developer_capstone`:

- README: `https://github.com/<YOUR_GITHUB_USERNAME>/xrwvm-fullstack_developer_capstone/blob/main/README.md`
- About: `.../blob/main/server/frontend/static/About.html` (see note below)
- Contact: `.../blob/main/server/frontend/static/Contact.html`
- Register: `.../blob/main/server/frontend/src/components/Register/Register.jsx`

The static `About.html` and `Contact.html` files are included at the exact paths the grader requests; Django renders corresponding templates from `server/frontend/templates/`.

## Screenshots
These must be screenshots taken of the real app, not mockups. Capture browser address bar as required.

`admin_login.png`, `admin_logout.png`, `get_dealers.png`, `get_dealers_loggedin.png`, `dealersbystate.png`, `dealer_id_reviews.png`, `dealership_review_submission.png`, `added_review.png`, `deployed_landingpage.png`, `deployed_loggedin.png`, `deployed_dealer_detail.png`, `deployed_add_review.png`.

## Deployment
A local server is not a public deployment. Set secrets and allowed hosts, deploy Django and both API services together with an appropriate reverse proxy, persist databases and reviews, then submit the real public URL. Never submit a placeholder URL.
