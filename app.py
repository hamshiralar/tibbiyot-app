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
            "🧪 Klinik keyslar va Testlar", 
            "📚 SanPiN va Amaliy koʻnikmalar"
        ]
    )

    # 1. SHOSHILINCH YORDAM BO'LIMI
    if bolim == "⚡ Shoshilinch yordam":
        st.header("⚡ Shoshilinch tibbiy yordam koʻrsatish algoritmlari")
        st.write("Kerakli holatni tanlang va harakatlar ketma-ketligini oʻrganing:")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💉 Anafilaktik shok", use_container_width=True):
                st.error("1. Yuborilayotgan dori vositasini DARHOL toʻxtating!")
                st.warning("2. Bemorning nafas yoʻllari oʻtkazuvchanligini ta'minlang (boshni yon tomonga burang).")
                st.success("3. Adrenalin (Epinefrin) 0.1% — 0.3–0.5 ml mushak orasiga (sonning yon yuzasiga) yuborilsin.")
                st.info("4. Venaga tomchilab fizrastvor (0.9% NaCl) quyishni yoʻlga qoʻying.")

            if st.button("🫀 Yurak-oʻpka reanimatsiyasi (CPR)", use_container_width=True):
                st.info("1. Bemorning hushini va arterial pulsini tekshiring (uyqu arteriyasida).")
                st.warning("2. Koʻkrak qafasi kompressiyasi: daqiqasiga 100–120 marta tezlikda, 5–6 sm chuqurlikda.")
                st.success("3. Kompressiya va sun'iy nafas nisbati — 30 : 2.")

        with col2:
            if st.button("🩸 Tashqi qon ketishlar (Gipovolemik shok)", use_container_width=True):
                st.error("1. Arteryal qon ketishda jgutni jarohatdan 3–5 sm yuqoriga bosing (vaqtni yozib qoʻying!).")
                st.warning("2. Venoz qon ketishda bosuvchi bogʻlam qoʻying.")
                st.success("3. Bemorni gorizontal yotqizib, oyoqlarini 30 gradusga koʻtaring.")

            if st.button("🧠 Gipertonik kriz", use_container_width=True):
                st.warning("1. Bemorni yarim oʻtirgan holatda tinchlantiring.")
                st.info("2. Qon bosimini va pulsni oʻlchang.")
                st.success("3. Shifokor koʻrsatmasiga koʻra til ostiga Kaptopril 25 mg yoki Moksonidin 0.2 mg bering.")

    # 2. KLINIK KEYSLAR VA TESTLAR BO'LIMI
    elif bolim == "🧪 Klinik keyslar va Testlar":
        st.header("🧪 Vaziyatli masalalar va test topshiriqlari")
        st.markdown("---")

        # 1-Masala
        st.subheader("📌 1-Keys: Muolaja xonasida dori asorati")
        st.write("**Vaziyat:** Bemorga vena ichiga Seftriakson yuborilayotganda toʻsatdan havo yetishmasligi, koʻkrakda siqilish va terida toshmalar paydo boʻldi. Qon bosimi 70/40 mm sim.ust. ga tushib ketdi.")
        
        j1 = st.radio("Birinchi galdagi hamshiralik harakatingiz:", [
            "A) Dori yuborishni toʻxtatib, Adrenalin (Epinefrin) yuborish",
            "B) Tinchlantiruvchi dori va shirin choy berish",
            "C) Dimedrol yuborib, tomchilab yuborishni sekinlashtirish"
        ], key="q1")
        
        if st.button("1-Masalani tekshirish"):
            if "A)" in j1:
                st.success("Toʻgʻri! Dori yuborishni DARHOL toʻxtatish va Adrenalin yuborish birinchi galda bajarilishi shart.")
            else:
                st.error("Notoʻgʻri! Anafilaktik shokda birinchi tanlov preparati — Adrenalin hisoblanadi.")

        st.markdown("---")

        # 2-Masala
        st.subheader("📌 2-Keys: Reanimatsion yordam")
        st.write("**Vaziyat:** Palatada bemor toʻsatdan hushini yoʻqotdi, nafas olishi toʻxtadi, uyqu arteriyasida puls aniqlanmayapti.")
        
        j2 = st.radio("Yurak-oʻpka reanimatsiyasini oʻtkazishda kompressiya va nafas berish nisbati qanday?", [
            "A) 15 : 2",
            "B) 30 : 2",
            "C) 5 : 1"
        ], key="q2")

        if st.button("2-Masalani tekshirish"):
            if "B)" in j2:
                st.success("Toʻgʻri! Katta yoshdagilarda Reanimatsiya standarti 30 ta bosish va 2 ta nafas berishdir.")
            else:
                st.error("Notoʻgʻri! Zamonaviy reanimatsiya standarti boʻyicha nisbat 30 : 2 ni tashkil etadi.")

        st.markdown("---")

        # 3-Masala
        st.subheader("📌 3-Keys: Muolaja va parenteral yuborish")
        st.write("**Vaziyat:** Hamshira mushak orasiga dori yuborish jarayonida ignani kiritgach, shprits porshenini orqaga tortganda qon chiqdi.")
        
        j3 = st.radio("Sizning harakatingiz:", [
            "A) Dorini baribir yuboraverish",
            "B) Ignani biroz sugʻorib, dorini yuborish",
            "C) Ignani zudlik bilan chiqarib olish, yangi igna va joy tanlab qayta yuborish"
        ], key="q3")

        if st.button("3-Masalani tekshirish"):
            if "C)" in j3:
                st.success("To'g'ri! Qon chiqishi igna tomirga tushganini bildiradi. Qon tomir ichiga emboliya xavfi boʻlgani uchun dori yuborilmaydi.")
            else:
                st.error("Notoʻgʻri! Ignani zudlik bilan chiqarib, boshqa joyga yangi sterile igna bilan yuborish lozim.")

    # 3. SANPIN VA AMALIY KO'NIKMALAR
    elif bolim == "📚 SanPiN va Amaliy koʻnikmalar":
        st.header("📚 SanPiN me'yorlari va aseptika rejimari")
        
        tab1, tab2, tab3 = st.tabs(["🧹 Dezinfeksiya va Sterilizatsiya", "🧤 Qoʻllarni gigenik ishlov berish", "🗑 Tibbiy chiqindilar"])

        with tab1:
            st.subheader("Tibbiy asboblarni zarasizlantirish bosqichlari")
            st.write("1. **Dezinfeksiya** — Asboblarni dezinfektor eritmasiga toʻliq botirib qoʻyish.")
            st.write("2. **PEO (Presterilizatsion tozalash)** — Oqova suvda yuvish va quritish.")
            st.write("3. **Sterilizatsiya** — Avtoklav (134°C) yoki Suxojar (180°C) shkafida zararsizlantirish.")

        with tab2:
            st.subheader("Qoʻllarni ishlov berish bosqichlari (EN-1500 standarti)")
            st.write("• Kaftlarni kaftga ishqash")
            st.write("• Kaft bilan ikkinchi qoʻl orqa qismini yuvish")
            st.write("• Barmoqlar orasini ishqash")
            st.write("• Bosh barmoqlarni aylana harakat bilan tozalash")

        with tab3:
            st.subheader("Tibbiy chiqindilarni saralash (Klassifikatsiya)")
            st.error("🔴 **A-sinf (Xavfsiz):** Maishiy chiqindilar, qogʻozlar, oziq-ovqat qoldiqlari.")
            st.warning("🟡 **B-sinf (Xavfli):** Qon va biologik suyuqlik tekkan materiallar, shpritslar, ignalar.")
            st.info("🟡 **V-sinf (Favqulodda xavfli):** Mikrobiologik laboratoriya va yuqumli kasalliklar chiqindilari.")

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
