# 📚 AI Study Buddy: Abstractive Text Summarizer

This project is an **end-to-end web application** that generates high-quality, fluent summaries from any long English text. It demonstrates key skills in **Transfer Learning**, **Deep Learning Deployment**, and **MLOps**.

---

## ✨ Project Highlights & Technical Stack

| Feature | Description | Key Skill Demonstrated |
| :--- | :--- | :--- |
| **Abstractive Summarization** | The application is built around the **BART-Large-CNN Transformer** model, which generates **new, coherent sentences** (mimicking human summarization). | **Transfer Learning**, **Seq2Seq Architecture** (Encoder-Decoder). |
| **Model Selection** | Chose the **BART-CNN** model specifically because it was fine-tuned on the large **CNN/Daily Mail** news dataset, guaranteeing top-tier English summarization quality. | **Model Evaluation/Selection**, **Deep Learning Optimization**. |
| **Deployment** | The entire Python backend is wrapped in an interactive front-end using **Streamlit**. | **MLOps Lite**, **End-to-End Delivery**, and **Web Application Deployment**. |
| **Scalability Awareness** | The design includes a clear plan for **Hierarchical Summarization** to overcome the model's **1024-token context window limit**. | **MLOps Pipeline Design**, **Scaling Solutions**. |

---

## ⚙️ Installation and Run Instructions

This section ensures anyone can easily replicate and test your work.

### Prerequisites

* Python 3.8+
* The project requires a stable internet connection for the initial download of the large **BART** model weights.

### Steps to Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/laliithaaganti/AI-Study-Buddy-Summarizer.git](https://github.com/laliithaaganti/AI-Study-Buddy-Summarizer.git)
    cd AI-Study-Buddy-Summarizer
    ```

2.  **Activate Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    # Installs the exact versions of transformers, torch, and streamlit
    pip install -r requirements.txt
    ```

4.  **Launch the App**
    ```bash
    streamlit run study_buddy_app.py
    ```
    *The application will open in your default browser at `http://localhost:8501`.*