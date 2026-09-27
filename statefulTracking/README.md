# Web Privacy TP1 - Stateful Tracking

Simple student implementation of the Flask lab.

## Run

On macOS/Linux:

```bash
cd statefulTracking
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activation is `venv\Scripts\activate`.

Start each application in a separate terminal:

```bash
python app.py
cd publisher-one && python app.py
cd publisher-two && python app.py
cd tracker-one && python app.py
cd analytics && python app.py
cd tracker-two && python app.py
```

Open these pages in this order:

1. `http://127.0.0.1:8000` for headers and cookie attributes.
2. `http://127.0.0.1:8011`, then its AI article.
3. `http://localtest.me:8002`, then its Morocco article.
4. `http://tracker-one.localhost:9000/profile` for Tracker One's chronological log.
5. `http://analytics.localhost:9100/profile` for the first-party analytics log.

`127.0.0.1`, `localtest.me`, `tracker-one.localhost` and `analytics.localhost` are used as separate hosts, so the lab does not require editing the system hosts file. All of them resolve back to the local computer. Modern browsers may block third-party cookies. If that happens, the repeated `(new)` tracker IDs and blocked `Set-Cookie` reason in DevTools are valid privacy evidence.

## Cookie tests

Delete `aid` before each URL:

- `/?mode=session`
- `/?mode=persistent`
- `/?mode=secure`
- `/?mode=httponly`
- `/?mode=strict`

For the optional syncing demo, click the sync link inside Tracker One's iframe. Tracker One redirects its ID to Tracker Two. The saved pairs are visible at `http://tracker-two.localhost:9200/profile`.
