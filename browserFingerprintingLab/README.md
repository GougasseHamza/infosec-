# Browser Fingerprinting Lab

A small Flask application for the M235 Information Security browser fingerprinting lab. It demonstrates passive request headers, active browser feature collection, and typing-behaviour measurements.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8000/` for the fingerprinting page and `http://127.0.0.1:8000/typing` for the typing experiment. The Flask app logs collected JSON to its console.

## Report

The concise LaTeX source, compiled PDF, and screenshots are in `report/`. The ZIP contains the report source, screenshots, and relevant lab code.
