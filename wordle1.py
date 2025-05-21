import streamlit as st
import random

core_words = {
    "magic": "a special power that makes impossible things happen",
    "library": "a place where you can read or borrow books",
    "adventure": "an exciting or unusual experience",
    "secret": "something that you do not tell other people",
    "listen": "to pay attention to sounds or words",
    "sneak": "to go somewhere quietly and secretly"
}

word_list = [
    "magic", "library", "adventure", "secret", "listen", "sneak",
    "midnight", "character", "alice", "rabbit", "pirate",
    "council", "tale", "wisdom", "borrow", "story", "lover",
    "curious", "clock", "page", "amaze", "change", "return"
]

if 'answer' not in st.session_state:
    st.session_state.answer = random.choice(list(core_words.keys()))
    st.session_state.definition = core_words[st.session_state.answer]
    st.session_state.attempts = 0
    st.session_state.max_attempts = 6
    st.session_state.guessed = False

def compare_words(guess, answer):
    result = []
    for i in range(len(guess)):
        if i < len(answer) and guess[i] == answer[i]:
            result.append("🟩")
        elif guess[i] in answer:
            result.append("🟨")
        else:
            result.append("⬛")
    return "".join(result)

st.title("Wordle Game")
st.write(f"Hint: Definition - {st.session_state.definition}")
st.write(f"The word has {len(st.session_state.answer)} letters.")
st.write(f"You have {st.session_state.max_attempts - st.session_state.attempts} attempts left.")

guess = st.text_input("Enter your guess:")

if st.button("Submit") and guess:
    guess = guess.lower()
    if guess not in word_list:
        st.warning("Please guess a valid word from the list.")
    elif st.session_state.guessed:
        st.info("You already guessed the word! Please restart the app to play again.")
    else:
        st.session_state.attempts += 1
        feedback = compare_words(guess, st.session_state.answer)
        st.write(f"Result: {feedback}")
        if guess == st.session_state.answer:
            st.success(f"Correct! The word is '{st.session_state.answer.upper()}'.")
            st.write(f"Meaning: {st.session_state.definition}")
            st.session_state.guessed = True
        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.error(f"Sorry, you used all attempts. The word was '{st.session_state.answer.upper()}'.")
            st.write(f"Meaning: {st.session_state.definition}")
            st.session_state.guessed = True
