# AI-Assisted Patient Intake Demo

A small educational project that collects a fictional patient's symptoms, history, medicines, allergies, and available readings, then prepares a clinician handoff and asks Sarvam's language model for possible explanations.

> **Demonstration only:** use fictional case details. This is not a medical product and must not be used to make real patient-care decisions.

## What the demo does

- Collects symptoms and when they began.
- Collects age, optional sex/gender details, past conditions, medicines and doses, and allergies.
- Collects heart rate, blood pressure, glucose, and the source/time of the readings.
- Creates a factual summary and asks Sarvam for up to three possible explanations and information that is missing.

The model's response is educational text, not a diagnosis. The demo does not determine whether a person is safe, rule out an emergency, recommend treatment, or conclude that symptoms are "only panic."

## How it works

```text
Browser form (`index.html`)
        │ fictional case details
        ▼
Local Python server (`server.py`)
        │ Sarvam SDK: `sarvamai`
        ▼
Sarvam Chat Completions API (`sarvam-105b`)
        │ generated text
        ▼
Browser displays the handoff and educational response
```

The API key stays on the Python server and is read from `.env`; it is not sent to the browser. The demo server binds to `127.0.0.1` and does not save submitted entries. Submitting a case sends its details to Sarvam. Sarvam workspace data-retention settings apply; its default is indefinite retention until an owner changes it. See [Sarvam's data-retention documentation](https://docs.sarvam.ai/api/platform/data-retention).

## Run locally

1. Install the Sarvam Python SDK:

   ```powershell
   python -m pip install sarvamai
   ```

2. Create a `.env` file in this project folder with:

   ```dotenv
   SARVAM_API_KEY=
   ```

   Add your key after `=` on your own machine. `.env` is excluded by `.gitignore`; never commit or share it.

3. Start the local server from this folder:

   ```powershell
   python server.py
   ```

4. Open [http://127.0.0.1:8000](http://127.0.0.1:8000), enter fictional details, check the confirmation box, and submit.

Keep the server window open while using the demo. Opening `index.html` directly or publishing it with GitHub Pages will not run the Python API backend. To host the AI version online, deploy `server.py` to a Python-capable backend and configure the API key as a server-side secret.

## Project files

- `index.html` — browser form and response display.
- `server.py` — local API server and Sarvam request.
- `intake_demo.py` — local text-only intake demonstration.
- `sarvam_chat.py` — minimal Sarvam chat-call example.
- `.gitignore` — excludes `.env` from Git.

## Scope and next steps

This prototype uses manually entered readings. It does not connect to hospital monitors, an electronic health record, speech recognition, or text-to-speech. Any future clinical workflow would need clinician-designed protocols, appropriate privacy/security review, and validation before real-world use.

