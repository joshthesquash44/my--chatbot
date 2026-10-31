import os
import re
import random

from flask import Flask, render_template, request, jsonify, session
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.secret_key = os.environ.get(
    "SECRET_KEY", "change-this-development-key"
)

messages = [
    "hi",
    "hello",
    "hey there",
    "hi there",
    "good morning",
    "good afternoon",
    "good night",
    "goodbye",
    "bye",
    "see you later",
    "how are you",
    "how is your day",
    "what's up",
    "what are you doing",
    "can you help me",
    "help me please",
    "what is Python",
    "how does coding work",
    "what is your name",
    "who are you",
    "tell me a joke",
    "say something funny",
    "thank you",
    "thanks",
    "you're welcome",
    "I'm bored",
    "that's cool",
    "that's awesome",
    "I don't understand",
    "explain that",
    "tell me something interesting",
    "what can you do",
    "are you smart",
    "what is your favorite color",
    "do you like games",
    "let's play a game",
    "I'm happy",
    "I'm sad",
    "I'm confused",
    "nice to meet you",
    "good job",
    "try again",
    "what time is it",
    "tell me a story",
    "can you tell me a story",
    "make up a story",
    "give me an idea",
    "how do I learn Python",
    "what is an AI",
    "how do computers work",
    "I'm back",
    "see you tomorrow"
]

