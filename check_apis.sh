#!/usr/bin/env bash
set -euo pipefail
curl --fail --silent http://localhost:3030/fetchDealers
curl --fail --silent http://localhost:3030/fetchDealer/1
curl --fail --silent http://localhost:3030/fetchDealers/Kansas
curl --fail --silent http://localhost:3030/fetchReviews/dealer/1
curl --fail --silent http://localhost:8000/djangoapp/get_cars
curl --fail --silent 'http://localhost:5050/analyze/Fantastic%20services'
