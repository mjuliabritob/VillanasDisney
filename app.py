import streamlit as st

st.write("Hola mundo")
import streamlit as st
import random
import time

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="👑")

# -----------------------------
# Preguntas
# -----------------------------
preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de La Sirenita?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Jafar"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana puede transformarse en dragón?",
        "opciones": ["Maléfica", "Úrsula", "Reina Malvada", "Gothel"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Quién quiere la piel de dálmatas?",
        "opciones": ["Cruella de Vil", "Lady Tremaine", "Yzma", "Madre Gothel"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Quién es la villana de Blancanieves?",
        "opciones": ["Reina Malvada", "Maléfica", "Gothel", "Úrsula"],
        "respuesta": "Reina Malvada"
    },
    {
        "pregunta": "¿Quién secuestra a Rapunzel?",
        "opciones": ["Madre Gothel", "Cruella", "Úrsula", "Yzma"],
        "respuesta": "Madre Gothel"
    },
    {
        "pregunta": "¿Qué villana usa magia con manzanas?",
        "opciones": ["Reina Malvada", "Maléfica", "Gothel", "Cruella"],
        "respuesta": "Reina Malvada"
    },
    {
        "pregunta": "¿Quién es la villana de La Cenicienta?",
        "opciones": ["Lady Tremaine", "Úrsula", "Maléfica", "Yzma"],
        "respuesta": "Lady Tremaine"
    },
    {
        "pregunta": "¿Qué villana es científica loca?",
        "opciones": ["Yzma", "Cruella", "Gothel", "Úrsula"],
        "respuesta": "Yzma"
    },
    {
        "pregunta": "¿Quién engaña a Ariel con un contrato?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Yzma"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana odia el color?",
        "opciones": ["Cruella de Vil", "Maléfica", "Gothel", "Reina Malvada"],
        "respuesta": "Cruella de Vil"
    },
]

# Duplicamos para llegar a 20
preguntas = preguntas * 2

# -----------------------------
# Estado
# -----------------------------
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.respondido = False
    st.session_state.opciones = []

# -----------------------------
# Función animación
# -----------------------------
def animacion(correcto):
    if correcto:
        st.success("✨ ¡Correcto!")
        st.balloons()
    else:
        st.error("❌ Incorrecto")
        st.snow()

# -----------------------------
# Juego
# -----------------------------
if st.session_state.indice < len(preguntas):

    pregunta_actual = preguntas[st.session_state.indice]

    st.title("👑 Trivia: Villanas de Disney")
    st.subheader(f"Pregunta {st.session_state.indice + 1} de {len(preguntas)}")

    st.write(pregunta_actual["pregunta"])

    # Mezclar opciones solo una vez
    if not st.session_state.opciones:
        opciones = pregunta_actual["opciones"].copy()
        random.shuffle(opciones)
        st.session_state.opciones = opciones

    seleccion = st.radio(
        "Elige una opción:",
        st.session_state.opciones,
        key=st.session_state.indice
    )

    if st.button("Responder") and not st.session_state.respondido:

        correcto = seleccion == pregunta_actual["respuesta"]

        if correcto:
            st.session_state.puntaje += 1

        animacion(correcto)
        st.session_state.respondido = True

    if st.session_state.respondido:
        if st.button("Siguiente"):
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.session_state.opciones = []
            st.rerun()

else:
    st.title("🎉 Fin del juego")
    st.write(f"Tu puntaje final es: {st.session_state.puntaje} / {len(preguntas)}")

    if st.button("Reiniciar"):
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.respondido = False
        st.session_state.opciones = []
        st.rerun()
        
