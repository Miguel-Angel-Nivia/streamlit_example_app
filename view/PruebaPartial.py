def probar_streamlit(st):
    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("#### Botón Anti-Estrés")
    st.button("Aplastame >:v")
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Pregunta Seria:")
        option = st.selectbox(
            'Cuanto es dos ceros y tres uno?',
            ('N.A','2031', '0031', '00111'))
        st.write('Tu Opción:', option)

    with col2:
        color = st.color_picker('Pick A Color', '#00f900')
        st.write('The current color is', color)

    with st.expander("Mi Autobiografía"):
        st.write("¡Quietos y no se resistan, quedan bajo arresto! De:")
        st.image('https://i.ytimg.com/vi/Gv_N06gd36g/mqdefault.jpg')

