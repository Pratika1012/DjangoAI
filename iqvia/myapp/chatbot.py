# chat_bot.py
import json
import openai

with open(r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient1.json') as file:
    data = json.load(file)

openai.api_key = "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"

chat_history = []  # Store chat history

def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def chatbot_response(user_input, context):
    if user_input.lower() == "what is previous question":
        if len(chat_history) > 0:
            previous_question = chat_history[-1]["user_input"]
            return f"Previous question: {previous_question}"
        else:
            return "There is no previous question."
    elif user_input.lower() == "what is previous to previous question":
        if len(chat_history) > 1:
            previous_to_previous_question = chat_history[-2]["user_input"]
            return f"Previous to previous question: {previous_to_previous_question}"
        else:
            return "There is no previous to previous question."

    input_text = f"""
    Context: {context}
    Question: {user_input}

    Answer: 
    """

    response = generate_response(input_text)

    # Store current user input and chatbot response in chat history
    chat_history.append({"user_input": user_input, "response": response})

    return chat_history