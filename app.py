import streamlit as st

# Funciones del prototipo

def obtener_datos_paciente(nombre, edad, peso, diagnostico, estado_nutricional, patologias):
    """Crea un diccionario con los datos del paciente."""
    return {
        "nombre": nombre,
        "edad": int(edad),
        "peso": float(peso),
        "diagnostico": diagnostico,
        "estado_nutricional": estado_nutricional,
        "patologias": [p.strip() for p in patologias.split(",")] if patologias else []
    }

def calcular_necesidades_validado(datos_paciente):
    """Calcula las necesidades nutricionales verificando que 'edad' y 'peso' sean válidos."""
    try:
        edad = datos_paciente.get("edad", 0)
        peso = datos_paciente.get("peso", 0)
        if not isinstance(edad, (int, float)) or edad <= 0:
            raise ValueError("La edad debe ser un número positivo.")
        if not isinstance(peso, (int, float)) or peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        
        necesidades = {
            "calorias": peso * 25,
            "proteinas": peso * 1.2
        }
        return necesidades
    except Exception as e:
        st.error("Error en calcular necesidades: " + str(e))
        return None

def generar_recomendacion(datos_paciente, necesidades):
    """
    Genera una recomendación de nutrición basada en las reglas:
      - Si el diagnóstico es "Oncológico" y el estado nutricional es "Riesgo moderado",
        recomienda "NPT Magistral".
      - En otros casos, recomienda "Nutrición estándar".
    """
    if datos_paciente["diagnostico"] == "Oncológico" and datos_paciente["estado_nutricional"] == "Riesgo moderado":
        return "NPT Magistral"
    else:
        return "Nutrición estándar"

# Interfaz de usuario con Streamlit
st.title("Agente IA para Recomendación de NPT Magistral")
st.write("Ingresa los datos del paciente:")

nombre = st.text_input("Nombre del paciente", "Juan Pérez")
edad = st.number_input("Edad", min_value=1, value=65)
peso = st.number_input("Peso (kg)", min_value=1.0, value=75.0)
diagnostico = st.selectbox("Diagnóstico", ["Oncológico", "Otro"])
estado_nutricional = st.selectbox("Estado Nutricional", ["Riesgo moderado", "Normal", "Alto riesgo"])
patologias = st.text_input("Patologías (separadas por coma)", "Hipertensión")

if st.button("Generar Recomendación"):
    datos_paciente = obtener_datos_paciente(nombre, edad, peso, diagnostico, estado_nutricional, patologias)
    necesidades = calcular_necesidades_validado(datos_paciente)
    if necesidades:
        recomendacion = generar_recomendacion(datos_paciente, necesidades)
        st.write("**Necesidades Nutricionales:**", necesidades)
        st.write("**Recomendación:**", recomendacion)
