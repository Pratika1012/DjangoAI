## versions

Name: Django
Version: 4.2.2

Name: sqlparse
Version: 0.4.4

Name: asgiref
Version: 3.7.2

Name: tzdata
Version: 2023.3

We have use Html file for django application

Index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Web Interface</title>
    <!-- Include Bootstrap CSS -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.2.0/css/bootstrap.min.css"
    />
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }

    .container {
      max-width: 8000px;
      margin: 0 auto;
    }

    .form-group {
      margin-bottom: 20px;
    }

    label {
      display: block;
      margin-bottom: 5px;
    }
h3{
  margin-left:200px;
}
    .patient-details-container {
    
      padding: 20px;
      border-radius: 5px;
    }

    .patient-details-container h3 {
      margin-top: 0;
    }

    .patient-details-container p {
      margin-bottom: 10px;
    }

    .patient-details-container ul {
      margin: 0;
      padding-left: 20px;
      list-style-type: square;
    }
    .chat-container {
      height: 300px;
      overflow-y:scroll;
    }
    
    .chat-messages {
      padding-right: 10px; 
    }
    .custom-select {
      width: 20%;
    }
  </style>
</head>
  <body>
    <div class="form-group">
      <h2><center>DEMO</h2></center>
      <label for="patientSelect">Select Patient:</label>
      <select class="form-control custom-select" id="patientSelect">
        
        <option value="John Doe">John Doe</option>
        <option value="Jane Smith">Jane Smith</option>
        <option value="Sarah Williams">Sarah Williams</option>
        <option value="Michael Johnson">Michael Johnson</option>
        <option value="Emily Davis">Emily Davis</option>
        <option value="Michaela Thompson">Michaela Thompson</option>
        <option value="Olivia Anderson">Olivia Anderson</option>
        <option value="Daniel Wilson">Daniel Wilson</option>
      </select>
    </div>
    </div>
    <div class="container">
      <div class="row">
        <h3>Patient Details</h3>
        <div class="col-md-4 patient-details-container">
          
          <p><strong>Patient ID:</strong> <span id="patientId"></span></p>
          <p><strong>Name:</strong> <span id="name"></span></p>
          <p><strong>Date of Birth:</strong> <span id="dateOfBirth"></span></p>
          <p><strong>Gender:</strong> <span id="gender"></span></p>
          <p>
            <strong>Contact Number:</strong> <span id="contactNumber"></span>
          </p>
          <p><strong>Address:</strong> <span id="address"></span></p>
          <br>
          <h5>Medical History</h5>
          <ul>
          <li><strong>Allergies:</strong> <span id="allergies"></span></li>
          <li><strong>Surgeries:</strong> <span id="surgeries"></span></li>
          </ul>
          <br>
          <h5>Family History</h5>
          <ul>
          <li><strong>Conditions:</strong> <span id="conditions"></span></li>
          <li>
            <strong>Family Members:</strong> <span id="familyMembers"></span>
          </li>
        </ul>
          <br>
          <p><strong>Last visite Date:</strong> <span id="Lastdate"></span></p>
          <p><strong>Doctor:</strong> <span id="Doctor"></span></p>
        </div>
        <div class="col-md-3">
          <h5><strong>Conditions:</strong> <span id="Conditions"></span></h5>
          <p><b>1. Name : </b><span id="ConditionsName"></span></p>
          <p><b>diagnosis Date : </b><span id="ConditionsDiagnosisDate"></span></p>
          <b>treatments : </b>
          <ul>
            <li><b>Name-1: </b><span id="ConditionsTreatmentsName"></span></li>
            <li><b>startDate : </b><span id="ConditionsStartDate"></span></li>
            <li><b>Dosage : </b><span id="ConditionsDosage"></span></li>
          </ul>
          <ul>
            <li><b>Name-2: </b><span id="ConditionsTreatmentsName11"></span></li>
            <li><b>startDate : </b><span id="ConditionsStartDate11"></span></li>
            <li><b>Dosage : </b><span id="ConditionsDosage11"></span></li>
          </ul>

          <p><b>2.Name : </b><span id="ConditionsName1"></span></p>
          <p>
            <b>diagnosis Date : </b><span id="ConditionsDiagnosisDate1"></span>
          </p>
          <b>treatments : </b>
          <ul>
            <li><b>Name-1 : </b><span id="ConditionsTreatmentsName1"></span></li>
            <li><b>startDate : </b><span id="ConditionsStartDate1"></span></li>
            <li><b>Dosage : </b><span id="ConditionsDosage1"></span></li>
          </ul>
          <ul>
            <li><b>Name-2 : </b><span id="ConditionsTreatmentsName22"></span></li>
            <li><b>startDate : </b><span id="ConditionsStartDate22"></span></li>
            <li><b>Dosage : </b><span id="ConditionsDosage22"></span></li>
          </ul>
          
        </div>
        <div class="col-md-5">
          <h3>Chat Interface</h3>
          <div class="card mt-4">
            <div class="card-header"></div>
            <div class="card-body chat-container">
              <div class="chat-messages">
                <!-- Chat messages go here -->
              </div>
            </div>
          </div>
          <form id="chat-form">
            <div class="input-group mt-3">
              <input
                type="text"
                class="form-control"
                id="message-input"
                placeholder="Type your message..."
              />
              <button type="submit" class="btn btn-primary" id="Send-btn">Send</button>
            </div>
          </form>
        </div>
      </div>

    <!-- Include Bootstrap JS and jQuery -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.2.0/js/bootstrap.bundle.min.js"></script>

    <script>
        $(document).ready(function() {
        
          var currentPatient = null;
          var patient=[]
        
            var csrftoken = $('[name=csrfmiddlewaretoken]').val();
            $('#chat-form').submit(function(event) {
                event.preventDefault();
                var messageInput = $('#message-input');
                var message = messageInput.val().trim();

                if (message !== '') {
                    // Display user question in the chat card body
                    var chatBody = $('.card-body');
                    
                    var userQuestion = '<strong>User:</strong> ' + message + '<br>';
                    chatBody.append(userQuestion);

                    // Clear the input field
                     messageInput.val('');
                    console.log(message)
                    // Call the Chatbot API with the user's question
                    // callChatbotAPI(message,currentPatientIndex);
                }
            });
    
      
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            function clearChatResponses() {
              $('.card-body .chatbot-response').remove();
        
          }
          function clearChatHistory() {
            $('.card-body').empty();
          }
          function loadPatientDetails() {
            clearChatHistory();
            clearChatResponses();
          
            if (currentPatientIndex < patients.length) {
              currentPatient = patients[currentPatientIndex];
              displayPatientDetails(currentPatient);
              console.log(currentPatient);
            }
          }
          
          $('#next-btn').click(function() {
            console.log('Next button clicked');
            if (currentPatientIndex < patients.length - 1) {
                currentPatientIndex++;
               
                loadPatientDetails();
                
            }
        });
        $('#Send-btn').click(function() {
          console.log('Send button clicked');
          var question = $('#message-input').val();
          if (question.trim() !== '') {
            var patientIndex = currentPatientIndex; // Store the current patient index
            {% comment %} console.log(question)
            console.log(currentPatientIndex) {% endcomment %}
            callChatbotAPI(question,currentPatientIndex);
          }
        });

        $(document).ready(function() {
          $('#patientSelect').change(function() {
            var selectedPatient = $(this).val();
            var patient = patients.find(function(patient) {
              return patient.name === selectedPatient;
            });
        
            if (patient) {
              clearChatHistory();
             clearChatResponses();
              currentPatientIndex=patients.indexOf(patient)
             
              displayPatientDetails(patient);
            }
           
            });
        });





    
            function callChatbotAPI(question,currentPatientIndex) {
              console.log(currentPatientIndex)
             
                var csrfToken = getCookie('csrftoken');
                
                var patient = patients[currentPatientIndex];
                
                if (currentPatientIndex < patients.length) {
                    
                $.ajax({
                    type: "POST",
                    url: '/chat-interface/',
                    headers: {
                         'X-CSRFToken': csrfToken
                     },
                    data: {
                       // Include a unique identifier for the patient
                      user_input: question,
                      currentPatientIndex1:currentPatientIndex
                  },
                    success: function(response) {
                      
                      clearChatResponses();
                      currentPatient = patients[currentPatientIndex];

                        // Display the chatbot's response in the chat card body
                        var chatBody = $('.card-body');
                        var chatQuestion = '<p class="card-text">' + question + '</p>';
                        var chatResponse = '<p class="card-text">' + response.response + '</p>';
                       
                        chatBody.append(chatResponse);
                        
                         
                      },
                    error: function(err) {
                        console.log(err)
                        var errorMessage = '<p class="card-text">An error occurred while processing the request.</p>';
                        $('.card-body').append(errorMessage);
                    }
                });
            }
          }
        });
        
    </script>
    </script>
