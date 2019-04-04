from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def get_message(message):
    chatbot = ChatBot('Ron Obvious', read_only=True, logic_adapters=['chatterbot.logic.BestMatch',
                                                                     {'import_path': 'chatterbot.logic.BestMatch',
                                                                      'threshold': 0.65,
                                                                      'default_response': 'I am sorry, but I can only answer questions related to ACM.'
                                                                      }
                                                                     ],
                      input_adapter='chatterbot.input.VariableInputTypeAdapter',
                      output_adapter='chatterbot.output.OutputAdapter',
                      filter='chatterbot.filters.RepetitiveResponseFilter')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english.greetings",
                  "chatterbot.corpus.english.conversations",
                  "chatterbot.corpus.english.emotion",
                  "chatterbot.corpus.english.psychology")
    return chatbot.generate_response(message)
