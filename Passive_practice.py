import streamlit as st
import random

# Page settings
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

# Irregular verb dictionary
irregular_verbs = {
    "eat": "eaten", "write": "written", "see": "seen", "make": "made", "take": "taken",
    "do": "done", "read": "read", "go": "gone", "say": "said", "give": "given",
    "buy": "bought", "find": "found", "send": "sent"
}

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_passive" not in st.session_state:
    st.session_state.show_passive = False

# Current sentence
current = examples[st.session_state.index]

# Display Active Sentence (Large font)
st.markdown(f"### ✏️ Active Sentence: {current}")

# Convert to passive
def convert_to_passive(sentence):
    words = sentence.strip(".").split()
    if len(words) < 3:
        return None, "❗ This sentence is too short."

    subject = words[0]
    verb = words[1]
    obj = " ".join(words[2:])

    # Present tense
    if verb.endswith("s"):
        base_verb = verb[:-1]
        be = "is"
        past_participle = irregular_verbs.get(base_verb, base_verb + "ed")
    # Past tense
    elif verb in irregular_verbs.values() or verb.endswith("ed"):
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

# Buttons (with session state update)
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Show Passive"):
        st.session_state.show_passive = True

with col2:
    if st.button("➡️ Next Sentence"):
        st.session_state.index = (st.session_state.index + 1) % len(examples)
        st.session_state.show_passive = False

# Show passive only if triggered
if st.session_state.show_passive:
    result, explanation = convert_to_passive(current)
    if result:
        st.markdown(f"### ✅ Passive Voice: {result}")
        st.markdown(f"### 🧠 Explanation:\n{explanation}")
    else:
        st.warning(explanation)
