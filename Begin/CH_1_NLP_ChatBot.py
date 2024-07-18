# Importing TextBlob to help the chatbot understand language nuances.
# This line imports the TextBlob class from the TextBlob module, allowing you to use TextBlob's 
# natural language processing functionalities in your Python script. TextBlob is a Python library 
# for processing textual data. It provides a simple API for common NLP tests and sentiment analysis.
from textblob import TextBlob


# Defining the ChatBot class for interaction.
class ChatBot:
    def __init__(self):
        # Initializing the sentiment analysis tool.
        #This creates an instance variable and initializes it
        # with an empty TextBlob object. This object will serve as 
        # our tool for sentiment analysis. Now let's define a method called chart stat. Def start_chat self. Then we'll print a grading message from the ChatBot to the console. 
        self.sentiment_analyzer = TextBlob("") 

    def start_chat(self):
        print("ChatBot: Hi, how can I help you?")
        while True:
            user_message = input("You: ").strip()

            # Analyzing the sentiment of the user's message.
            self.sentiment_analyzer = TextBlob(user_message)
            #computes the polarity score-emotional skill of chatbox
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

            # Generating the chatbot's response based on sentiment.
            if sentiment_score > 0 :#more +ve sentiment
                chatbot_message = f"ChatBot: That's great to hear! \n Sentiment Score {sentiment_score}\n"
            elif sentiment_score <0:#more -ve sentiment
                chatbot_message = f"ChatBot: I am sorry to hear that. Would you like me to transfer you to a live agent? \n Sentiment Score: {sentiment_score}\n"
            else:#neutral statement
                chatbot_message=f"ChatBot: Hmm, I see. Can you please provide more information? \n Sentiment Score:{sentiment_score}\n"
            
            # Printing the chatbot's response and sentiment.
            print(chatbot_message)


if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    chatbot = ChatBot()
    chatbot.start_chat()