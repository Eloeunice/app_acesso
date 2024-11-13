import streamlit as st
import pandas as pd


# Carregar base de dados
def carregar_usuarios():
    return pd.read_excel('RegistroUsuarios (1).xlsx', engine='openpyxl')

# Tela de login
st.title('Controle de Acessos aos Dashboards')
email = st.text_input('Email')
senha = st.text_input('Senha', type='password')
if st.button('Login'):
    usuarios = carregar_usuarios()
    usuario = usuarios[usuarios['EMAIL'] == email]
    if not usuario.empty:
        st.session_state['usuario'] = usuario.iloc[0].to_dict()
        st.success('Login realizado com sucesso!')
        #st.experimental_rerun()
    else:
        st.error('Email ou senha inválidos.')
if 'usuario' in st.session_state:
    usuario = st.session_state['usuario']
    st.title(f'Bem-vindo, {usuario["NOME"]}!')
    st.subheader('Dashboards Disponíveis')
    dashboards = usuario['LINKS DA DASHBOARD'].split(';')
    for dashboard in dashboards:
        st.markdown(f"- [LINKS DA DASHBOARD]({dashboard})")
@st.cache_data
def carregar_usuarios():
    return pd.read_excel('usuarios_acessos.xlsx', engine='openpyxl')
