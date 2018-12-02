from flask import Flask, request
#from hmac import compare_digest

app = Flask(__name__)

@app.route("/theproject/gh/event", methods=["POST"])
def gh_event_router():
  if "X-GitHub-Event" not in request.headers:
    # TODO
    return None
  gh_digest = request.headers["X-Hub-Signature"]
  gh_event = request.headers["X-GitHub-Event"]
  if gh_event == "pull_request":
    payload = request.get_json(force=True)
    # TODO: do something based on `payload["action"]`.
    # TODO
    return None
  # TODO
  return None
