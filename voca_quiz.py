import streamlit as st
import random

# Vocabulary dictionary (word: meaning)
vocab = {
    "library": "도서관",
    "character": "성격",
    "midnight": "밤 열두시",
    "rumor": "소문",
    "adventure": "모험",
    "whisper": "속삭이다"
}

# Shuffle and select 5 random questions
quiz_items = random.sample(list(vocab.items()), 5)

# App title
st.title("📚 Vocabulary Quiz Game")

# Session state for tracking progress
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.answers = []

# Show quiz if not finished
if st.session_state.step < len(quiz_items):
    current_word, current_meaning = quiz_items[st.session_state.step]

    st.subheader(f"Question {st.session_state.step + 1} of {len(quiz_items)}")
    st.write(f"**Meaning:** {current_meaning}")
    answer = st.text_input("Enter the English word:", key=st.session_state.step)

    if st.button("Submit"):
        if answer.strip().lower() == current_word.lower():
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer was **{current_word}**.")
        st.session_state.step += 1

else:
    st.subheader("🎉 Quiz Finished!")
    st.write(f"Your score: **{st.session_state.score} / {len(quiz_items)}**")
    if st.button("Play Again"):
        st.session_state.step = 0
        st.session_state.score = 0
