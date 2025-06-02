import streamlit as st

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

# Verb forms: past → past participle
past_to_pp = {
    "ate": "eaten", "wrote": "written", "saw": "seen", "made": "made",
    "took": "taken", "did": "done", "bought": "bought", "found": "found",
    "sent": "sent", "read": "read", "said": "said", "went": "gone", "gave": "given"
}

# Base → past participle
base_to_pp = {
    "eat": "eaten", "write": "written", "see": "seen", "make": "made",
    "take": "taken", "do": "done", "buy": "bought", "find": "found",
    "send": "sent", "read": "read", "say": "said", "go": "gone", "give": "given"
}

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_passive" not in st.session_state:
    st.session_state.show_passive = False

# Get current sentence
current = examples[st.session_state.index]
st.markdown(f"### ✏️ Active Sentence: {current}")

def convert_to_passive(sentence):
    words = sentence.strip(".").split()
    if len(words) < 3:
        return None, "❗ Not enough words to analyze."

    subject = words[0]
    verb = words[1]
    obj = " ".join(words[2:])

    # Subject for be verb agreement
    subject_lower = subject.lower()
    plural_subjects = ["they", "we", "you"]

    # Handle past tense
    if verb in past_to_pp:
        be = "were" if subject_lower in plural_subjects else "was"
        past_participle = past_to_pp[verb]

    # Handle present tense (3rd person singular with 's')
    elif verb.endswith("s"):
        base_verb = verb[:-1]
        be = "are" if subject_lower in plural_subjects else "is"
        past_participle = base_to_pp.get(base_verb, base_verb + "ed")

    # Support regular past tense (e.g., "watched" → "watched")
    elif verb.endswith("ed"):
        be = "were" if subject_lower in plural_subjects else "was"
        past_participle = verb

    else:
        return None, f"❗ Unknown verb form: '{verb}'."

    passive = f"{obj.capitalize()} {be} {past_participle} by {subject}."
    explanation = (
        f"➡ Subject = **{subject}**\n"
        f"➡ Verb = **{verb}** → Past participle = **{past_participle}**\n"
        f"➡ Object = **{obj}** → becomes the subject in passive\n"
        f"➡ Passive = **{passive}**"
    )
    return passive, explanation

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Show Passive"):
        st.session_state.show_passive = True
with col2:
    if st.button("➡️ Next Sentence"):
        st.session_state.index = (st.session_state.index + 1) % len(examples)
        st.session_state.show_passive = False

# Display passive voice if selected
if st.session_state.show_passive:
    result, explanation = convert_to_passive(current)
    if result:
        st.markdown(f"### ✅ Passive Voice: {result}")
        st.markdown(f"### 🧠 Explanation:\n{explanation}")
    else:
        st.warning(explanation)
