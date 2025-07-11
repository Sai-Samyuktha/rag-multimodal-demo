# streamlit_app.py
# This file should be placed in the root directory of your forked repository

import streamlit as st
import sys
import os

# Add the backend directories to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

st.set_page_config(
    page_title="RAG Multimodal Demo",
    page_icon="🤖",
    layout="wide"
)

def main():
    st.title("🤖 RAG Multimodal Demo")
    st.markdown("---")
    
    # Check if environment variables are set
    if not os.getenv("OPENAI_API_KEY"):
        st.error("⚠️ OpenAI API Key not found! Please set it in Streamlit Cloud secrets.")
        st.markdown("""
        To set up your API key:
        1. Go to your Streamlit Cloud dashboard
        2. Click on your app
        3. Go to Settings → Secrets
        4. Add: `OPENAI_API_KEY = "your-api-key-here"`
        """)
        return
    
    # Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Home", "RAG Option 1", "RAG Option 2", "RAG Option 3", "Setup Guide"]
    )
    
    if page == "Home":
        show_home()
    elif page == "RAG Option 1":
        show_rag_option_1()
    elif page == "RAG Option 2":
        show_rag_option_2()
    elif page == "RAG Option 3":
        show_rag_option_3()
    elif page == "Setup Guide":
        show_setup_guide()

def show_home():
    st.header("Welcome to RAG Multimodal Demo")
    
    st.markdown("""
    This demo showcases three different approaches to Retrieval-Augmented Generation (RAG) with multimodal data:
    
    ### 🔍 Three RAG Options:
    
    **Option 1: Raw Images + Multimodal LLM**
    - Uses multimodal embeddings (CLIP) to embed images and text
    - Retrieves both images and text using similarity search
    - Passes raw images and text to GPT-4V for synthesis
    
    **Option 2: Image Summaries + Text LLM**
    - Uses GPT-4V to create text summaries from images
    - Embeds and retrieves image summaries and text chunks
    - Uses GPT-4 for final answer synthesis
    
    **Option 3: Hybrid Approach**
    - Creates text summaries from images for retrieval
    - But passes raw images to GPT-4V for final synthesis
    - Best of both worlds approach
    
    ### 📋 Current Status:
    """)
    
    # Check system status
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if os.getenv("OPENAI_API_KEY"):
            st.success("✅ OpenAI API Key: Configured")
        else:
            st.error("❌ OpenAI API Key: Missing")
    
    with col2:
        # Check if data is ingested (simplified check)
        if os.path.exists("./chroma_db"):
            st.success("✅ Database: Ready")
        else:
            st.warning("⚠️ Database: Not initialized")
    
    with col3:
        st.info("ℹ️ Status: Ready to use")
    
    st.markdown("---")
    st.markdown("**Note**: This is a simplified Streamlit version. Full functionality requires local setup with data ingestion.")

def show_rag_option_1():
    st.header("RAG Option 1: Raw Images + Multimodal LLM")
    
    st.markdown("""
    This option uses:
    - **Multimodal embeddings** (CLIP) for both images and text
    - **Raw image retrieval** with similarity search
    - **GPT-4V** for final answer synthesis
    """)
    
    # Simple query interface
    query = st.text_input("Enter your question:")
    
    if st.button("Search", key="rag1"):
        if query:
            st.warning("⚠️ Full RAG functionality requires data ingestion. This is a demo interface.")
            st.info(f"Query: {query}")
            st.markdown("In a full setup, this would:")
            st.markdown("1. 🔍 Search for relevant images and text using CLIP embeddings")
            st.markdown("2. 📊 Retrieve raw images and text chunks")
            st.markdown("3. 🤖 Send to GPT-4V for multimodal analysis")
        else:
            st.error("Please enter a question")

def show_rag_option_2():
    st.header("RAG Option 2: Image Summaries + Text LLM")
    
    st.markdown("""
    This option uses:
    - **GPT-4V** to create text summaries from images
    - **Text embeddings** for retrieval
    - **GPT-4** (text-only) for final synthesis
    """)
    
    query = st.text_input("Enter your question:", key="query2")
    
    if st.button("Search", key="rag2"):
        if query:
            st.warning("⚠️ Full RAG functionality requires data ingestion. This is a demo interface.")
            st.info(f"Query: {query}")
            st.markdown("In a full setup, this would:")
            st.markdown("1. 🔍 Search for relevant image summaries and text")
            st.markdown("2. 📝 Retrieve text summaries (no raw images)")
            st.markdown("3. 🤖 Send to GPT-4 for text-based synthesis")
        else:
            st.error("Please enter a question")

def show_rag_option_3():
    st.header("RAG Option 3: Hybrid Approach")
    
    st.markdown("""
    This option combines the best of both worlds:
    - **GPT-4V** creates summaries for retrieval
    - **Text embeddings** for efficient search
    - **Raw images + GPT-4V** for final synthesis
    """)
    
    query = st.text_input("Enter your question:", key="query3")
    
    if st.button("Search", key="rag3"):
        if query:
            st.warning("⚠️ Full RAG functionality requires data ingestion. This is a demo interface.")
            st.info(f"Query: {query}")
            st.markdown("In a full setup, this would:")
            st.markdown("1. 🔍 Search using image summaries and text embeddings")
            st.markdown("2. 📊 Retrieve raw images and text chunks")
            st.markdown("3. 🤖 Send raw images + text to GPT-4V for synthesis")
        else:
            st.error("Please enter a question")

def show_setup_guide():
    st.header("Setup Guide")
    
    st.markdown("""
    ## 🚀 Full Setup Instructions
    
    To get the complete functionality, you need to run this locally:
    
    ### 1. Prerequisites
    ```bash
    # Install system dependencies
    # Linux:
    sudo apt install poppler-utils tesseract-ocr
    
    # macOS:
    brew install poppler tesseract
    ```
    
    ### 2. Clone and Setup
    ```bash
    git clone https://github.com/artefactory/rag-multimodal-demo
    cd rag-multimodal-demo
    poetry install
    ```
    
    ### 3. Environment Variables
    ```bash
    cp template.env .env
    # Edit .env with your OpenAI API key
    ```
    
    ### 4. Ingest Data
    ```bash
    # Choose one:
    make ingest_rag_1  # For Option 1
    make ingest_rag_2  # For Option 2
    make ingest_rag_3  # For Option 3
    ```
    
    ### 5. Run Application
    ```bash
    # Backend
    make serve_backend
    
    # Frontend (new terminal)
    make serve_frontend
    ```
    
    ## 🔧 Streamlit Cloud Limitations
    
    This Streamlit Cloud version is a **demo interface only** because:
    - No data ingestion capabilities
    - Limited system dependencies
    - Memory constraints for large document processing
    - No persistent storage
    
    For full functionality, deploy on platforms like:
    - Google Cloud Run
    - AWS ECS
    - Azure Container Instances
    - Or run locally
    """)

if __name__ == "__main__":
    main()
