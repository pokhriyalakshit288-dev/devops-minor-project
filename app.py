from flask import Flask, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DevOps Demo App</title>
  <style>
    body { font-family: Arial, sans-serif; background:#f3f6fb; margin:0; color:#182230; }
    main { max-width:760px; margin:8vh auto; padding:32px; background:white; border-radius:16px;
           box-shadow:0 8px 28px rgba(0,0,0,.08); }
    h1 { color:#2457c5; margin-top:0; }
    .tag { display:inline-block; background:#e5edff; color:#2048a0; padding:8px 12px;
           border-radius:999px; font-size:14px; }
    li { margin:10px 0; }
    footer { margin-top:28px; color:#5b6574; font-size:13px; }
  </style>
</head>
<body><main>
  <span class="tag">BCA Minor Project • DevOps</span>
  <h1>Automated Web App Deployment</h1>
  <p>This demo application is running inside a Docker container on an Ubuntu server.</p>
  <h2>DevOps tools used</h2>
  <ul><li>Linux / Ubuntu — server environment</li><li>Git &amp; GitHub — source control</li>
      <li>Docker — containerization</li><li>Jenkins — CI/CD pipeline (optional extension)</li></ul>
  <p><b>Application status:</b> Running</p>
  <p><b>Container hostname:</b> {{ hostname }}</p>
  <p><b>Server time (UTC):</b> {{ server_time }}</p>
  <footer>Educational demo created for a BCA Minor Project. Do not put secrets in source code.</footer>
</main></body></html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE, hostname=os.uname().nodename, server_time=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
