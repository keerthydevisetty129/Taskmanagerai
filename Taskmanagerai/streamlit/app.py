import streamlit as st
import datetime
from transformers import pipeline

# Load simple text-generation model (GPT2)
generator = pipeline("text-generation", model="gpt2")

# Streamlit page setup
st.set_page_config(page_title="🧠 TaskMate AI", layout="centered")
st.title("✅ TaskMate AI")
st.caption("Your AI assistant for managing tasks")

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input from user
user_input = st.text_input("📝 Add a task or ask for a suggestion")

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("➕ Add Task") and user_input:
        st.session_state.tasks.append({
            "task": user_input,
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "done": False
        })
        st.success("Task added!")

with col2:
    if st.button("🤖 Suggest a Task"):
        suggestion = generator("Suggest one productivity task:", max_length=30, num_return_sequences=1)[0]["generated_text"]
        st.info(f"💡 Suggested Task: {suggestion}")

# Show task list
st.subheader("📋 My Tasks")
for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write(f"- {t['task']}  \n🕒 Added on {t['created']}")
    with col2:
        if st.button(f"✅ Done", key=f"done_{i}"):
            st.session_state.tasks.pop(i)
            st.success("Task marked as done.")
            st.experimental_rerun()

st.markdown("---")
st.markdown("Made with 💻 by Keerthy • Powered by Streamlit & Transformers")
