import flask
import train_chatbot
app = flask.Flask(__name__)


@app.route("/api", methods=['GET', 'POST'])
def message():
    data = {"success": False}
    params = flask.request.json

    if params is None:
        params = flask.request.args

    if params is not None:
        message = params.get("message")
        data["response"] = train_chatbot.get_message(message)
        data["success"] = True

    return flask.jsonify(data)


app.run(host="localhost")
