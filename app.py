from test_api import explain_concept, generate_exercise, check_code
import streamlit as st

st.set_page_config(page_title="Python Tutor", page_icon="🐍", layout="wide")
st.caption("This tool runs using AI, always check the answers")
with st.sidebar:
    st.title("Python Tutor")
    st.markdown(
        """
        This app helps you learn Python by explaining concepts, generating exercises, and checking your code.
        """
    )
    st.divider()
    st.text("You can use the tabs above to navigate between explaining concepts, generating exercises, and checking your code.")
    st.divider()
    st.info("**Note:** This app uses AI to generate explanations and exercises. Always verify the answers and code provided.")
tab1, tab2, tab3 = st.tabs(["Explain Concept", "Generate Exercise", "Check Code"])
st.divider()
st.caption("Made by Jacopo · Powered by Groq · The tutor can make mistakes, always check the answers.")

with tab1:
    st.header("Explain Concept")
    concept = st.text_input("Enter a Python concept to explain:", key="concept_input")
    if st.button("Explain"):
        if not concept.strip():
            st.warning("Please enter a concept to explain.")
        else:
            with st.spinner("Explaining..."):
                explanation = explain_concept(concept.strip())
            st.session_state["explanation"] = explanation
            if "**definition**" in explanation:
                st.session_state["topic_input"] = concept.strip()
    if st.session_state.get("explanation"):
        st.markdown(st.session_state["explanation"])

with tab2:
    st.header("Generate Exercise")
    topic = st.text_input("Enter a Python topic for the exercise:", key="topic_input")
    level = st.selectbox("Select the level of difficulty:", ["Beginner", "Intermediate", "Advanced"], key="level_select")
    if st.button("Generate"):
        if not topic.strip():
            st.warning("Please enter a topic to generate an exercise.")
        else:
            with st.spinner("Generating exercise..."):
                exercise = generate_exercise(
                    topic=topic.strip(),
                    level=level.lower(),
                    previous_exercise=st.session_state.get("previous_exercise"),
                )
            if "**exercise**" in exercise:
                st.session_state["previous_exercise"] = exercise
            else:
                st.warning("The tutor couldn't generate an exercise. Try again.")
    if st.session_state.get("previous_exercise"):
        st.markdown(st.session_state["previous_exercise"])

with tab3:
    st.header("Check Code")
    exercise = st.session_state.get("previous_exercise")
    if exercise:
        st.markdown(exercise)
    code = st.text_area("Enter your Python code:", key="code_input")
    if st.button("Check"):
        if not exercise:
            st.warning("Please generate an exercise first in the 'Generate Exercise' tab.")
        elif not code.strip():
            st.warning("Please enter your code to check.")
        else:
            with st.spinner("Checking code..."):
                st.session_state["feedback"] = check_code(exercise, code)
    if st.session_state.get("feedback"):
        st.markdown(st.session_state["feedback"])