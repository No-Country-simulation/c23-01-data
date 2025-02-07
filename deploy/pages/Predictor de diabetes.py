import streamlit as st
import joblib
import numpy as np
import pandas as pd

#load trained model
model = joblib.load("trained_model.pkl")

### Define dictionaries: they will be useful later (here in spanish)
binary_dict = {0:'No',1:'Si'} ### Dictionary for binary variables
diagnose_dict = {0:'Non-diabetic',1:'Diabetic'} ### Dictionary for the diabetes_status
sex_dict = {0:'Female',1:'Male' }### Sex Dictionary
general_health_dict = {1:'Excelente',2:'Muy buena',3:'Buena',4:'Regular',5:'Pobre'} ### General Health Dictionary
age_dict = {1:'18-24', 2:'25-29', 3:'30-34', 4:'35-39', 5:'40-44', 6:'45-49', 7:'50-54', 8:'55-59', 9:'60-64', 10:'65-69', 11:'70-74', 12:'75-79', 13:'80 o más'} ### Age dictionary
#education_dict = {1:"Kindergarten",2:"Elementary",3:"Some high school",4:"High school graduate",5:"Some college/tecnical school",6:"College graduate"} ### Education
income_dict = {1:"menos de 10K",2:"10-15K",3:"15-20K",4:"20-25K",5:"25-35K",6:"35-50K",7:"50-75K",8:"75K o más"}


nombre_app = "DiabetiScan"
st.set_page_config(page_title=f'{nombre_app}', page_icon="deploy/colibri_celeste.jpeg")

st.title("Predictor de diabetes")

st.markdown("## Ingrese los datos del paciente:")

#input features

# Input height and weight -> Needed for the BMI
height = st.number_input("Ingrese la estatura del paciente en metros:", 1.50, 2.00, step=0.01)
weight = st.number_input("Ingrese el peso del paciente en Kilogramos:", 1, 160, step=1)

#Compute BMI
BMI = round(weight/(height)**2)

# Input age
Age = st.radio("Seleccione el grupo de edad del paciente:",
                  [1,2,3,4,5,6,7,8,9,10,11,12,13],format_func=lambda x: age_dict.get(x),
                  index=None
                  )
#st.write(Age)

# Input age
Income = st.radio("Seleccione el salario anual del paciente (en dólares):",
                  [1,2,3,4,5,6,7,8], format_func=lambda x: income_dict.get(x),
                  index=None
                  )

# Input your general health
General_health = st.radio("¿Cómo esta la salud general del paciente?",
                     [1,2,3,4,5], format_func=lambda x: general_health_dict.get(x),
                     index=None
)

# Input the binary features

High_Chol = st.radio("¿tiene el paciente el colesterol alto?",
                     [0,1], format_func=lambda x: binary_dict.get(x),
                     index=None
)

High_BP = st.radio("¿sufre de presión arterial alta el paciente?",
                     [0,1], format_func=lambda x: binary_dict.get(x),
                     index=None
)

Heart_condition = st.radio("¿tiene o ha tenido problemas cardíacos el paciente?",
                     [0,1], format_func=lambda x: binary_dict.get(x),
                     index=None
)

Difficulty_walking = st.radio("¿tiene dificultades para caminar?",
                     [0,1], format_func=lambda x: binary_dict.get(x),
                     index=None
)

Physical_health = st.slider("Durante el último mes, ¿por cuántos días considera que su salud no fue buena?", min_value=0, max_value=30, value=0, step=1)

input_data = np.array([High_BP,High_Chol,BMI,Heart_condition,General_health,Physical_health,Difficulty_walking,Age,Income])

st.markdown("## Diagnostico según el modelo:")

if np.any(input_data == None) == True:
    st.warning("Debe llenar todos los items")
else:
    prediction = model.predict(input_data.reshape(1,-1))
    predicted_class = diagnose_dict[prediction[0]]
    #Display the result
    if prediction == 0:
        st.success(f"Yor are Non-diabetic")
    else:
        st.error(f"You are Diabetic")

