import streamlit as st

st.set_page_config(page_title="Passive Practice", page_icon="📝")
st.title("📝 Active to Passive Voice Practice")

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

# Include both base form and past tense keys
irregular_verbs = {
    "eat": "eaten", "ate": "eaten",
    "write": "written", "wrote": "written",
    "see": "seen", "saw": "seen",
    "make": "made", "made": "made",
    "take": "taken", "took": "taken",
    "do": "done", "did": "done",
    "buy": "bought", "bought": "bought",
    "find": "found", "found": "found",
    "send": "sent", "sent": "sent",
    "read": "read", "read": "read",
    "say": "said", "said": "said",
    "go": "gone", "went": "gone",
    "give": "given", "gave": "given"
}

if "index" not in st.session_state:
    st.session_state.index = 0
if "show_passive" not in st.session_state:
    st.session_state.show_passive = False

current = examples[st.session_state.index]
st.markdown(f"### ✏️ Active Sentence: {current}")

def convert_to_passive(sentence):
    words = sentence.strip(".").split()
    if len(words) < 3:
        return None, "❗ This sentence is too short."

    subject = words[0]
    verb = words[1]
    obj = " ".join(words[2:])

    # Check if verb is past
    if verb in irregular_verbs:
        past_participle = irregular_verbs[verb]
        be = "was" if subject.lower() not in ["they", "we", "you"] else "were"
    elif verb.endswith("s"):  # Present tense
        base_verb = verb[:-1]
        past_participle = irregular_verbs.get(base_verb, base_verb + "ed")
        be = "is" if subject.lower() not in ["they", "we", "you"] else "are"
    else:
        return None, "❗ Only simple present or past tense is supported."

    passive = f"{obj.capitalize()} {be} {past_participle} by {subject}."
    explanation = (
        f"➡ Subject = **{subject}**\n"
        f"➡ Verb = **{verb}** → Past participle = **{past_participle}**\n"
        f"➡ Object = **{obj}** → Becomes subject in passive\n"
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

# Show Passive Sentence
if st.session_state.show_passive:
    result, explanation = convert_to_passive(current)
    if result:
        st.markdown(f"### ✅ Passive Voice: {result}")
        st.markdown(f"### 🧠 Explanation:\n{explanation}")
    else:
        st.warning(explanation)
