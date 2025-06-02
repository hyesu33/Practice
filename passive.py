import streamlit as st
import spacy

# Load the English model (make sure it's installed: en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

st.set_page_config(page_title="Active to Passive Converter", page_icon="📝")
st.title("📝 Active to Passive Voice Converter")
st.write("This app converts a basic active voice sentence into passive voice. It works best with simple present and past tense sentences.")

# Input from user
user_input = st.text_input("👉 Enter an active voice sentence (e.g., 'Tom eats an apple.')")

# Function to convert active to passive
def convert_to_passive(sentence):
    doc = nlp(sentence)

    subject = None
    verb = None
    dobj = None

    for token in doc:
        if token.dep_ == "nsubj":
            subject = token
        elif token.dep_ == "dobj":
            dobj = token
        elif token.pos_ == "VERB":
            verb = token

    if subject and verb and dobj:
        # Determine tense
        tense = "present"
        if verb.tag_ in ["VBD", "VBN"]:
            tense = "past"

        # Choose correct be-verb
        be_verb = "is" if tense == "present" else "was"

        # Handle irregular past participles
        irregulars = {
            "eat": "eaten", "write": "written", "see": "seen",
            "make": "made", "take": "taken", "do": "done",
            "read": "read", "go": "gone", "say": "said", "give": "given"
        }
        past_participle = irregulars.get(verb.lemma_, verb.lemma_ + "ed")

        # Build passive sentence
        passive_sentence = f"{dobj.text.capitalize()} {be_verb} {past_participle} by {subject.text}."

        # Explanation
        explanation = (
            f"➡ **'{subject.text}'** is the subject.\n"
            f"➡ **'{verb.text}'** is the verb (tense: {tense}).\n"
            f"➡ **'{dobj.text}'** is the object and becomes the new subject in passive voice.\n"
            f"➡ We use **'{be_verb}' + '{past_participle}'** to form the passive verb.\n"
            f"➡ Finally, we add '**by {subject.text}**' to show who did the action."
        )

        return passive_sentence, explanation
    else:
        return None, "❗ This sentence might be too complex. Please try a simple one like 'She wrote a letter.'"

# Show result only when button is clicked
if st.button("🔄 Convert to Passive Voice"):
    if user_input:
        passive, exp = convert_to_passive(user_input)
        if passive:
            st.markdown(f"### ✅ Passive Voice:\n**{passive}**")
        st.markdown(f"### 🧠 Explanation:\n{exp}")
    else:
        st.warning("Please enter a sentence first.")