labels = [
    "greeting",
    "greeting",
    "greeting",
    "greeting",
    "good_morning",
    "good_afternoon",
    "good_night",
    "goodbye",
    "goodbye",
    "goodbye",
    "question",
    "question",
    "question",
    "question",
    "help",
    "help",
    "question",
    "question",
    "question",
    "question",
    "joke",
    "joke",
    "thanks",
    "thanks",
    "thanks",
    "feeling",
    "reaction",
    "reaction",
    "confused",
    "help",
    "question",
    "question",
    "question",
    "question",
    "question",
    "game",
    "feeling",
    "feeling",
    "feeling",
    "greeting",
    "reaction",
    "command",
    "question",
    "story",
    "story",
    "story",
    "idea",
    "help",
    "question",
    "question",
    "greeting",
    "goodbye"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

ai = MultinomialNB()
ai.fit(X, labels)
def clean_text(text):
    """Normalize text for comparing answers and commands."""
    return re.sub(r"[^a-z0-9\s]", "", text.lower()).strip()


def get_bot_reply(message):
    """Handle one message from a website visitor."""
    message_lower = clean_text(message)
    mode = session.get("mode")

    if mode == "joke_answer":
        correct_answer = session.get("joke_answer", "")

        if message_lower == clean_text(correct_answer):
            session.pop("mode", None)
            session.pop("joke_answer", None)
            return "Ding ding ding! Correct!"

        if message_lower in ["idk", "i dont know", "dont know"]:
            session.pop("mode", None)
            session.pop("joke_answer", None)
            return "Okay bro What do you mean you don't know?"

        session["mode"] = "joke_offer"
        return (
            "Not quite! Would you like the answer? "
            "Type yes to reveal it or no to keep guessing."
        )

    if mode == "joke_offer":
        if message_lower == "yes":
            answer = session.get("joke_answer", "")
            session.pop("mode", None)
            session.pop("joke_answer", None)
            return f"The answer is: {answer}"

        if message_lower == "no":
            session["mode"] = "joke_guess_again"
            return "Okay! Keep guessing. Type quit to stop!"

        return "Please type yes or no."

    if mode == "joke_guess_again":
        answer = session.get("joke_answer", "")

        if message_lower == "quit":
            session.pop("mode", None)
            session.pop("joke_answer", None)
            return "Game ended! Want to try another joke?"

        if message_lower == clean_text(answer):
            session.pop("mode", None)
            session.pop("joke_answer", None)
            return "Correct! 🎉"

        return "Not quite! Try again, or type quit to stop."

    if mode == "story_choice":
        session.pop("mode", None)

        if message_lower == "yes":
            spooky_stories = [
                (
                    "Every night, Emma closed her closet door before "
                    "going to bed. Every morning, it was open. One night, "
                    "she stayed awake and watched it. At exactly 3:00 a.m., "
                    "the door slowly creaked open. Emma whispered, "
                    "'Who's there?' A tiny voice answered, 'You told me "
                    "to come out.' Emma froze. She lived alone. Then her "
                    "phone buzzed. It was a message from her mom: "
                    "'Sweetie, I found your old imaginary friend's drawing "
                    "in the attic. Remember the name you gave him?' "
                    "The drawing showed a tall, shadowy figure. Underneath "
                    "it was written: 'Closet Charlie.' From inside the "
                    "closet came a giggle..."
                ),
                (
                    "Noah forgot his backpack at school and returned after dark. The hallways were empty, except for the sound of footsteps behind him. He turned around. Nobody. He hurried to his classroom, grabbed his bag, and ran toward the exit. Then the school intercom crackled. 'Noah, please report to room 13.' His school didn't have a Room 13. He ran faster. The intercom spoke again: 'Noah, we can see you.' He burst through the front doors and called his mom. The next morning, he asked his teacher about the announcement. She went pale. 'Noah,' she said, 'the intercom has been disconnected for ten years.'"
                )
            ]
            return random.choice(spooky_stories)

        if message_lower == "no":
            return "Sorry, I'm still learning how to tell regular stories!"

        session["mode"] = "story_choice"
        return "Please type yes or no. Do you want a spooky story?"

    if mode == "game_choice":
        if message_lower in ["guessing game", "guess", "guessing"]:
            session["mode"] = "guessing_game"
            session["game_number"] = random.randint(1, 1000)
            session["attempts"] = 0
            return (
                "Let's play! I'm thinking of a number between 1 and "
                "1,000. Type your guess!"
            )
        if message_lower = "black jack.strip("?, !")
            import random
            print("GAMBLE BOT 9,000")
            choice = "hit"
            command = "taxes"
            evil_total=0
            jack = ten = queen = king = 10
            ace = 11
            two = 2
            three = 3
            four = 4
            five = 5
            six = 6
            seven = 7
            eight = 8
            nine = 9
            cards = [two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,ace]
            picked_card1.strip() = random.choice(cards)
            total= picked_card1
            print (f"your card is {picked_card1}")
            evil_card1 = random.choice(cards)
            evil_total= evil_card1
            print (f"the dealers card is {evil_card1}")
            
            while True:
                if choice == "stand":
                    print ("the dealer goes again")
                else:
                    choice = input("hit or stand?:   ")
            
            
                if choice == "hit":
                    picked_card2 = random.choice(cards)
                    total = (total+picked_card2)
                    print (f"your card is {picked_card2} so your total is {total}")
                if evil_total>total:
                    print (f"the dealer stands and his final total is {evil_total}.")
                    command = ("break")
                else:
                        
                    evil_card2 = random.choice(cards)
                    evil_total = (evil_total+evil_card2)
                    print (f"the dealers card is {evil_card2} so their total is {evil_total}")
                if evil_total>21:
                    if total>21:
                        print ("you tie")
                        break
                    else:
                        print ("you win")
                        break
                if total>21:
                    if evil_total>21:
                        print ("Its a tie!!!")
                        break
                    else:
                        print ("you lose")
                        break
                if command == "break":
                    if total>evil_total:
                        print ("you win")
                    if evil_total>total:
                        print ("you lose!!!!!!!!!!")
                    break

        if message_lower in ["quit", "cancel", "no"]:
            session.pop("mode", None)
            return "Okay! Maybe we can play another time."

        return (
            "Right now, I have a guessing game! and black jack game  "
            "Type 'guessing game' to play, Black jack, or 'quit' to stop."
        )

    if mode == "guessing_game":
        if message_lower == "quit":
            session.pop("mode", None)
            session.pop("game_number", None)
            session.pop("attempts", None)
            return "Thanks for playing! Want to play again sometime?"

        try:
            number = int(message_lower)
        except ValueError:
            return "Please enter a whole number, or type quit to stop."

        if not 1 <= number <= 1000:
            return "Choose a number between 1 and 1,000!"

        session["attempts"] = session.get("attempts", 0) + 1
        secret_number = session["game_number"]

        if number < secret_number:
            return "Too low! Guess again."

        if number > secret_number:
            return "Too high! Guess again."

        attempts = session["attempts"]
        session.pop("mode", None)
        session.pop("game_number", None)
        session.pop("attempts", None)

        return (
            f"You beat my game in {attempts} attempts! 🎉 "
            "Want to play again? Type 'let's play a game'."
        )

    if mode == "help_followup":
        session.pop("mode", None)
        return (
            f"Got it! You need help with: {message}. "
            "Tell me a little more so I can try to help."
        )

    if mode == "feeling_followup":
        session.pop("mode", None)
        return (
            f"I hear you. You said: {message}. "
            "Want to tell me a little more about it?"
        )

    if message_lower in ["good morning", "good morning"]:
        category = "good_morning"
    elif message_lower == "good afternoon":
        category = "good_afternoon"
    elif message_lower == "good night":
        category = "good_night"
    else:
        new_message = vectorizer.transform([message])
        category = ai.predict(new_message)[0]
    

    if category == "good_morning":
        return "Good morning! Ready to code today?"

    elif category == "good_afternoon":
        return "Good afternoon! What's up?"

    elif category == "good_night":
        return "Good night! Are you ready to code tomorrow?"

    elif category == "greeting":
        return random.choice([
            "What's up?",
            "Hey, how's it going?",
            "What's on your mind?"
        ])

    elif category == "goodbye":
        return "See you later!"

    elif category == "thanks":
        return "No problem!"

    elif category == "joke":
        jokes = [
            ("Why don't skeletons fight each other?",
             "they don't have the guts"),
            ("Why did the math book look so mad?",
             "because it had too many problems"),
            ("Why can't your nose be 12 inches long?",
             "then it would be a foot"),
            ("What do you call a bear with no teeth?",
             "a gummy bear")
        ]

        question, correct_answer = random.choice(jokes)
        session["mode"] = "joke_answer"
        session["joke_answer"] = correct_answer
        return question + " Guess the answer!"

    elif category == "story":
        session["mode"] = "story_choice"
        return "Do you want a spooky story? Type yes or no."

    elif category == "game":
        session["mode"] = "game_choice"
        return (
            "What game would you like to play? "
            "I have a guessing game! Type 'guessing game'."
        )

    elif category == "help":
        session["mode"] = "help_followup"
        return "I'm happy to help! What do you need help with?"

    elif category == "feeling":
        session["mode"] = "feeling_followup"
        return "Why? Want to tell me what's going on?"

    elif category == "confused":
        return "No worries! What part should I explain differently?"

    elif category == "idea":
        return "Here's an idea: build a small game in Python!"

    elif category == "command":
        return "Sure! Let's try again. What would you like to do?"

    elif category == "reaction":
        return random.choice([
            "Thanks!",
            "Glad you think so!",
            "Awesome!"
        ])

    if "your name" in message_lower or "who are you" in message_lower:
        return "I'm your AI chatbot, built with Python and Flask!"

    if "what is python" in message_lower:
        return "Python is a programming language used to build websites, games, and AI."

    if "what is an ai" in message_lower or "what is ai" in message_lower:
        return "AI stands for artificial intelligence. I'm a simple chatbot that uses machine learning!"

    if "what can you do" in message_lower:
        return "I can chat, tell jokes and stories, and play a guessing game!"

    return "I'm still learning how to respond to that. Check for typos and try again!"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({"reply": "Please send a text message."}), 400

    message = message.strip()

    if not message:
        return jsonify({"reply": "Please type a message."}), 400

    if len(message) > 1000:
        return jsonify({
            "reply": "That message is too long. Please keep it under 1,000 characters."
        }), 400

    try:
        reply = get_bot_reply(message)
        return jsonify({"reply": reply})
    except Exception:
        app.logger.exception("Error processing chatbot message")
        return jsonify({
            "reply": "Something went wrong. Please try again."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
