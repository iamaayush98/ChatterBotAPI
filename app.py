import flask
import train_chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
app = flask.Flask(__name__)


@app.route("/api", methods=['GET', 'POST'])
def message():
    data = {"success": False}
    params = flask.request.json

    if params is None:
        params = flask.request.args

    if params is not None:
        message = params.get("message")

        chatbot = ChatBot('Ron Obvious')

        # Create a new trainer for the chatbot
        trainer = ChatterBotCorpusTrainer(chatbot)

        # Train the chatbot based on the english corpus
        trainer.train("chatterbot.corpus.english")

        # Get a response to an input statement
        response = chatbot.get_response(message)
        data["response"] = str(response)
        data["success"] = True

    return flask.jsonify(data)


app.run(host="localhost")
