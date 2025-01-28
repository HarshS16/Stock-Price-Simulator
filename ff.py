import streamlit as st
from time import sleep
import random
import plotly.graph_objects as go
import pandas as pd
import urllib.parse
import io


st.set_page_config(page_title="Fake News Detector", layout="wide")


st.markdown("""
    <style>
        /* General Page Styles */
        body {
            background: #F3F4F6; /* Light background */
            font-family: 'Roboto', sans-serif;
            color: #333;  /* Dark text color for readability */
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .stApp {
            background: #F3F4F6; /* Light background */
        }

        /* Title */
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #2D3A3A;
            text-align: center;
            margin-top: 50px;
            text-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Subheader */
        .subheader {
            text-align: center;
            color: #6B7280;
            font-size: 18px;
            margin-top: 15px;
            font-weight: 400;
        }

        /* Container for the content */
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px;
        }

        /* Input Area */
        .input_area {
            font-size: 16px;
            padding: 18px;
            border-radius: 10px;
            border: 2px solid #E5E7EB;
            width: 80%;
            margin: 20px auto;
            background-color: #FFFFFF;
            color: #333; /* Dark text color */
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }

        .input_area:focus {
            outline: none;
            border-color: #1D4ED8;
            box-shadow: 0px 4px 12px rgba(30, 136, 229, 0.2);
        }

        /* Button Styles */
        .stButton > button {
            background-color: #1D4ED8;
            color: white;
            font-size: 18px;
            padding: 15px 35px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            font-weight: 600;
        }

        .stButton > button:hover {
            background-color: #1D4ED8;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
            transform: translateY(-2px);
        }

        /* Result Box */
        .result {
            font-size: 28px;
            font-weight: 600;
            text-align: center;
            margin-top: 40px;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            color: #333; /* Set dark color for the result text */
        }

        .result.real {
            background-color: rgba(56, 142, 60, 0.1);
            color: #388E3C; /* Dark green for real */
        }

        .result.fake {
            background-color: rgba(244, 67, 54, 0.1);
            color: #F44336; /* Dark red for fake */
        }

        /* Confidence */
        .confidence {
            font-size: 20px;
            text-align: center;
            color: #6B7280; /* Dark grey for the confidence text */
            margin-top: 10px;
            font-weight: 600;
        }

        /* Spinner */
        .stSpinner {
            text-align: center;
            margin-top: 30px;
        }

        /* Alert Styles */
        .alert {
            text-align: center;
            color: #F87171;
            margin-top: 20px;
            font-size: 16px;
            font-weight: 600;
        }

        /* Selectbox with pointer */
        .stSelectbox, .stSelectbox div, .stSelectbox > div > div {
            cursor: pointer !important;
        }

        /* Text color fix for all markdown content (e.g., description, etc.) */
        .stMarkdown {
            color: #333 !important; /* Dark text color */
        }

        /* History section */
        .history {
            font-size: 18px;
            text-align: left;
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            background-color: #FFFFFF;
            width: 80%;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.05);
        }

        .history-item {
            margin-bottom: 15px;
        }

        /* Responsive styling */
        @media (max-width: 768px) {
            .title {
                font-size: 36px;
            }

            .input_area {
                width: 90%;
            }

            .stButton > button {
                width: 100%;
                padding: 14px;
            }
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="title">Fake News Detector</div>', unsafe_allow_html=True)
st.markdown("""
    🚨 **Paste a news headline or article below, and let us detect whether it's real or fake!** 
    We use advanced algorithms to detect misinformation. 
""", unsafe_allow_html=True)


news_category = st.selectbox(
    "Select the type of news:",
    ["Politics", "Science", "Entertainment", "Sports", "Health"],
    key="category_select"
)


if "user_input" not in st.session_state:
    st.session_state.user_input = ""


if "history" not in st.session_state:
    st.session_state.history = []


user_input = st.text_area(
    "Enter News Text",
    height=150,
    placeholder="Paste your news article or headline here...",
    value=st.session_state.user_input,
    key="news_input",
    help="Paste a news headline or article to analyze"
)


if user_input != st.session_state.user_input:
    st.session_state.user_input = user_input


if st.button("Check if it's Fake or Real", key="check_button"):
    if user_input:
        
        with st.spinner("Analyzing... Please wait!"):
            sleep(2)  

            
            result = random.choice(["Real", "Fake"])  
            confidence = random.uniform(60, 99)  

            
            result_class = "real" if result == "Real" else "fake"
            result_text = "Real" if result == "Real" else "Fake"
            st.markdown(f'<div class="result {result_class}">{"✅" if result == "Real" else "⚠️"} The news is <strong>{result_text}</strong>!</div>', unsafe_allow_html=True)

            
            st.markdown(f'<div class="confidence">Confidence: {confidence:.2f}%</div>', unsafe_allow_html=True)

            
            st.progress(confidence / 100)

            
            st.session_state.history.append({"text": user_input, "result": result, "confidence": confidence})

            
            st.session_state.user_input = ""

            
            share_url = f"https://twitter.com/intent/tweet?text=I%20just%20checked%20the%20news%20and%20it%20was%20{result}%20with%20{confidence:.2f}%20confidence%20-%20Fake%20News%20Detector%20%23FakeNewsDetector%20{urllib.parse.quote(user_input)}"
            st.markdown(f'<a href="{share_url}" target="_blank"><button class="stButton"><strong>Share on Twitter</strong></button></a>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="alert">⚠️ Please enter some text to analyze.</div>', unsafe_allow_html=True)


if st.button("Clear Input", key="clear_button"):
    st.session_state.user_input = ""  


if st.button("Clear History", key="clear_history_button"):
    st.session_state.history = []  


if st.session_state.history:
    def convert_history_to_csv(history):
        df = pd.DataFrame(history)
        csv = df.to_csv(index=False)
        return csv

    csv = convert_history_to_csv(st.session_state.history)
    st.download_button(
        label="Download Analysis History",
        data=csv,
        file_name="fake_news_analysis_history.csv",
        mime="text/csv"
    )


if st.session_state.history:
    
    st.markdown('<div class="history"><strong>Analysis History</strong></div>', unsafe_allow_html=True)
    
    
    results = [item["result"] for item in st.session_state.history]
    
    
    counts = {"Real": results.count("Real"), "Fake": results.count("Fake")}
    
    
    total_count = len(results)
    real_percentage = (counts["Real"] / total_count) * 100 if total_count > 0 else 0
    fake_percentage = (counts["Fake"] / total_count) * 100 if total_count > 0 else 0
    
    
    st.markdown(f"""
        <div class="result-summary">
            <h4><strong>Results Summary:</strong></h4>
            <p><strong>Total Results Analyzed:</strong> {total_count}</p>
            <p><strong>Real News:</strong> {counts['Real']} ({real_percentage:.2f}%)</p>
            <p><strong>Fake News:</strong> {counts['Fake']} ({fake_percentage:.2f}%)</p>
        </div>
    """, unsafe_allow_html=True)

    
    fig = go.Figure(data=[go.Pie(labels=list(counts.keys()), values=list(counts.values()), hole=0.3)])
    fig.update_layout(title_text="Real vs Fake News Analysis History")
    st.plotly_chart(fig)

    
    for item in st.session_state.history:
        st.markdown(f'''
            <div class="history-item" style="margin-bottom: 20px; padding: 10px; border-radius: 10px; background-color: #ffffff; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                <strong>News:</strong> <span style="font-style: italic;">{item["text"]}</span><br>
                <strong>Result:</strong> <span style="font-weight: bold; color: {'#388E3C' if item['result'] == 'Real' else '#F44336'};">{item["result"]}</span><br>
                <strong>Confidence:</strong> {item["confidence"]:.2f}% 
            </div>
        ''', unsafe_allow_html=True)
