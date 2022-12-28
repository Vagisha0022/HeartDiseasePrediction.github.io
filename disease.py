import numpy as np
import pickle 
import streamlit as st
#loading the data
loaded_model =pickle.load(open('trained_model.sav','rb'))

#creating a function for prediction
def heart_prediction(input_data):
    
    #change the input data to a numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    #reshape the numpy aaray as we are predicting for onlyy one instance4
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
        return"The Person does not have a Heart Disease"
    else:
         return "The Person is having a Heart Disease"

def main():
    #giving a title
    st.title('Heart Prediction')
    #getting the input data from user
    
    age=st.text_input('Age of the person')
    sex=st.text_input('Gender of the person')
    cp=st.text_input('cp of the person')
    trestbps=st.text_input('trestbps of the person')
    chol=st.text_input('Cholestrol of the person')
    fbs=st.text_input('fbs of the person')
    restecg=st.text_input('rest ecg of the person')
    thalach=st.text_input('thalach of the person')
    exang=st.text_input('exang of the person')
    oldpeak=st.text_input('oldpeak of the person')
    slope=st.text_input('slope of the person')
    ca=st.text_input('ca of the person')
    thal=st.text_input('thal of the person')

    #code for Prediction
    diagnosis='  '

    #creating a button for Prediction
    if st.button('Heart Disease Test Result'):
       diagnosis=heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    st.success(diagnosis)

if __name__== '__main__':
    main()