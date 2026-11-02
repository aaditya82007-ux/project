import os
from pathlib import Path

from sarvamai import SarvamAI

# Load the project's .env into the process environment without an extra dependency.
for line in Path(__file__).with_name(".env").read_text(encoding="utf-8").splitlines():
    name, separator, value = line.partition("=")
    if separator and name.strip() == "SARVAM_API_KEY":
        os.environ.setdefault("SARVAM_API_KEY", value.strip().strip("\"'"))

api_key = os.environ.get("SARVAM_API_KEY")
if not api_key:
    raise SystemExit("Add SARVAM_API_KEY to .env before running this script.")

client = SarvamAI(api_subscription_key=api_key)
response = client.chat.completions(
    model="sarvam-105b-conversations",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
    max_tokens=128,
    reasoning_effort=None,
)
print(response.choices[0].message.content)

