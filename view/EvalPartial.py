import datetime

from model.EvalAnteproy import EvaluacionAnteproyecto

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""

def agregar_evaluacion(st, controller):
    st.title("Registro De Estudiante")
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)
    col6, col7 = st.columns(2)
    # Objecto que modelará el formulario
    evaluacion_obj = EvaluacionAnteproyecto()
    with col1:
        evaluacion_obj.nombre = st.text_input("Nombre Estudiante")
    with col2:
        evaluacion_obj.id_estudiante = st.text_input("Id Estudiante")
    with col3:
        evaluacion_obj.tema_proyecto = st.text_input("Tema Proyecto")
    with col4:
        evaluacion_obj.version_doc = st.text_input("Version Documento")
    with col5:
        evaluacion_obj.fecha_evaluacion = st.date_input("Fecha De Evaluación", datetime.datetime(2022, 4, 28))
    st.write("#### Calificación De Criterios Del Proyecto")
    correct = st.checkbox('Fundamentos')
    evaluacion_obj.criterios = st.text_input("Criterios")
    if correct:
        st.write('Muy bien!')
    else:
        st.write('Debes Mejorar')
    with col6:
        evaluacion_obj.observaciones = st.text_area("Observaciones", "Sin Comentarios, Todo Bien En Tu Proyecto :)")
    with col7:
        evaluacion_obj.nota = st.number_input("Nota Final", 0.0, 5.0)
    enviado_btn = st.button("Enviar")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj)
        st.write("Evaluación agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def listar_evaluacion(st, controller):
    """Itera los elementos de evaluación agregados y los muestra"""
    st.title("Lista De Estudiantes")
    for evaluacion in controller.evaluaciones:
        acum = 1
        st.write("#### Estudiante #", acum)
        col1, col2, col3, col4, col5 = st.columns(5)
        col6, col7 = st.columns(2)
        with col1:
            st.write("Id Estudiante")
            st.write(evaluacion.id_estudiante)
        with col2:
            st.write("Nombre Estudiante")
            st.write(evaluacion.nombre)
        with col3:
            st.write("Tema Proyecto")
            st.write(evaluacion.tema_proyecto)
        with col4:
            st.write("Version Documento")
            st.write(evaluacion.version_doc)
        with col5:
            st.write("Fecha De Evaluación")
            st.write(evaluacion.fecha_evaluacion)
        with col6:
            st.write("Observaciones")
            st.write(evaluacion.observaciones)
        with col7:
            st.write("Nota Final")
            st.write(evaluacion.nota)
        acum += 1
