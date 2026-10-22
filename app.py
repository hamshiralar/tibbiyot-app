import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Tibbiyot simulyatori",
    page_icon="🩺",
    layout="wide"
)

# 2. Tilni tanlash menyusi
st.sidebar.title("🌍 Tilni tanlang / Выберите язык")
til = st.sidebar.selectbox("Til / Язык:", ["Oʻzbekcha", "Русский"])

# ==========================================
# OʻZBEKCHA TILI INTERFEYSI
# ==========================================
if til == "Oʻzbekcha":
    st.title("🩺 Oʻrta tibbiyot xodimlari uchun interaktiv simulyator")
    st.caption("Respublika oʻrta tibbiyot va farmatsevtika xodimlari malakasini oshirish markazi Qoʻqon filiali")
    st.markdown("---")

    st.sidebar.title("Navigatsiya")
    bolim = st.sidebar.radio(
        "Boʻlimni tanlang:",
        [
            "⚡ Shoshilinch yordam", 
            "🧪 Klinik keyslar (Test)", 
            "📚 SanPiN va Koʻnikmalar"
        ]
    )

    # 1. Shoshilinch yordam
    if bolim == "⚡ Shoshilinch yordam":
        st.header("⚡ Shoshilinch tibbiy yordam koʻrsatish algoritmlari")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💉 Anafilaktik shok", use_container_width=True):
                st.error("1. Yuborilayotgan dori vositasini DARHOL toʻxtating!")
                st.warning("2. Bemorning nafas yoʻllari oʻtkazuvchanligini ta'minlang.")
                st.success("3. Adrenalin (Epinefrin) 0.1% — 0.3-0.5 ml mushak orasiga yuborilsin.")
        
        with col2:
            if st.button("🫀 Yurak-oʻpka reanimatsiyasi (CPR)", use_container_width=True):
                st.info("1. Koʻkrak qafasi kompressiyasi: daqiqasiga 100-120 marta.")
                st.info("2. Kompressiya va nafas nisbati — 30 : 2.")

    # 2. Klinik keyslar
    elif bolim == "🧪 Klinik keyslar (Test)":
        st.header("🧪 Vaziyatli masalalar va test topshiriqlari")
        st.subheader("📌 Keys: Muolaja xonasida anafilaksiya")
        st.write("Bemorga vena ichiga dori yuborilayotganda toʻsatdan nafas siqishi va terida toshmalar paydo boʻldi.")
        
        javob = st.radio("Birinchi galdagi harakatingiz:", [
            "A) Dimedrol yuborish",
            "B) Dori yuborishni toʻxtatib, Adrenalin yuborish",
            "C) Bemorga shirin choy berish"
        ])
        
        if st.button("Tekshirish"):
            if "B)" in javob:
                st.balloons()
                st.success("Toʻgʻri! Dori zudlik bilan toʻxtatilib, Adrenalin birinchi tanlov preparati hisoblanadi.")
            else:
                st.error("Notoʻgʻri! Adrenalin yuborilishi va dori toʻxtatilishi shart.")

    # 3. SanPiN
    elif bolim == "📚 SanPiN va Koʻnikmalar":
        st.header("📚 SanPiN me'yorlari va amaliy koʻnikmalar")
        st.subheader("🧹 Dezinfeksiya va Sterilizatsiya bosqichlari")
        st.write("1. Dezinfeksiya $\rightarrow$ 2. PEO (Presterilizatsion tozalash) $\rightarrow$ 3. Sterilizatsiya")

# ==========================================
# RUSCHA TIL INTERFEYSI
# ==========================================
else:
    st.title("🩺 Интерактивный медицинский симулятор")
    st.caption("Кокандский филиал Республиканского Центра повышения квалификации средних медработников")
    st.markdown("---")

    st.header("⚡ Алгоритмы экстренной помощи")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💉 Анафилактический шок", use_container_width=True):
            st.error("1. НЕМЕДЛЕННО прекратите введение препарата!")
            st.warning("2. Обеспечьте проходимость дыхательных путей.")
            st.success("3. Введите Адреналин 0.1% — 0.3-0.5 мл внутримышечно.")

    with col2:
        if st.button("🫀 Сердечно-легочная реанимация (СЛР)", use_container_width=True):
            st.info("1. Частота компрессий грудной клетки: 100-120 в минуту.")
            st.info("2. Соотношение компрессий и вдохов — 30 : 2.")
