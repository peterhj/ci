from flask import Flask, request
#from hmac import compare_digest
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/theproject/ghevent", methods=["POST"])
def ghevent_router():
  app.logger.info("post")
  #app.logger.info("  headers: {}".format(request.headers))
  payload = request.get_json(force=True)
  #app.logger.info("  payload: {}".format(payload))
  return ""
  if "X-GitHub-Event" not in request.headers:
    # TODO
    return None
  gh_digest = request.headers["X-Hub-Signature"]
  gh_event = request.headers["X-GitHub-Event"]
  if gh_event == "pull_request":
    # TODO: do something based on `payload["action"]`.
    # TODO
    return None
  # TODO
  return None
