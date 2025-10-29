from googletrans import Translator, LANGUAGES
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")

# App Title
st.title("🌍 Cloud-Based Language Translator")
st.write("Translate text instantly between languages using a free translation API.")

# Prepare detailed language list (full names)
languages_full = {v.capitalize(): k for k, v in LANGUAGES.items()}
language_names = list(languages_full.keys())

# Input Section
text = st.text_area("Enter text to translate:", placeholder="Type something here...")
target_lang_name = st.selectbox("Select target language:", sorted(language_names), index=language_names.index("English"))

# Translation Process
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        try:
            translator = Translator()
            dest_code = languages_full[target_lang_name]
            translated = translator.translate(text, dest=dest_code)
            st.success(f"**Translated ({target_lang_name}):** {translated.text}")
        except Exception as e:
            st.error(f"⚠️ Translation failed: {e}")

# Footer
st.markdown("---")
st.markdown("**Developed by:** Sam Jackson S | **Cloud Provider:** GCP (PaaS via Streamlit Cloud)")
