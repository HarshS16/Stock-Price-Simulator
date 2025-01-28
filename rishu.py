import streamlit as st
from time import sleep
import random
import plotly.graph_objects as go
import urllib.parse

# Set up the page configuration
st.set_page_config(page_title="Fake News Detector", layout="wide")

# Adding custom CSS for the modern SaaS design with interactive features
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

# Add title and description
st.markdown('<div class="title">Fake News Detector</div>', unsafe_allow_html=True)
st.markdown("""
    🚨 **Paste a news headline or article below, and let us detect whether it's real or fake!** 
    We use advanced algorithms to detect misinformation. 
""", unsafe_allow_html=True)

# Add a dropdown or radio button for news category (optional)
news_category = st.selectbox(
    "Select the type of news:",
    ["Politics", "Science", "Entertainment", "Sports", "Health"],
    key="category_select"
)

# Initialize the session state for user_input if not already set
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Initialize history if not already set
if "history" not in st.session_state:
    st.session_state.history = []

# Add a text input area for user to enter text (headlines or articles)
user_input = st.text_area(
    "Enter News Text",
    height=150,
    placeholder="Paste your news article or headline here...",
    value=st.session_state.user_input,
    key="news_input",
    help="Paste a news headline or article to analyze"
)

# Update session state when text is entered
if user_input != st.session_state.user_input:
    st.session_state.user_input = user_input

# Add a button for users to trigger fake news detection
if st.button("Check if it's Fake or Real", key="check_button"):
    if user_input:
        # Show a spinner while processing the input
        with st.spinner("Analyzing... Please wait!"):
            sleep(2)  # Simulate a delay for analysis (replace with your actual model prediction)

            # Simulated result for now (replace this with real model output)
            result = random.choice(["Real", "Fake"])  # Randomize the result for now
            confidence = random.uniform(60, 99)  # Simulated confidence score

            # Display the result with dynamic styling based on "Fake" or "Real"
            result_class = "real" if result == "Real" else "fake"
            result_text = "Real" if result == "Real" else "Fake"
            st.markdown(f'<div class="result {result_class}">{"✅" if result == "Real" else "⚠️"} The news is <strong>{result_text}</strong>!</div>', unsafe_allow_html=True)

            # Display confidence score
            st.markdown(f'<div class="confidence">Confidence: {confidence:.2f}%</div>', unsafe_allow_html=True)

            # Add a progress bar for the confidence score
            st.progress(confidence / 100)

            # Save the result in history
            st.session_state.history.append({"text": user_input, "result": result, "confidence": confidence})

            # Clear input field after submission
            st.session_state.user_input = ""

            # Social Media Share
            share_url = f"https://twitter.com/intent/tweet?text=I%20just%20checked%20the%20news%20and%20it%20was%20{result}%20with%20{confidence:.2f}%20confidence%20-%20Fake%20News%20Detector%20%23FakeNewsDetector%20{urllib.parse.quote(user_input)}"
            st.markdown(f'<a href="{share_url}" target="_blank"><button class="stButton"><strong>Share on Twitter</strong></button></a>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="alert">⚠️ Please enter some text to analyze.</div>', unsafe_allow_html=True)

# Option to clear the input using session state
if st.button("Clear Input", key="clear_button"):
    st.session_state.user_input = ""  # Clear the input in session state

# Display history of analyzed news
if st.session_state.history:
    st.markdown('<div class="history"><strong>Analysis History</strong></div>', unsafe_allow_html=True)
    for item in st.session_state.history:
        st.markdown(f'''
            <div class="history-item">
                <strong>News:</strong> {item["text"]} <br>
                <strong>Result:</strong> {item["result"]} <br>
                <strong>Confidence:</strong> {item["confidence"]:.2f}% 
            </div>
        ''', unsafe_allow_html=True)

# Provide tips for identifying fake news
st.markdown("""
    <div class="history">
    <strong>Tips for Identifying Fake News:</strong>
    <ul>
        <li>Check the source: Make sure the news comes from a reputable outlet.</li>
        <li>Verify with multiple sources: Cross-check the same story with other trusted sources.</li>
        <li>Beware of sensational headlines: If it sounds too good to be true, it probably is!</li>
        <li>Check the author and date: Ensure the article is written by a credible author and is up-to-date.</li>
    </ul>
    </div>
""", unsafe_allow_html=True)
