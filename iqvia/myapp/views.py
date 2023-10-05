import json
import openai
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.urls import path
import pdfplumber



# List of patient JSON file paths
patient_files = [
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient1.pdf',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient2.pdf',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient3.pdf',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient4.pdf',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient5 (1).pdf',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient6.pdf',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient7.pdf',
    r'C:\Users\HP\Desktop\django\iqvia\myapp\data\Patient8 (1).pdf',
    
]

# openai.api_key

memory = []  # Initialize an empty memory list
currentPatientIndex = 0

def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=50,
        temperature=0.1,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def load_current_patient(ind):
    # Load the current patient's JSON file
    
    with pdfplumber.open(patient_files[int(ind)]) as pdf:
       text = ""
       for page in pdf.pages:
         text += page.extract_text()   
    return text



def process_api_key(request):   
    if request.method == 'POST':
        api_key = request.POST.get('api_key')
        openai.api_key=api_key
     
    
        # return HttpResponse(f"Received API Key: {api_key}")

    return render(request, 'index.html')

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
        delimited by triple quotes \
        extract the information relevant to patient detail. 
           question base on contex,give the proper answer,if require long detilts of patients condition then give proper datails step wise
            Context: what was the paitentId,dateofBirth,gender,medicalhistory,diagnosisdate Of Patient
            What medical history allergies patient surgiers,conditions,family history,Family Members have,
            Treatments name,Startdate,dosage of patient,lastVisitdate,Doctorname,address of patient,\
            answer size is maximum 200 words
            contex:{load_current_patient(user_input1)}
            
            Question: {user_input}
            

            Answer:
            """
        
        response = generate_response(input_text)

        # Save the user's question in memory
        # memory.append(user_input)

        return JsonResponse({'response': response})

    return render(request, 'index.html')
urlpatterns = [
    path('chat-interface/', chat_interface, name='chat_interface'),
    path('process_api_key/', process_api_key, name='process_api_key'),

]












