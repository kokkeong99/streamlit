 
import pickle
import streamlit as st
 
#Loading the prediction model
#pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(open('classifier.pkl', 'rb'))
 
@st.cache()
  
# defining the function which will make the pass prediction using the data which the user inputs 
def prediction_pass(gender, marital_status, malaysian, type_sponsor, course_code, group, max_percentage, percentage):   
 
  # Making predictions 
  prediction1 = classifier.predict( 
        [[gender, marital_status, malaysian, type_sponsor, course_code, group, max_percentage, percentage]])
     
  if prediction1 == 0:
    return 'Pass'
  elif prediction1 == 1:
    return 'at-Risk'
 
# this is the main function in which we define the webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Student Performance Predictor</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    course_code_in = st.selectbox('Course', ("SSK3100 Computer Programming I", "SSK3101 Computer Programming II", "SSK3118 Data Structures and Algorithms", "SSK3207 Computer Organization and Assembly Language", "SSK3313 Operating System",
                                             "SSK3408 Database Application Development","SSK4506 Database Security","SSK4508 Computer Forensics", "SSK4602 Intelligent Computing", "SSK4610 Knowledge Based System",
                                             "SSK3003 Discrete Structures", "SIM3251 Statistics for Computer Science", "SIM4207 Ethics in Computing", "SIM4208 Electronic Commerce", "SKM4212 Audio Visual Digitisation", 
                                             "SKR3305 Python Programming", "SKR3307 Shell Programming","SKR3504 Network Analysis and Design", "SKR4202 High Performance Computing", "SKR4307 Mobile Application", 
                                             "SSE3150 Web Application Development", "SSE4306 Software Quality","SSE4351 Software Maintenance And Evolution", "SSE4356 Secure Software Development"), 
                                             help = "The prediction model is based on courses offered in the first semester of the 2019/2020 academic year, and there may be some new courses not covered")
    
    gender_in = st.selectbox('Gender',("Female","Male"))
    marital_status_in = st.selectbox('Marital Status',("Single","Married","Widow"))
    malaysian_in = st.selectbox('Malaysian',("Yes", "No")) 
    type_sponsor_in = st.selectbox('Type of Sponsor',("No","Loan","Scholarship")) 
    
    #Specific the group number according to the dataset
    if course_code_in == "SKM4212 Audio Visual Digitisation":
      max_group = 2
    elif course_code_in == "SSE4306 Software Quality":
      max_group = 2
    elif course_code_in == "SSE4351 Software Maintenance And Evolution":
      max_group = 2
    elif course_code_in == "SSK3118 Data Structures and Algorithms":
      max_group = 2
    elif course_code_in == "SKR4307 Mobile Application":
      max_group = 3
    elif course_code_in == "SSK3313 Operating System":
      max_group = 4
    elif course_code_in == "SSK3408 Database Application Development":
      max_group = 6
    elif course_code_in == "SSK3100 Computer Programming I":
      max_group = 7
    elif course_code_in == "SSK3003 Discrete Structures":
      max_group = 8
    else:
      max_group = 1

    group = st.number_input('Group', min_value = 1, max_value = int(max_group), value = 1, step = 1, help = "Please refer to the group for the first semester of the 2019/2020 academic year")
    max_percentage_in = st.number_input('Full Mark for Test 1 ', min_value = 5, max_value = 20, value = 20, step = 5)
    percentage_in = st.number_input('Test 1 Mark', min_value = 0.0, max_value = float(max_percentage_in), value = 0.0, step = 0.1)

    # Pre-processing user input    
    if gender_in == "Female":
      gender = 0
    elif gender_in == "Male":
      gender = 1

    if marital_status_in == "Married":
      marital_status = 0
    elif marital_status_in == "Single":
      marital_status = 1
    elif marital_status_in == "Widow":
      marital_status = 2

    if malaysian_in == "No":
      malaysian = 0
    elif malaysian_in == "Yes":
      malaysian = 1

    if type_sponsor_in == "Scholarship":
      type_sponsor = 0
    elif type_sponsor_in == "Loan":
      type_sponsor = 1
    elif type_sponsor_in == "No":
      type_sponsor = 2 
 
    if course_code_in == "SIM3251 Statistics for Computer Science":
      course_code = 0
    elif course_code_in == "SIM4207 Ethics in Computing":
      course_code = 1
    elif course_code_in == "SIM4208 Electronic Commerce":
      course_code = 2
    elif course_code_in == "SKM4212 Audio Visual Digitisation":
      course_code = 3
    elif course_code_in == "SKR3305 Python Programming":
      course_code = 4      
    elif course_code_in == "SKR3307 Shell Programming":
      course_code = 5
    elif course_code_in == "SKR3504 Network Analysis and Design":
      course_code = 6 
    elif course_code_in == "SKR4202 High Performance Computing":
      course_code = 7 
    elif course_code_in == "SKR4307 Mobile Application":
      course_code = 8 
    elif course_code_in == "SSE3150 Web Application Development":
      course_code = 9 
    elif course_code_in == "SSE4306 Software Quality":
      course_code = 10 
    elif course_code_in == "SSE4351 Software Maintenance And Evolution":
      course_code = 11 
    elif course_code_in == "SSE4356 Secure Software Development":
      course_code = 12 
    elif course_code_in == "SSK3003 Discrete Structures":
      course_code = 13 
    elif course_code_in == "SSK3100 Computer Programming I":
      course_code = 14
    elif course_code_in == "SSK3101 Computer Programming II":
      course_code = 15 
    elif course_code_in == "SSK3118 Data Structures and Algorithms":
      course_code = 16 
    elif course_code_in == "SSK3207 Computer Organization and Assembly Language":
      course_code = 17 
    elif course_code_in == "SSK3313 Operating System":
      course_code = 18 
    elif course_code_in == "SSK3408 Database Application Development":
      course_code = 19 
    elif course_code_in == "SSK4506 Database Security":
      course_code = 20 
    elif course_code_in == "SSK4508 Computer Forensics":
      course_code = 21 
    elif course_code_in == "SSK4602 Intelligent Computing":
      course_code = 22 
    elif course_code_in == "SSK4610 Knowledge Based System":
      course_code = 23 

    if max_percentage_in == 5:
      max_percentage = 0
    elif max_percentage_in == 10:
      max_percentage = 1
    elif max_percentage_in == 15:
      max_percentage = 2
    elif max_percentage_in == 20:
      max_percentage = 3
    
    #Calculate the percentage of test 1
    percentage = percentage_in / max_percentage_in

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction_pass(gender, marital_status, malaysian, type_sponsor, course_code, group, max_percentage, percentage) 
        
        #Display the output
        if result == 'Pass':
          st.success('Prediction result for this course is {} (Performance Accuracy: 93.24%)'.format(result))
        elif result == 'at-Risk':
          st.error('Prediction result for this course is {} (Grade = C-, D+, D or F) Performance Accuracy: 93.24%'.format(result))
     
if __name__=='__main__': 
    main()
