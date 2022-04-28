from model.EvalAnteproy import EvaluacionAnteproyecto

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""

def agregar_evaluacion(st, controller):
    st.title("Registro De Estudiante")
    # Objecto que modelará el formulario
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Nombre Estudiante")
    evaluacion_obj.id_estudiante = st.text_input("Id Estudiante")
    evaluacion_obj.tema_proyecto = st.text_input("Tema Proyecto")
    evaluacion_obj.version_doc = st.text_input("Version Documento")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
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
        col1, col2, col3, col4 = st.columns(4)
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
