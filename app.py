import streamlit as st

st.title("🤖 AI Problem Solver Chatbot")

def bot(text):
    text = text.lower()

    if "stress" in text:
        return "Take rest 😌 and break tasks into small steps"
    elif "study" in text:
        return "Make timetable 📚 and revise daily"
    elif "career" in text:
        return "Focus on skills 💼 and projects"
    elif "sad" in text:
        return "You are strong 💙 things will improve"
    else:
        return "Tell me more details 🤖"

user = st.text_input("You:")
if user:
    st.write(bot(user))
