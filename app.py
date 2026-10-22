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
    st.title("🩺 Oʻrta tibbiyot xodimlari uchun kengaytirilgan simulyator")
    st.caption("Respublika oʻrta tibbiyot va farmatsevtika xodimlari malakasini oshirish markazi Qoʻqon filiali")
    st.markdown("---")

    st.sidebar.title("Navigatsiya")
    bolim = st.sidebar.radio(
        "Boʻlimni tanlang:",
        [
            "⚡ Shoshilinch yordam (Algoritmlar)", 
            "🧪 Klinik keyslar va Testlar (5 ta)", 
            "📚 SanPiN va Amaliy standartlar"
        ]
    )

    # 1. SHOSHILINCH YORDAM BO'LIMI
    if bolim == "⚡ Shoshilinch yordam (Algoritmlar)":
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

            if st.button("🧠 Gipertonik kriz", use_container_width=True):
                st.warning("1. Bemorni yarim oʻtirgan holatda tinchlantiring.")
                st.info("2. Qon bosimini va pulsni oʻlchang.")
                st.success("3. Shifokor koʻrsatmasiga koʻra til ostiga Kaptopril 25 mg yoki Moksonidin 0.2 mg bering.")

        with col2:
            if st.button("🩸 Tashqi qon ketishlar", use_container_width=True):
                st.error("1. Arteryal qon ketishda jgutni jarohatdan 3–5 sm yuqoriga bosing (vaqtini yozib qoʻying!).")
                st.warning("2. Venoz qon ketishda bosuvchi steril bogʻlam qoʻying.")
                st.success("3. Bemorni gorizontal yotqizib, oyoqlarini 30 gradusga koʻtaring.")

            if st.button("⚡ Tutaqanoq (Sudoroga/Epilepsiya)", use_container_width=True):
                st.error("1. Bemorni yiqilishidan va jarohat olishidan saqlang (bosh ostiga yumshoq narsa qoʻying).")
                st.warning("2. Ogʻziga majburan qattiq buyumlar (qoshiq, spagatel) tiqmang!")
                st.success("3. Xuruj tugagach, bemorni yonbosh holatga (tiklanish holati) oʻtkazing.")

            if st.button("💔 Oʻtkir miokard infarkti (OKS)", use_container_width=True):
                st.error("1. Bemorni zudlik bilan yotqizing va harakatlanishini taqiqlang.")
                st.warning("2. Til ostiga Nitrogbitserin (agar arterial bosim > 90/60 boʻlsa) bering.")
                st.success("3. Oksigenoterapiya (kislorod berish) va EKG tushirishni tashkillashtiring.")

    # 2. KLINIK KEYSLAR VA TESTLAR BO'LIMI
    elif bolim == "🧪 Klinik keyslar va Testlar (5 ta)":
        st.header("🧪 Vaziyatli masalalar va amaliy testlar")
        st.markdown("---")

        # 1-Keys
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

        # 2-Keys
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

        # 3-Keys
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

        st.markdown("---")

        # 4-Keys
        st.subheader("📌 4-Keys: Hemotransfuziya (Qon quyish)")
        st.write("**Vaziyat:** Bemorga eritrotsitar massa quyilayotgan paytda bel sohasida kuchli ogʻriq, qaltirash va tana haroratining koʻtarilishi kuzatildi.")
        j4 = st.radio("Hamshiraning birinchi harakati qanday boʻlishi kerak?", [
            "A) Qon quyish tezligini sekinlashtirish va shifokorni kutish",
            "B) Qon quyishni DARHOL toʻxtatish va venaga fizrastvor quyishni ulash",
            "C) Bemorgа isitma tushiruvchi dori yuborish"
        ], key="q4")
        if st.button("4-Masalani tekshirish"):
            if "B)" in j4:
                st.success("Toʻgʻri! Gemotransfuzion reaksiyada qon quyish ZUDLIK bilan toʻxtatiladi va vena yoʻli saqlab qolinadi.")
            else:
                st.error("Notoʻgʻri! Qon quyishni zudlik bilan toʻxtatish va shifokorga xabar berish shart.")

        st.markdown("---")

        # 5-Keys
        st.subheader("📌 5-Keys: Kuydiruvchi jarohatlar (Termik kuyish)")
        st.write("**Vaziyat:** Bemor oʻng qoʻli va koʻkrak qafasining old yuzasi qaynayotgan suvdan kuydi. Kuyish maydoni necha foizni tashkil etadi?")
        j5 = st.radio("Valter ('Toʻqqizlar qoidasi') boʻyicha hisoblang:", [
            "A) 9%",
            "B) 18%",
            "C) 27%"
        ], key="q5")
        if st.button("5-Masalani tekshirish"):
            if "B)" in j5:
                st.success("Toʻgʻri! Bitta qoʻl yuzasi = 9%, koʻkrak qafasi old yuzasi = 9%. Jami: 18%.")
            else:
                st.error("Notoʻgʻri!
