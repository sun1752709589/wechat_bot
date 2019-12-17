from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pdb


chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
pdb.set_trace()
# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
