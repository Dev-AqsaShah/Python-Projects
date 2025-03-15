import streamlit as st
import random

st.title("Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    }
] 

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.show_result = False

question = st.session_state.current_question

st.subheader(question["question"])

# User answer selection
selected_option = st.radio("Choose your answer:", question["options"], key="answer")

# Submit Answer
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect! The correct answer is: {question['answer']}")

    # Show result before changing the question
    st.session_state.show_result = True

# Button to go to next question (AFTER user sees result)
if st.session_state.show_result:
    if st.button("Next Question"):
        st.session_state.current_question = random.choice(questions)
        st.session_state.show_result = False
        st.rerun()
