import streamlit as st
#------------------------------------------------------------saidbar
st.sidebar.title('esportes')
opcao=['jogos','noticias']
opcao=st.sidebar.selectbox('selecione umaq opcao',opcao)
#-------------------------------------------------------------principal
st.title('esportes')


tab1, tab2, tab3, tab4 = st.tabs(['FIFA', 'NBA', 'NFL', 'MBL'])

with tab1:
    if opcao == 'jogos':
        st.subheader('FIFA ')
        st.write('Paris Saint-Germain vs Internazionale 16:00')
        st.video('https://www.youtube.com/watch?v=jg4ONiRwtVU')
        st.write('Bahia vs São Paulo FC SP 18:00')
        st.video('https://www.youtube.com/watch?v=tcEGQpFDqm4')
    elif opcao == 'noticias':
        st.subheader('FIFA NOTICIAS')

with tab2:
    if opcao == 'jogos':
        st.subheader('NBA')
    elif opcao == 'noticias':
        st.subheader('NBA NOTICIAS')
    

with tab3:
    if opcao == 'jogos':
        st.subheader('NFL')
    elif opcao == 'noticias':
        st.subheader('NFL NOTICIAS')
    

with tab4:
    if opcao == 'jogos':
        st.subheader('MLB')
    elif opcao == 'noticias':
        st.subheader('MBL NOTICIAS')



