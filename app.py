from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Testing new pipeline - 24.01.2024 09:15 from github actions which does building/pushing image to repo, kustomize edit yaml files with new image tags, then the rest is handled by argo"