</script>
<script>
  
      var patients = [
        {
          patientId: "123456789",
          name: "John Doe",
          dateOfBirth: "1980-01-01",
          gender: "Male",
          contactNumber: "+1 (123) 456-7890",
          address: "123 Main Street, City, State, ZIP",
          medicalHistory: {
            allergies: ["Penicillin", "Peanuts"],
            surgeries: ["Appendectomy", "Knee arthroscopy"],
            familyHistory: {
              conditions: ["Diabetes", "Hypertension"],
              familyMembers: ["Mother", "Father"],
            },
          },
          Conditions: [
            {
              name: "Diabetes",
              diagnosisDate: "2010-05-15",
              treatments: [
                {
                  name: "Insulin therapy",
                  startDate: "2010-05-20",
                  dosage: "10 units/day",
                },
                {
                  name: "Dietary changes",
                  startDate: "2010-05-15",
                },
              ],
            },
            {
              name: "Hypertension",
              diagnosisDate: "2015-02-10",
              treatments: [
                {
                  name: "Antihypertensive medication",
                  startDate: "2015-02-15",
                  dosage: "10 mg/day",
                },
                {
                  name: "Exercise regimen",
                  startDate: "2015-02-15",
                },
              ],
            },
          ],
          lastVisitDate: "2023-05-30",
          doctor: "Dr. Jane Smith",
        },

        {
          patientId: "987654321",
          name: "Jane Smith",
          dateOfBirth: "1992-07-15",
          gender: "Female",
          contactNumber: "+1 (987) 654-3210",
          address: "456 Oak Street, City, State, ZIP",
          medicalHistory: {
            allergies: ["Sulfa drugs"],
            surgeries: ["Gallbladder removal"],
            familyHistory: {
              conditions: ["Heart disease", "Breast cancer"],
              familyMembers: ["Grandmother", "Sister"],
            },
          },
          Conditions: [
            {
              name: "Asthma",
              diagnosisDate: "2005-10-20",
              treatments: [
                {
                  name: "Inhaler",
                  startDate: "2005-10-20",
                  dosage: "2 puffs/day",
                },
                {
                  name: "Allergy testing",
                  startDate: "2005-10-25",
                },
              ],
            },
            {
              name: "Anxiety",
              diagnosisDate: "2012-03-12",
              treatments: [
                {
                  name: "Cognitive Behavioral Therapy",
                  startDate: "2012-03-15",
                },
              ],
            },
          ],
          lastVisitDate: "2023-06-01",
          doctor: "Dr. Mark Johnson",
        },

        {
          patientId: "246813579",
          name: "Sarah Williams",
          dateOfBirth: "1975-12-03",
          gender: "Female",
          contactNumber: "+1 (555) 123-4567",
          address: "789 Elm Street, City, State, ZIP",
          medicalHistory: {
            allergies: ["Shellfish", "Latex"],
            surgeries: ["Hip replacement"],
            familyHistory: {
              conditions: ["Cancer", "Alzheimer's"],
              familyMembers: ["Father", "Maternal aunt"],
            },
          },
          Conditions: [
            {
              name: "Osteoarthritis",
              diagnosisDate: "2010-08-18",
              treatments: [
                {
                  name: "Physical therapy",
                  startDate: "2010-08-20",
                },
                {
                  name: "Pain medication",
                  startDate: "2010-08-18",
                  dosage: "As needed",
                },
              ],
            },
            {
              name: "Depression",
              diagnosisDate: "2015-06-07",
              treatments: [
                {
                  name: "Selective Serotonin Reuptake Inhibitors (SSRIs)",
                  startDate: "2015-06-10",
                },
                {
                  name: "Therapy sessions",
                  startDate: "2015-06-07",
                },
              ],
            },
          ],
          lastVisitDate: "2023-05-28",
          doctor: "Dr. Emily Thompson",
        },

        {
          patientId: "135792468",
          name: "Michael Johnson",
          dateOfBirth: "1985-03-10",
          gender: "Male",
          contactNumber: "+1 (555) 987-6543",
          address: "789 Maple Avenue, City, State, ZIP",
          medicalHistory: {
            allergies: ["Pollen", "Eggs"],
            surgeries: ["ACL reconstruction"],
            familyHistory: {
              conditions: ["Stroke", "Obesity"],
              familyMembers: ["Grandfather", "Brother"],
            },
          },
          Conditions: [
            {
              name: "Type 2 Diabetes",
              diagnosisDate: "2010-12-05",
              treatments: [
                {
                  name: "Oral medication",
                  startDate: "2010-12-10",
                  dosage: "1000 mg/day",
                },
                {
                  name: "Lifestyle changes",
                  startDate: "2010-12-05",
                },
              ],
            },
            {
              name: "High Cholesterol",
              diagnosisDate: "2015-08-22",
              treatments: [
                {
                  name: "Statins",
                  startDate: "2015-08-25",
                  dosage: "20 mg/day",
                },
                {
                  name: "Dietary changes",
                  startDate: "2015-08-22",
                },
              ],
            },
          ],
          lastVisitDate: "2023-06-03",
          doctor: "Dr. David Roberts",
        },

        {
          patientId: "864209753",
          name: "Emily Davis",
          dateOfBirth: "1990-09-25",
          gender: "Female",
          contactNumber: "+1 (555) 246-8102",
          address: "987 Pine Street, City, State, ZIP",
          medicalHistory: {
            allergies: ["Dust mites", "Mold"],
            surgeries: ["Tonsillectomy"],
            familyHistory: {
              conditions: ["Rheumatoid Arthritis", "Colon cancer"],
              familyMembers: ["Mother", "Maternal uncle"],
            },
          },
          Conditions: [
            {
              name: "Migraine",
              diagnosisDate: "2008-06-15",
              treatments: [
                {
                  name: "Triptans",
                  startDate: "2008-06-20",
                  dosage: "As needed",
                },
                {
                  name: "Identifying triggers",
                  startDate: "2008-06-15",
                },
              ],
            },
            {
              name: "Endometriosis",
              diagnosisDate: "2014-03-10",
              treatments: [
                {
                  name: "Birth control pills",
                  startDate: "2014-03-15",
                },
                {
                  name: "Pain medication",
                  startDate: "2014-03-10",
                  dosage: "As needed",
                },
              ],
            },
          ],
          lastVisitDate: "2023-05-29",
          doctor: "Dr. Sarah Anderson",
        },
        {
          patientId: "987654321",
          name: "Michaela Thompson",
          dateOfBirth: "1978-06-12",
          gender: "Female",
          contactNumber: "+1 (555) 123-4567",
          address: "123 Elm Street, City, State, ZIP",
          medicalHistory: {
            allergies: ["Bee stings", "Shellfish"],
            surgeries: ["Gallbladder removal"],
            familyHistory: {
              conditions: ["Heart disease", "Breast cancer"],
              familyMembers: ["Mother", "Sister"],
            },
          },
          Conditions: [
            {
              name: "Hypothyroidism",
              diagnosisDate: "2002-04-15",
              treatments: [
                {
                  name: "Synthetic thyroid hormone",
                  startDate: "2002-04-20",
                  dosage: "50 mcg/day",
                },
                {
                  name: "Regular blood tests",
                  startDate: "2002-04-15",
                },
              ],
            },
            {
              name: "Depression",
              diagnosisDate: "2010-07-10",
              treatments: [
                {
                  name: "Selective Serotonin Reuptake Inhibitors (SSRIs)",
                  startDate: "2010-07-15",
                },
                {
                  name: "Therapy sessions",
                  startDate: "2010-07-10",
                },
              ],
            },
          ],
          lastVisitDate: "2023-06-01",
          doctor: "Dr. Robert Wilson",
        },

        {
          patientId: "123456789",
          name: "Olivia Anderson",
          dateOfBirth: "1995-11-28",
          gender: "Female",
          contactNumber: "+1 (555) 987-6543",
          address: "456 Oak Street, City, State, ZIP",
          medicalHistory: {
            allergies: ["Peanuts", "Dogs"],
            surgeries: ["Appendectomy"],
            familyHistory: {
              conditions: ["Diabetes", "Hypertension"],
              familyMembers: ["Mother", "Father"],
            },
          },
          Conditions: [
            {
              name: "Asthma",
              diagnosisDate: "2003-08-12",
              treatments: [
                {
                  name: "Inhaler",
                  startDate: "2003-08-15",
                  dosage: "2 puffs/day",
                },
                {
                  name: "Allergy testing",
                  startDate: "2003-08-12",
                },
              ],
            },
            {
              name: "Anxiety",
              diagnosisDate: "2012-01-05",
              treatments: [
                {
                  name: "Cognitive Behavioral Therapy",
                  startDate: "2012-01-10",
                },
              ],
            },
          ],
          lastVisitDate: "2023-06-03",
          doctor: "Dr. Lisa Davis",
        },

        {
          patientId: "246813579",
          name: "Daniel Wilson",
          dateOfBirth: "1982-04-20",
          gender: "Male",
          contactNumber: "+1 (555) 234-5678",
          address: "789 Maple Avenue, City, State, ZIP",
          medicalHistory: {
            allergies: ["Pollen", "Cats"],
            surgeries: ["Knee replacement"],
            familyHistory: {
              conditions: ["Cancer", "Alzheimer's"],
              familyMembers: ["Father", "Maternal aunt"],
            },
          },
          Conditions: [
            {
              name: "Osteoarthritis",
              diagnosisDate: "2007-10-15",
              treatments: [
                {
                  name: "Physical therapy",
                  startDate: "2007-10-20",
                },
                {
                  name: "Pain medication",
                  startDate: "2007-10-15",
                  dosage: "As needed",
                },
              ],
            },
            {
              name: "Depression",
              diagnosisDate: "2014-05-10",
              treatments: [
                {
                  name: "Selective Serotonin Reuptake Inhibitors (SSRIs)",
                  startDate: "2014-05-15",
                },
                {
                  name: "Therapy sessions",
                  startDate: "2014-05-10",
                },
              ],
            },
          ],
          lastVisitDate: "2023-05-31",
          doctor: "Dr. Jessica Thompson",
        },
      ];
    
    

    



     
      function displayPatientDetails(patient) {
       
        $("#patientId").text(patient.patientId);
        $("#name").text(patient.name);
        $("#dateOfBirth").text(patient.dateOfBirth);
        $("#gender").text(patient.gender);
        $("#contactNumber").text(patient.contactNumber);
        $("#address").text(patient.address);
        $("#allergies").text(patient.medicalHistory.allergies);
        $("#surgeries").text(patient.medicalHistory.surgeries);
        $("#conditions").text(patient.medicalHistory.familyHistory.conditions);
        $("#familyMembers").text(patient.medicalHistory.familyHistory.familyMembers);
        $("#ConditionsName").text(patient.Conditions[0].name);
        $("#ConditionsName1").text(patient.Conditions[1].name);
        $("#Lastdate").text(patient.lastVisitDate);
        $("#Doctor").text(patient.doctor);
        $("#ConditionsDiagnosisDate").text(patient.Conditions[0].diagnosisDate);

        $("#ConditionsTreatmentsName").text(
          patient.Conditions[0].treatments[0].name
        );

        $("#ConditionsStartDate").text(
          patient.Conditions[0].treatments[0].startDate
        );
        $("#ConditionsDosage").text(
          patient.Conditions[0].treatments[0].dosage || "Not Available"
        );

        $("#ConditionsTreatmentsName11").text(
          patient.Conditions[0].treatments[1].name
        );
        $("#ConditionsStartDate11").text(
          patient.Conditions[0].treatments[1].startDate
        );
        $("#ConditionsDosage11").text(
          patient.Conditions[0].treatments[1].dosage
        );

        $("#ConditionsDiagnosisDate1").text(
          patient.Conditions[1].diagnosisDate
        );

        $("#ConditionsTreatmentsName1").text(
          patient.Conditions[1].treatments[0].name
        );
        $("#ConditionsStartDate1").text(
          patient.Conditions[1].treatments[0].startDate
        );
        $("#ConditionsDosage1").text(
          patient.Conditions[1].treatments[0].dosage
        );

        $("#ConditionsTreatmentsName22").text(
          patient.Conditions[1].treatments[1].name
        );
        $("#ConditionsStartDate22").text(
          patient.Conditions[1].treatments[1].startDate
        );
        $("#ConditionsDosage22").text(
          patient.Conditions[1].treatments[1].dosage
        );
        
      }
      
      var currentPatientIndex = 0; 

      function loadPatientDetails() {
        var patient = patients[currentPatientIndex]; 
        displayPatientDetails(patient);
      }
      
      loadPatientDetails();

     


      // Next button click event
      // Next button click event


      // Previous button click event
      $("#previous-btn").click(function () {
        if (currentPatientIndex > 0) {
          currentPatientIndex--;
          loadPatientDetails();
         
        }
      });
    </script>
  </body>
</html>
"""



