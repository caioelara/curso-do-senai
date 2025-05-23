import streamlit as st 
st.sidebar.image('movida_logo.png')
st.sidebar.title('mobida-aluguel de carros')
st.sidebar.write('seja bem vindo(a)')

carros=['BMW', 'MUSTANG', 'HB20', 'FUSCA', 'CIVIC']
carro=st.sidebar.selectbox('selecione um carro', carros)
valor_do_dia=0
if carro=='BMW':
    valor_do_dia=700
elif carro=='MUSTANG':
    valor_do_dia=1000
elif carro=='HB20':
    valor_do_dia=150
elif carro=='FUSCA':
    valor_do_dia=200
elif carro=='CIVIC':
    valor_do_dia=200
else:
    valor_do_dia=100
#---------------------------------------------
st.title('movida-aluguel de carros')
st.write('seja bem vindo(a)')
st.image(f'{carro}.png')

dias=st.text_input('quantos dias foi utilizado: ')
km=st.text_input('quantos km voce rodou:')
if st.button('calcule'):
    dias=int(dias)
    km=float(km)
    valor_dias=dias*valor_do_dia
    valor_km=km*0.15
    st.warning(f'voce rodou {km}km e usou por {dias}dias.E o valor total:R${valor_dias+valor_km}')