import streamlit as st
from PIL import Image

nombre_app = "DiabeScan"

st.set_page_config(page_title=f'{nombre_app}', page_icon="deploy/colibri_celeste.jpeg")

st.title(f'Bienvenidos a {nombre_app}')

img = Image.open("deploy/colibri_celeste.jpeg")
st.image(img,use_container_width=False, width=500)
#st.markdown(f"<h2 style='text-align: center'> Un futuro sin diabetes es posible </h3>", unsafe_allow_html=True)
st.markdown(f"<h2> Un futuro sin diabetes es posible </h2>", unsafe_allow_html=True)

