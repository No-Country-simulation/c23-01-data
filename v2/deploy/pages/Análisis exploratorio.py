import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image


nombre_app = "DiabeScan"
st.set_page_config(page_title=f'{nombre_app}', page_icon="deploy/colibri_celeste.jpeg", layout='wide') #page_icon: puede ser un emoticon, una imagen..
#st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)

df = pd.read_csv('v2/Data/diabetes_renamed.csv')
df_cat = pd.read_csv('v2/Data/diabetes_cat.csv')

### Define dictionaries: they will be useful later

binary_dict = {0:'No',1:'Yes'} ### Dictionary for binary variables
diagnose_dict = {0:'Non-diabetic',1:'Diabetic'} ### Dictionary for the diabetes_status
sex_dict = {0:'Female',1:'Male' }### Sex Dictionary
general_health_dict = {1:'Excellent',2:'Very good',3:'Good',4:'Fair',5:'Poor'} ### General Health Dictionary
age_dict = {1:'18-24', 2:'25-29', 3:'30-34', 4:'35-39', 5:'40-44', 6:'45-49', 7:'50-54', 8:'55-59', 9:'60-64', 10:'65-69', 11:'70-74', 12:'75-79', 13:'above 80'}
education_dict = {1:"Kindergarten",2:"Elementary",3:"Some high school",4:"High school graduate",5:"Some college/tecnical school",6:"College graduate"} ### Education
income_dict = {1:"less than 10K",2:"10-15K",3:"15-20K",4:"20-25K",5:"25-35K",6:"35-50K",7:"50-75K",8:"75K or above"}




