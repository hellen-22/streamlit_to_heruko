import pickle
import streamlit as st
 

pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()

  
 
def prediction(school, sex, age, address, famsize, Medu, Fedu, traveltime, studytime, famsup, activities, higher, romantic, famrel, freetime):   
 
    # Pre-processing user input    
    if school == "GP":
        school = 0
    else:
        school = 1
 
    if sex == "F":
        sex = 0
    else:
        sex = 1

    if address == "U":
        address = 0
    else:
        address = 1  

    if famsize == "GT3":
        famsize = 0
    else:
        famsize = 1 

    if famsup == "no":
        famsup = 0
    else:
        famsup = 1

    if activities == "no":
        activities = 0
    else:
        activities = 1  

    if higher == "yes":
        higher = 0
    else:
        higher = 1

    if romantic == "no":
        romantic = 0
    else:
        romantic = 1
  
    # Making predictions 
    prediction = classifier.predict( 
        [[school, sex, age, address, famsize, Medu, Fedu, traveltime, studytime, famsup, activities, higher, romantic, famrel, freetime]])
     
    if prediction == 0:
      pred = 'A'
    elif prediction == 1:
      pred = 'B'
    else:
      pred = 'C'

    return pred
      
  
 
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Student grade prediction web app</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      

    school = st.selectbox('School',("GP","MS"))
    sex = st.selectbox('Gender',("Male","Female")) 
    age = st.number_input("Age")
    address = st.selectbox('Address',("Urban","Rural")) 
    famsize = st.selectbox('Family size',("GT3", "LE3"))
    Medu =st.number_input("Mother's education")
    Fedu =st.number_input("Father's education")
    traveltime = st.number_input("traveltime")
    studytime = st.number_input("studytime")
    famsup = st.selectbox('Family support',("yes","no"))
    activities = st.selectbox('activities',("no","yes"))
    higher = st.selectbox('Higher education',("no","yes"))
    romantic = st.selectbox('Romantic relationship',("no","yes"))
    famrel = st.number_input("Familyrelationship")
    freetime = st.number_input("Free time")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(school, sex, age, address, famsize, Medu, Fedu, traveltime, studytime, famsup, activities, higher, romantic, famrel, freetime) 
        st.success('Your grade is {}'.format(result))
      
     
if __name__=='__main__': 
    main()