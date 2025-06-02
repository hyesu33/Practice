import streamlit as st
import random

# Set page
st.set_page_config(page_title="Passive Practice", page_icon="📝")
st.title("📝 Active to Passive Voice Practice")

# Example sentences
examples = [
    "Tom eats an apple.",
    "She wrote a letter.",
    "They make cookies.",
    "He buys a car.",
    "We saw a movie.",
    "I took a picture.",
    "You did the homework.",
    "The chef made a cake."
]

# Irregular verbs
irregular_verbs = {
    "eat": "eaten", "write": "written", "see": "seen", "make": "made", "take": "taken",
    "do": "done", "read": "read", "go": "gone", "say": "said", "give": "given",
    "buy": "bought", "find": "found", "send": "sent"
}

# Initialize index
if "index" not in st.session_state:
    st.session_state.index = 0

# Get current sentence
current = examples[st.session_state.index]
st.markdown(f"## ✏️ Active Sentence: {current}")  # Enlarged size

# Passive conversion function
def convert_to_passive(sentence):
    words = sentence.strip(".").split()
    if len(words) < 3:
        return None, "❗ This sentence is too short."

    subject = words[0]
    verb = words[1]
    obj = " ".join(words[2:])

    # Determine tense
    if verb.endswith("s"):  # Present
        base_verb = verb[:-1]
        be = "is"
        past_participle = irregular_verbs.get(base_verb, base_verb + "ed")
    elif verb in irregular_verbs.values() or verb.endswith("ed"):  # Past
        base_verb = verb
        be = "was"
        past_participle = verb if verb in irregular_verbs.values() else base_verb
    else:
        return None, "❗ Only simple present or past tense is supported."

    passive = f"{obj.capitalize()} {be} {past_participle} by {subject}."
    explanation = (
        f"➡ Subject = **{subject}**\n"
        f"➡ Verb = **{verb}** → Past participle = **{past_participle}**\n"
        f"➡ Object = **{obj}** → Becomes subject in passive\n"
        f"➡ Passive = **{obj.capitalize()} {be} {past_participle} by {subject}.**"
    )

    return passive, explanation

# Show Passive button
if st.button("🔄 Show Passive"):
    result, explanation = convert_to_passive(current)
    if result:
        st.markdown(f"### ✅ Passive Voice:\n**{result}**")
        st.markdown(f"### 🧠 Explanation:\n{explanation}")
    else:
        st.warning(explanation)

# Next Sentence button
if st.button("➡️ Next Sentence"):
    st.session_state.index = (st.session_state.index + 1) % len(examples)
    st.experimental_rerun()
