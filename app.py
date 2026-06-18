import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

# Page Configuration
st.set_page_config(
    page_title="CodeAlpha Language Translation Tool",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#4F46E5;
}
.sub-title{
    text-align:center;
    font-size:20px;
    color:gray;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    "<div class='main-title'>🌍 CodeAlpha Language Translation Tool</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>CodeAlpha Internship Project - Translate text instantly into multiple languages using AI</div>",
    unsafe_allow_html=True
)

st.success("🌟 Welcome! Enter your text and get instant translations.")

# Languages
languages = {
    "🇺🇸 English": "en",
    "🇮🇳 Tamil": "ta",
    "🇮🇳 Hindi": "hi",
    "🇫🇷 French": "fr",
    "🇩🇪 German": "de",
    "🇪🇸 Spanish": "es",
    "🇯🇵 Japanese": "ja",
    "🇨🇳 Chinese": "zh-CN",
    "🇸🇦 Arabic": "ar",
    "🇷🇺 Russian": "ru",
    "🇰🇷 Korean": "ko",
    "🇮🇹 Italian": "it"
}

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Enter Text")

    input_text = st.text_area(
        "",
        height=300,
        placeholder="Type your text here..."
    )

    st.info(f"📄 Words: {len(input_text.split())}")
    st.info(f"🔤 Characters: {len(input_text)}")

with col2:
    st.subheader("🌐 Select Target Language")

    target_lang = st.selectbox(
        "",
        list(languages.keys())
    )

# Automatic Translation
if input_text.strip():

    try:
        translated_text = GoogleTranslator(
            source="auto",
            target=languages[target_lang]
        ).translate(input_text)

        st.subheader("📋 Translated Text")

        st.text_area(
            "",
            translated_text,
            height=250
        )

        # Download Button
        st.download_button(
            label="📥 Download Translation",
            data=translated_text,
            file_name="translated_text.txt",
            mime="text/plain"
        )

        # Text to Speech
        st.subheader("🔊 Listen to Translation")

        tts = gTTS(
            text=translated_text,
            lang=languages[target_lang]
        )

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)

            with open(fp.name, "rb") as audio_file:
                audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

    except Exception as e:
        st.error(f"Translation Error: {e}")

else:
    st.info("✍️ Enter text to start translating.")

# Footer
st.markdown("---")
st.markdown(
    "<center>🌍 CodeAlpha Language Translation Tool | Developed by Srijana D | Python • Streamlit • Deep Translator • gTTS</center>",
    unsafe_allow_html=True
)