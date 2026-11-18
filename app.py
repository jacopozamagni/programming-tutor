import streamlit as st

from test_api import check_code, explain_concept, generate_exercise, is_correct_feedback

st.set_page_config(page_title="Python Tutor", page_icon="🐍", layout="wide")


def clear_feedback():
    """Forget the old review when the learner edits the code."""
    st.session_state["feedback"] = None
    st.session_state["hint_count"] = 0


with st.sidebar:
    st.title("🐍 Python Tutor")
    st.markdown("Learn Python one small step at a time.")
    st.divider()
    st.markdown(
        """
        **How to use it**
        1. Explain a concept.
        2. Generate an exercise.
        3. Write your code and ask for a hint.
        """
    )
    st.divider()
    st.info(
        "This app uses AI. Always check the explanations, examples and feedback yourself."
    )
    if st.button("Start over", use_container_width=True):
        st.session_state.clear()
        st.rerun()

tab1, tab2, tab3 = st.tabs(["Explain Concept", "Generate Exercise", "Check Code"])

with tab1:
    st.header("Explain a concept")
    st.caption("Type any Python topic, from variables to recursion.")
    concept = st.text_input(
        "Python concept",
        placeholder="e.g. for loops, dictionaries, recursion",
        key="concept_input",
    )
    if st.button("Explain", type="primary"):
        if not concept.strip():
            st.warning("Please enter a concept to explain.")
        else:
            with st.spinner("Explaining..."):
                st.session_state["explanation"] = explain_concept(concept.strip())

    if st.session_state.get("explanation"):
        st.divider()
        st.markdown(st.session_state["explanation"])
        if st.button("Use this concept as exercise topic"):
            st.session_state["exercise_topic"] = concept.strip()
            st.rerun()

with tab2:
    st.header("Generate an exercise")
    st.caption("Each new exercise avoids repeating the previous one.")
    topic_col, level_col = st.columns([3, 1])
    with topic_col:
        topic = st.text_input(
            "Python topic",
            placeholder="e.g. lists, loops, functions",
            key="exercise_topic",
        )
    with level_col:
        level = st.selectbox(
            "Level",
            ["Beginner", "Intermediate", "Advanced"],
            key="level_select",
        )

    if st.button("Generate exercise", type="primary"):
        if not topic.strip():
            st.warning("Please enter a topic to generate an exercise.")
        else:
            st.session_state["feedback"] = None
            st.session_state["hint_count"] = 0
            st.session_state["checked_code"] = None
            st.session_state["code_input"] = ""
            previous_exercise = st.session_state.get("previous_exercise")
            with st.spinner("Generating exercise..."):
                exercise = generate_exercise(
                    topic=topic.strip(),
                    level=level.lower(),
                    previous_exercise=previous_exercise,
                )
            if "**exercise**" in exercise:
                st.session_state["previous_exercise"] = exercise
            else:
                st.warning("The tutor couldn't generate an exercise. Try again.")

    if st.session_state.get("previous_exercise"):
        st.divider()
        st.markdown(st.session_state["previous_exercise"])

with tab3:
    st.header("Check your code")
    exercise = st.session_state.get("previous_exercise")
    if not exercise:
        st.info("Generate an exercise first in the **Generate Exercise** tab.")
    else:
        with st.expander("Current exercise", expanded=True):
            st.markdown(exercise)

        code = st.text_area(
            "Your Python code",
            height=220,
            placeholder="Paste or write your solution here...",
            key="code_input",
            on_change=clear_feedback,
        )

        if st.button("Check my code", type="primary"):
            if not code.strip():
                st.warning("Please enter your code to check.")
            else:
                with st.spinner("Checking your code..."):
                    st.session_state["feedback"] = check_code(exercise, code)
                    st.session_state["checked_code"] = code
                st.session_state["hint_count"] = 0

        feedback = st.session_state.get("feedback")
        if feedback:
            st.divider()
            correct = is_correct_feedback(feedback)
            if correct:
                st.success("This looks correct. Nice work!")
            st.markdown(feedback)

            has_review = "**what to fix**" in feedback
            if has_review and not correct:
                hint_count = st.session_state.get("hint_count", 0)
                if hint_count < 3:
                    if st.button("Get another hint"):
                        with st.spinner("Thinking of a more specific hint..."):
                            st.session_state["feedback"] = check_code(
                                exercise,
                                st.session_state.get("checked_code") or code,
                                previous_feedback=feedback,
                            )
                        st.session_state["hint_count"] = hint_count + 1
                        st.rerun()
                    st.caption(f"Hint {hint_count + 1} of 3")
                else:
                    st.info(
                        "That was the last hint. Try the exercise again with what you've learned."
                    )

st.divider()
st.caption(
    "Made by Jacopo · Powered by Groq · The tutor can make mistakes, always check the answers."
)
