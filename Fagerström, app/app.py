import streamlit as st
import time

# 1. CONFIGURACIÓN Y ESTILO DE ALTO CONTRASTE
st.set_page_config(page_title="Salud Policial Roatán", page_icon="🚭", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: white !important; }
    h1, h2, h3, p, span, label, div { color: #1a1a1a !important; }
    .pregunta-titulo {
        font-size: 19px;
        font-weight: bold;
        background-color: #f0f2f6;
        padding: 12px;
        border-radius: 10px;
        margin-top: 20px;
        border-left: 6px solid #002d72;
    }
    .consejo-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2196f3;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO
st.title("🚭 Programa: Gana Vida Sin Tabaco")
st.subheader("Dirección de Sanidad Policial - Roatán")
st.write("Servir y Proteger también es cuidar de tu propia salud. ¡Haz el test!")

# 3. FORMULARIO
with st.form("test_fagerstrom_final"):
    st.markdown("<div class='pregunta-titulo'>1. ¿Cuánto tiempo tarda en fumar su primer cigarrillo tras despertar?</div>", unsafe_allow_html=True)
    p1 = st.radio("p1", ["Más de 60 minutos", "31-60 minutos", "6-30 minutos", "Menos de 5 minutos"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>2. ¿Le cuesta no fumar en sitios prohibidos (Cine, Posta, patrulla)?</div>", unsafe_allow_html=True)
    p2 = st.radio("p2", ["No", "Sí"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>3. ¿A qué cigarrillo le costaría más renunciar?</div>", unsafe_allow_html=True)
    p3 = st.radio("p3", ["Cualquier otro", "El primero de la mañana"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>4. ¿Cuántos cigarrillos fuma al día?</div>", unsafe_allow_html=True)
    p4 = st.radio("p4", ["Menos de 11", "11-20", "21-30", "Más de 30"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>5. ¿Fuma más durante las primeras horas tras levantarse?</div>", unsafe_allow_html=True)
    p5 = st.radio("p5", ["No", "Sí"], label_visibility="collapsed")

    st.markdown("<div class='pregunta-titulo'>6. ¿Fuma si está tan enfermo que debe estar en cama?</div>", unsafe_allow_html=True)
    p6 = st.radio("p6", ["No", "Sí"], label_visibility="collapsed")

    st.divider()
    boton_enviar = st.form_submit_button("📊 EVALUAR RESULTADOS")

# 4. LÓGICA DE RESULTADOS Y CONSEJOS (Basados en PDF 0.1.1 y 0.1.2)
if boton_enviar:
    puntos = 0
    puntos += ["Más de 60 minutos", "31-60 minutos", "6-30 minutos", "Menos de 5 minutos"].index(p1)
    puntos += 1 if p2 == "Sí" else 0
    puntos += 1 if p3 == "El primero de la mañana" else 0
    puntos += ["Menos de 11", "11-20", "21-30", "Más de 30"].index(p4)
    puntos += 1 if p5 == "Sí" else 0
    puntos += 1 if p6 == "Sí" else 0

    with st.spinner('Analizando datos médicos...'):
        time.sleep(1)

    st.markdown(f"<h2 style='text-align: center;'>Puntuación: {puntos}</h2>", unsafe_allow_html=True)

    # --- RESULTADOS DINÁMICOS ---
    if puntos < 4:
        st.balloons()
        st.success("✅ **Dependencia BAJA**")
        st.markdown("<div class='consejo-box'><b>Consejo para ti:</b> Tu cuerpo aún tiene el control. Al dejarlo hoy, en solo <b>20 minutos</b> tu ritmo cardíaco y presión arterial volverán a su nivel normal. ¡Gana vida ahora!</div>", unsafe_allow_html=True)
    
    elif 4 <= puntos <= 6:
        st.warning("⚠️ **Dependencia MEDIA**")
        st.markdown("<div class='consejo-box'><b>Consejo para ti:</b> El tabaco ya te condiciona. A las <b>48 horas</b> de dejarlo, recuperarás la agudeza del gusto y el olfato para disfrutar del paraíso en Roatán. ¡Tú puedes lograrlo!</div>", unsafe_allow_html=True)
    
    else:
        st.snow()
        st.error("🚨 **Dependencia ALTA**")
        st.markdown("<div class='consejo-box'><b>Consejo Urgente:</b> Tu salud operativa está en riesgo. A las <b>8 horas</b> de dejarlo, el oxígeno en tu sangre subirá a su nivel normal. No lo dudes, acude a Sanidad Policial para apoyo especializado.</div>", unsafe_allow_html=True)

    # Beneficio general adicional del PDF
    st.info("💡 **¿Sabías que?** Al año de dejar de fumar, tu riesgo de sufrir un infarto de miocardio disminuye a la mitad.")

st.caption("Referencia: Test de Fagerström y Manual ¡Gana Vida! - D.S.P. Roatán")
