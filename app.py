import streamlit as st
from gTTS import gTTS
import io

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Tibbiyot simulyatori",
    page_icon="🩺",
    layout="wide"
)

# Ovoz chiqarish funksiyasi
def speak(text, lang='uz'):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)
    except Exception as e:
        st.error("Ovozni ijro etishda xatolik yuz berdi.")

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
            "📚 SanPiN va Koʻnikmalar", 
            "🎙 Ovozli Shifokor-Hamshira Simulyatsiyasi" # YANGI BO'LIM!
        ]
    )

    # 1-BO'LIM: Shoshilinch yordam (Oldingi saqlangan bo'lim)
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

    # 2-BO'LIM: Klinik keyslar
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

    # 3-BO'LIM: SanPiN
    elif bolim == "📚 SanPiN va Koʻnikmalar":
        st.header("📚 SanPiN me'yorlari va amaliy koʻnikmalar")
        st.subheader("🧹 Dezinfeksiya va Sterilizatsiya bosqichlari")
        st.write("1. Dezinfeksiya $\rightarrow$ 2. PEO (Presterilizatsion tozalash) $\rightarrow$ 3. Sterilizatsiya")

    # 4-BO'LIM: YANGI OVOZLI SIMULYATSIYA!
    elif bolim == "🎙 Ovozli Shifokor-Hamshira Simulyatsiyasi":
        st.header("🎙 Shifokor va Hamshira oʻrtasidagi ovozli muloqot simulyatori")
        st.info("Bu boʻlimda shifokor va hamshira oʻrtasidagi muloqotni ham matn, ham ovozli eshitish orqali mashq qilishingiz mumkin.")

        mavzu = st.selectbox("Simulyatsiya mavzusini tanlang:", [
            "Anafilaktik shok holati",
            "Yurak toʻxtashi (CPR) holati"
        ])

        if mavzu == "Anafilaktik shok holati":
            st.markdown("### 👨‍⚕️ Shifokor va 👩‍⚕️ Hamshira muloqoti:")
            
            st.chat_message("user").write("👨‍⚕️ **Shifokor:** Hamshira xonim, bemorda anafilaktik shok belgilari kuzatilyapti! Zudlik bilan harakat qiling!")
            st.chat_message("assistant").write("👩‍⚕️ **Hamshira:** Tushundim, doktor! Dori yuborishni toʻxtatdim. Qanday dori tayyorlay?")
            st.chat_message("user").write("👨‍⚕️ **Shifokor:** Zudlik bilan 0.5 ml 0.1 foizli Adrenalin tayyorlang va mushak orasiga yuboring!")

            if st.button("Muloqotni ovozli eshitish 🔊"):
                muloqot_matni = "Shifokor: Hamshira xonim, bemorda anafilaktik shok belgilari kuzatilyapti! Zudlik bilan 0.5 millilitr 0.1 foizli Adrenalin yuboring! Hamshira: Tushundim, doktor! Dori to'xtatildi va Adrenalin yuborilmoqda."
                speak(muloqot_matni, lang='uz')

        elif mavzu == "Yurak toʻxtashi (CPR) holati":
            st.markdown("### 👨‍⚕️ Shifokor va 👩‍⚕️ Hamshira muloqoti:")
            
            st.chat_message("user").write("👨‍⚕️ **Shifokor:** Bemorda puls yoʻq! Zudlik bilan reanimatsiyani boshlaymiz!")
            st.chat_message("assistant").write("👩‍⚕️ **Hamshira:** Doktor, soat qayd etildi. Koʻkrak qafasi kompressiyasini boshlaymanmi?")
            st.chat_message("user").write("👨‍⚕️ **Shifokor:** Ha, 30 ta bosish va 2 ta nafas nisbatida davom eting!")

            if st.button("Muloqotni ovozli eshitish 🔊"):
                muloqot_matni = "Shifokor: Bemorda puls yo'q! Zudlik bilan reanimatsiyani boshlaymiz! Hamshira: Doktor, soat qayd etildi. Kompressiya 30 ga 2 nisbatda boshlanmoqda."
                speak(muloqot_matni, lang='uz')

# ==========================================
# RUSCHA TIL INTERFEYSI
# ==========================================
else:
    st.title("🩺 Интерактивный медицинский симулятор")
    st.caption("Кокандский филиал Республиканского Центра повышения квалификации средних медработников")
    st.markdown("---")

    st.header("🎙 Голосовая симуляция: Врач и Медсестра")
    
    st.chat_message("user").write("👨‍⚕️ **Врач:** Сестра, у пациента признаки анафилактического шока! Срочно прекратите введение лекарства!")
    st.chat_message("assistant").write("👩‍⚕️ **Медсестра:** Поняла, доктор! Препарат остановлен. Готовлю Адреналин!")

    if st.button("Прослушать диалог 🔊"):
        dialog_ru = "Врач: Сестра, у пациента признаки анафилактического шока! Срочно прекратите введение лекарства! Медсестра: Поняла, доктор! Препарат остановлен. Готовлю Адреналин 0.1 percent!"
        speak(dialog_ru, lang='ru')
