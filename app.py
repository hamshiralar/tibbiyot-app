import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Tibbiyot simulyatori / Медицинский симулятор",
    page_icon="🩺",
    layout="wide"
)

# 2. Tilni tanlash menyusi (Yon panelda)
st.sidebar.title("🌍 Tilni tanlang / Выберите язык")
til = st.sidebar.selectbox("Til / Язык:", ["Oʻzbekcha", "Русский"])

# OʻZBEKCHA TILI UCHUN INTERFEYS
if til == "Oʻzbekcha":
    st.title("🩺 Oʻrta tibbiyot xodimlari uchun interaktiv simulyator")
    st.caption("Respublika oʻrta tibbiyot va farmatsevtika xodimlari malakasini oshirish markazi")
    st.markdown("---")

    st.sidebar.title("Navigatsiya")
    bolim = st.sidebar.radio(
        "Boʻlimni tanlang:",
        ["💬 Savol-Javob", "🧪 Klinik Keyslar (Test)", "📚 Standartlar va Protokollar"]
    )

    if bolim == "💬 Savol-Javob":
        st.header("💬 Shoshilinch tibbiy yordam boʻyicha ekspress-konsultant")
        st.info("Savolingizni pastga kiriting yoki quyidagi tayyor tugmalardan birini bosing:")

        col1, col2 = st.columns(2)
        with col1:
            btn1 = st.button("💉 Anafilaktik shokda yordam")
        with col2:
            btn2 = st.button("🫀 Yurak-oʻpka reanimatsiyasi (CPR)")

        savol = st.text_input("Savolingizni yozing:", value="Anafilaktik shok" if btn1 else ("CPR" if btn2 else ""))

        if st.button("Harakatlar algoritmini koʻrish", type="primary"):
            if savol:
                st.markdown("---")
                if "anafilaktik" in savol.lower() or btn1:
                    st.subheader("📋 Anafilaktik shokda bajariladigan shoshilinch choralar:")
                    st.error("1. Yuborilayotgan dori vositasini DARHOL toʻxtating!")
                    st.warning("2. Bemorning nafas yoʻllari oʻtkazuvchanligini ta'minlang (boshni yon tomonga burish).")
                    st.success("3. Adrenalin (Epinefrin) 0.1% — 0.3-0.5 ml mushak orasiga yuborilsin.")
                    st.info("4. Vena ichiga kateter oʻrnating va fiziologik eritma yuborishni boshlang.")
                elif "cpr" in savol.lower() or btn2:
                    st.subheader("🫀 Bazaviy yurak-oʻpka reanimatsiyasi (CPR):")
                    st.write("- **Chastota:** Daqiqasiga 100–120 marta.")
                    st.write("- **Chuqurlik:** 5–6 sm.")
                    st.write("- **Nisbat:** 30 ta bosish va 2 ta sun'iy nafas (30:2).")
                else:
                    st.warning("Bu savol boʻyicha ma'lumot topilmadi.")
            else:
                st.warning("Iltimos, savol kiriting!")

    elif bolim == "🧪 Klinik Keyslar (Test)":
        st.header("🧪 Amaliy koʻnikmalarni baholash")
        st.subheader("📌 Vaziyatli masala: Anafilaksiya")
        st.markdown("> **Vaziyat:** Inyeksiya vaqtida bemorda nafas qisishi va bosim tushishi kuzatildi.")
        
        javob = st.radio("Birinchi galdagi harakat:", [
            "A) Dimedrol yuborish",
            "B) Dori yuborishni toʻxtatib, Adrenalin yuborish",
            "C) Shirin choy berish"
        ])
        if st.button("Tekshirish"):
            if "B)" in javob:
                st.balloons()
                st.success("Toʻgʻri! Adrenalin birinchi tanlov preparati.")
            else:
                st.error("Notoʻgʻri!")

    elif bolim == "📚 Standartlar va Protokollar":
        st.header("📚 Standartlar")
        st.write("• Qoʻllarni gigiyenik ishlov berish (JST standarti).")
        st.write("• Periferik vena kateterini parvarish qilish.")

# RUSCHA TILI UCHUN INTERFEYS (РУССКИЙ ЯЗЫК)
else:
    st.title("🩺 Интерактивный симулятор для среднего медицинского персонала")
    st.caption("Центр повышения квалификации медицинских работников")
    st.markdown("---")

    st.sidebar.title("Навигация")
    bolim = st.sidebar.radio(
        "Выберите раздел:",
        ["💬 Вопросы и ответы", "🧪 Клинические кейсы (Тест)", "📚 Стандарты и протоколы"]
    )

    if bolim == "💬 Вопросы и ответы":
        st.header("💬 Экспресс-консультант по неотложной помощи")
        st.info("Введите ваш вопрос ниже или нажмите на готовую кнопку:")

        col1, col2 = st.columns(2)
        with col1:
            btn1 = st.button("💉 Помощь при анафилактическом шоке")
        with col2:
            btn2 = st.button("🫀 Сердечно-легочная реанимация (СЛР)")

        savol = st.text_input("Ваш вопрос:", value="Анафилактический шок" if btn1 else ("СЛР" if btn2 else ""))

        if st.button("Посмотреть алгоритм действий", type="primary"):
            if savol:
                st.markdown("---")
                if "анафилак" in savol.lower() or btn1:
                    st.subheader("📋 Алгоритм при анафилактическом шоке:")
                    st.error("1. НЕМЕДЛЕННО прекратите введение препарата!")
                    st.warning("2. Обеспечьте проходимость дыхательных путей.")
                    st.success("3. Введите Адреналин 0.1% внутримышечно.")
                    st.info("4. Обеспечьте венозный доступ и начните инфузию.")
                elif "слр" in savol.lower() or btn2:
                    st.subheader("🫀 Базовая СЛР:")
                    st.write("- **Частота:** 100–120 в минуту.")
                    st.write("- **Глубина:** 5–6 см.")
                    st.write("- **Соотношение:** 30 компрессий : 2 вдоха.")
                else:
                    st.warning("Информация по данному вопросу добавляется.")
            else:
                st.warning("Пожалуйста, введите вопрос!")

    elif bolim == "🧪 Клинические кейсы (Тест)":
        st.header("🧪 Проверка практических навыков")
        st.subheader("📌 Ситуационный кейс: Анафилаксия")
        st.markdown("> **Ситуация:** У пациента одышка и падение давления после инъекции.")
        
        javob = st.radio("Первое действие:", [
            "А) Ввести димедрол",
            "Б) Прекратить введение и ввести Адреналин",
            "В) Дать чай"
        ])
        if st.button("Проверить"):
            if "Б)" in javob:
                st.balloons()
                st.success("Верно! Адреналин — препарат первой линии.")
            else:
                st.error("Неверно!")

    elif bolim == "📚 Стандарты и протоколы":
        st.header("📚 Стандарты")
        st.write("• Гигиеническая обработка рук (стандарт ВОЗ).")
        st.write("• Уход за периферическим катетером.")