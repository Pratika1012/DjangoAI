import json
import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path

# List of patient JSON file paths
patient_files = [
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient1.json',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient2.json',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient3.json',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient4.json',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient5.json',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient6.json',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient7.json',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient8.json',
    
]

openai.api_key = "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"

memory = []  # Initialize an empty memory list
currentPatientIndex = 0

def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def load_current_patient(ind):
    # Load the current patient's JSON file
    with open(patient_files[int(ind)]) as file:
        current_patient_data = json.load(file)

    return current_patient_data

def chat_interface(request):
    
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        user_input1 = request.POST.get('currentPatientIndex1')
      

        # if user_input.lower() == "what is previous question":
        #     if len(memory) > 0:
        #         previous_question = memory.pop()
        #         response = "Chatbot: Previous question: " + previous_question
        #     else:
        #         response = "Chatbot: There is no previous question."
        # elif user_input.lower() == "what is previous to previous question":
        #     if len(memory) > 1:
        #         previous_to_previous_question = memory[-2]
        #         response = "Chatbot: Previous to previous question: " + previous_to_previous_question
        #     else:
        #         response = "Chatbot: There is no previous to previous question."
        # else:
        input_text = f"""

            Context: summarize the conditions,Therphay,Treatments,diagnosisdate,startdate,dosage,clinical summary for the patients,what was the last time They  had a visit to her doctor?
            allergies,surgeries,Lastvisitdate,medicialhistory,dateOfBirth,gender,address of patient contactnumber of patient,
            doctorname{load_current_patient(user_input1)}
            Question: {user_input}

            Answer:
            """
        
        response = generate_response(input_text)

        # Save the user's question in memory
        # memory.append(user_input)

        return JsonResponse({'response': response})

    return render(request, 'index.html')