def main():
    st.markdown(f"<h1 style='text-align: center'>{nombre_app} </h1>", unsafe_allow_html=True)

    st.markdown("## Diabetes: ultimo reporte de la Federación Internacional de diabetes (2021)")

    colI, colII = st.columns(2)

    with colI:
        st.markdown("### Números clave:") 
        st.markdown("###  ") 
        st.markdown("""
        <ul>
            <li style='font-size:23px;'> 1 de cada 10 habitantes en el mundo padece de diabetes </li>
            <li style='font-size:23px;'> Casi la mitad no sabe que padece diabetes </li>
            <li style='font-size:23px;'> 90 % de las personas con diabetes tienen diabetes tipo 2 </li>
            <li style='font-size:23px;'> Proyección 2045: 1 de cada 8 personas tendrá diabetes </li>
        </ul>
        """, unsafe_allow_html=True)

    with colII: 
        st.markdown("### Una visión global:")  
        img = Image.open("v2/deploy/IDF_map.webp")
        st.image(img,use_container_width=True)
        st.text("Fuente: Federación Internacional de diabetes")


    st.markdown("## Nuestro estudio: encuestas de la CDC (Estados Unidos) del año 2015")



    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"<h3 style='text-align: center'> Total de encuestados: {len(df)} </h3>", unsafe_allow_html=True)

        #st.markdown("<h3 style='text-align: center'> Percent count </h3>", unsafe_allow_html=True)
        fig1 = px.pie(df_cat,names="Diabetes_status",color='Diabetes_status',color_discrete_map={'Non-diabetic': 'green', 'Diabetic': 'red'}, width=350, height=350)
            # Update layout for better aesthetics
        fig1.update_traces(texttemplate='%{percent:.1%}', textposition='inside')
        fig1.update_layout(
        yaxis_title="Diabetes status", 
        xaxis_title="Frequency [Count]",
        legend_title_text='Diabetes Status',
        template='plotly_white',  # Similar to seaborn's "whitegrid" style
         margin=dict(t=0, b=0, l=0, r=0),
        font=dict(
            size=20  # General font size for other text elements
        ),
        legend=dict(font=dict(size= 20)),
        legend_title=dict(font=dict(size= 22))
        )
        st.plotly_chart(fig1,use_container_width=True)
 

    #col3, col4 = st.columns(2)

    with col2:
        #st.markdown("### Distribución por sexo")
        st.markdown(f"<h3 style='text-align: center'> Distribución por sexo </h3>", unsafe_allow_html=True)

        fig2 = px.histogram(
            df_cat,
            y='Diabetes_status',
            color='Sex',
            barmode='group',
            color_discrete_map={'Female': 'hotpink', 'Male': 'blue'},
        )
        fig2.update_layout(
            xaxis_title="Frequency [Count]",
            yaxis_title="Diabetes status",
            xaxis=dict(tickfont=dict(size=16)),  # X-axis tick font size
            yaxis=dict(tickfont=dict(size=16)),  # Y-axis tick font size
            xaxis_title_font_size=20,  # X-axis title font size
            yaxis_title_font_size=20,  # Y-axis title font size
            legend=dict(font=dict(size= 20)),
            legend_title=dict(font=dict(size= 22))
        )
        st.plotly_chart(fig2,use_container_width=True)

    with col3:
        #st.markdown("### Distribución etaria")
        st.markdown(f"<h3 style='text-align: center'> Distribución etaria </h3>", unsafe_allow_html=True)

        fig3 = px.histogram(
            df_cat,
            color='Diabetes_status',
            x='Age',
            barmode='group',
            color_discrete_map={'Non-diabetic': 'green', 'Diabetic': 'red'},
        )
        fig3.update_layout(xaxis_title="Diabetes status",
                           yaxis_title="Frequency [Count]", 
                            showlegend = False,
                            xaxis=dict(tickfont=dict(size=16)),  # X-axis tick font size
                            yaxis=dict(tickfont=dict(size=16)),  # Y-axis tick font size
                            xaxis_title_font_size=20,  # X-axis title font size
                            yaxis_title_font_size=20,  # Y-axis title font size
                           )
        fig3.update_xaxes(categoryorder='array', categoryarray= list(age_dict.values()))
        st.plotly_chart(fig3,use_container_width=True)     


    cola, colb, colc = st.columns(3)

    with cola:
        #st.markdown("### Diabetes vs. IMC")   
        st.markdown(f"<h3 style='text-align: center'> Diabetes vs. IMC </h3>", unsafe_allow_html=True)

        figa = px.box(
            df_cat,
            y="BMI",
            x="Diabetes_status",
            color="Diabetes_status",
            color_discrete_sequence=['green', 'red'],
            #box=True,      # Adds a box plot inside the violin
            #points="all"   # Shows all individual points
        ) 
        figa.update_layout(xaxis_title="Diabetes status", 
                           yaxis_title="BMI", 
                           showlegend = False,
                            xaxis=dict(tickfont=dict(size=16)),  # X-axis tick font size
                            yaxis=dict(tickfont=dict(size=16)),  # Y-axis tick font size
                            xaxis_title_font_size=20,  # X-axis title font size
                            yaxis_title_font_size=20,  # Y-axis title font size
                           )
        st.plotly_chart(figa,use_container_width=True) 

    with colb:
        #st.markdown("### Diabetes vs. Salud general")
        st.markdown(f"<h3 style='text-align: center'> Diabetes vs. Salud general </h3>", unsafe_allow_html=True)
        figb = px.violin(
            df_cat,
            y="General_health",
            x="Diabetes_status",
            color="Diabetes_status",
            color_discrete_sequence=['green', 'red']
        )
        figb.update_yaxes(categoryorder='array', categoryarray= list(general_health_dict.values()))
        figb.update_layout(xaxis_title="Diabetes status", 
                           yaxis_title="General health", 
                           showlegend = False,
                            xaxis=dict(tickfont=dict(size=16)),  # X-axis tick font size
                            yaxis=dict(tickfont=dict(size=16)),  # Y-axis tick font size
                            xaxis_title_font_size=20,  # X-axis title font size
                            yaxis_title_font_size=20,  # Y-axis title font size
                           )
        st.plotly_chart(figb,use_container_width=True)

    with colc:
        #st.markdown("### Diabetes vs. Socioeconómico")
        st.markdown(f"<h3 style='text-align: center'> Diabetes vs. Socioeconómico </h3>", unsafe_allow_html=True)
        figc = px.violin(
            df_cat,
            y="Income",
            x="Diabetes_status",
            color="Diabetes_status",
            color_discrete_sequence=['green', 'red'],
        )
        figc.update_yaxes(categoryorder='array', categoryarray= list(income_dict.values()))
        figc.update_layout(xaxis_title="Diabetes status", 
                           showlegend = False,
                            xaxis=dict(tickfont=dict(size=16)),  # X-axis tick font size
                            yaxis=dict(tickfont=dict(size=16)),  # Y-axis tick font size
                            xaxis_title_font_size=20,  # X-axis title font size
                            yaxis_title_font_size=20,  # Y-axis title font size)
        )
        st.plotly_chart(figc,use_container_width=True)  

if __name__ == '__main__':
    main()