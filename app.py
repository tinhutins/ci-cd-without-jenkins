from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Testing new pipeline - 23.01.2024 16:50 from github actions which does building/pushing image to repo, kustomize edit yaml files with new image tags, then the rest is handled by argo"

