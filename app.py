import streamlit as st
import random
import requests

st.set_page_config(
    page_title="Práctica de Ecuaciones",
    page_icon="🧮",
    layout="centered"
)

# -----------------------------
# Función para cargar animación
# -----------------------------
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# -----------------------------
# Generar ecuación aleatoria
# -----------------------------
def generar_ecuacion():
    solucion = random.randint(0, 10)

    a = random.randint(1, 10)
    b = random.randint(-10, 10)

    c = a * solucion + b

    pregunta = f"{a}x + ({b}) = {c}"

    return pregunta, solucion

# -----------------------------
# Inicialización
# -----------------------------
if "pregunta" not in st.session_state:
    st.session_state.pregunta, st.session_state.respuesta = generar_ecuacion()

st.title("🧮 Práctica de Ecuaciones de Primer Grado")

st.write(
    "Resuelve la ecuación. Todas las respuestas son números enteros entre 0 y 10."
)

st.subheader(st.session_state.pregunta)

respuesta_usuario = st.number_input(
    "¿Cuál es el valor de x?",
    step=1,
    value=0
)

col1, col2 = st.columns(2)

# -----------------------------
# Verificar respuesta
# -----------------------------
with col1:
    if st.button("✅ Verificar"):
        if respuesta_usuario == st.session_state.respuesta:

            st.success("¡Correcto! 🎉")

            animacion = load_lottieurl(
                "https://assets2.lottiefiles.com/packages/lf20_jbrw3hcz.json"
            )

            if animacion:
                st.components.v1.html(
                    f"""
                    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                    <lottie-player
                        src="https://assets2.lottiefiles.com/packages/lf20_jbrw3hcz.json"
                        background="transparent"
                        speed="1"
                        style="width: 300px; height: 300px;"
                        autoplay>
                    </lottie-player>
                    """,
                    height=320
                )

        else:
            st.error(
                f"Incorrecto. Intenta nuevamente."
            )

# -----------------------------
# Nueva pregunta
# -----------------------------
with col2:
    if st.button("🔄 Nueva pregunta"):
        st.session_state.pregunta, st.session_state.respuesta = generar_ecuacion()
        st.rerun()

# Mostrar solución opcional (para pruebas)
with st.expander("Modo profesor"):
    st.write("Respuesta:", st.session_state.respuesta)
