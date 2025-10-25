import streamlit as st
from transformers import pipeline

# --- 1. MODEL LOADING AND CACHING ---

# We return to BART-Large-CNN: the best general-purpose English summarizer.
# This ensures high-quality, fluent output, which is crucial for the resume.
@st.cache_resource
def load_bart_summarizer():
    """Loads the BART English Summarizer, ensuring stability and high quality."""
    try:
        st.info("Loading BART English Summarizer Model (High Quality)...")
        # BART is a Sequence-to-Sequence Transformer fine-tuned for English summarization.
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        return summarizer
    except Exception as e:
        st.error(f"FATAL ERROR: Could not load the model. Check your internet and Python environment. Error: {e}")
        return None

# Load the model
summarizer = load_bart_summarizer()

# --- 2. STREAMLIT APP LAYOUT ---

st.title("📚 AI Study Buddy: Abstractive Summarizer")
st.markdown("---")
# Highlighting the model's capability for the interviewer
st.caption("Powered by the BART Transformer | Focus: High Quality, Fluent English Summary")

# User Input Area
input_text = st.text_area(
    "Paste your study material (English) here:",
    height=300,
    placeholder="Example: The process of photosynthesis is vital for life on Earth. It is the mechanism by which green plants..."
)

# Sliders for User-Controlled Hyperparameters
st.sidebar.header("Summary Length Control (Tokens)")
max_length = st.sidebar.slider("Maximum Length (Tokens)", 
                               min_value=30, max_value=200, value=100, step=10)
min_length = st.sidebar.slider("Minimum Length (Tokens)", 
                               min_value=10, max_value=150, value=30, step=10)

# --- 3. CORE LOGIC (English Inference) ---

if st.button("Generate Summary"):
    
    # 3.1 Verification Checks
    if summarizer is None: st.error("Model not loaded.")
    elif not input_text.strip(): st.warning("Please paste some text.")
    elif len(input_text.split()) < 20: st.warning("Input text is too short for abstractive AI (min 20 words).")
    else:
        # The input is fed directly without any translation prefix.
        input_for_model = input_text

        with st.spinner('AI is generating the high-quality English summary...'):
            try:
                # CORE MODEL CALL
                summary_output = summarizer(
                    input_for_model,
                    max_length=max_length,
                    min_length=min_length,
                    do_sample=False
                )
                
                # --- RESULTS ---
                st.subheader("✅ Abstractive Summary (English)")
                final_summary = summary_output[0]['summary_text']
                st.success(final_summary)
                
                # Show MLOps Data (Word count metrics)
                original_len = len(input_text.split())
                summary_len = len(final_summary.split())
                st.info(f"Original: {original_len} words | Summary Output: {summary_len} words")
                
                # Interview talking point:
                st.markdown("**Project Stability Note:** This output proves proficiency in **Transfer Learning** using a stable, dedicated, high-resource model (BART).")

            except Exception as e:
                st.error(f"An error occurred during model inference: {e}")