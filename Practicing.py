import streamlit as st

# App settings
st.set_page_config(page_title="Passive Practice", page_icon="📝")
st.title("📝 Active to Passive Voice Practice")

# 문장 목록
examples = [
    "Tom eats an apple.",
    "She wrote a letter.",
    "They make cookies.",
    "He buys a car.",
    "We saw a movie.",
    "I took a picture.",
    "You did the homework.",
    "The chef made a cake.",
    "A student found the book.",
    "The teacher sent a message."
]

# 과거형 -> 과거분사
past_to_pp = {
    "ate": "eaten", "wrote": "written", "saw": "seen", "made": "made",
    "took": "taken", "did": "done", "bought": "bought", "found": "found",
    "sent": "sent", "read": "read", "said": "said", "went": "gone", "gave": "given"
}

# 현재형 -> 과거분사
base_to_pp = {
    "eat": "eaten", "write": "written", "see": "seen", "make": "made",
    "take": "taken", "do": "done", "buy": "bought", "find": "found",
    "send": "sent", "read": "read", "say": "said", "go": "gone", "give": "given",
    "buy": "bought", "find": "found", "send": "sent"
}

# 초기 상태 설정
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_passive" not in st.session_state:
    st.session_state.show_passive = False

# 현재 문장
current_sentence = examples[st.session_state.index]

# UI 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Show Passive"):
        st.session_state.show_passive = True
with col2:
    if st.button("➡️ Next Sentence"):
        st.session_state.index = (st.session_state.index + 1) % len(examples)
        st.session_state.show_passive = False

# 문장 크게 출력
st.markdown(f"<h3 style='font-size: 28px;'>✏️ Active Sentence: {current_sentence}</h3>", unsafe_allow_html=True)

# 문장 분석 함수
def convert_to_passive(sentence):
    sentence = sentence.strip().rstrip(".")
    words = sentence.split()

    # 관사 제거된 주어/목적어 만들기 위해 전체 리스트에서 조사
    # 주어: 첫 1~2단어 (The chef, A student 등)
    if words[0].lower() in ["the", "a", "an"]:
        subject = f"{words[0]} {words[1]}"
        verb = words[2]
        obj_words = words[3:]
    else:
        subject = words[0]
        verb = words[1]
        obj_words = words[2:]

    obj = " ".join(obj_words)

    # 수동태 만들기
    subject_lower = subject.lower()
    plural_subjects = ["they", "we", "you"]
    is_plural = any(plural in subject_lower for plural in plural_subjects)

    # 동사 분석
    if verb in past_to_pp:
        be = "were" if is_plural else "was"
        past_participle = past_to_pp[verb]
    elif verb.endswith("s"):  # 현재형
        base = verb[:-1]
        be = "are" if is_plural else "is"
        past_participle = base_to_pp.get(base, base + "ed")
    elif verb.endswith("ed"):
        be = "were" if is_plural else "was"
        past_participle = verb
    else:
        return None, f"❗ Unknown verb: '{verb}'"

    # 결과 문장
    passive = f"{obj.capitalize()} {be} {past_participle} by {subject}."
    explanation = (
        f"➡ Subject = **{subject}**\n"
        f"➡ Verb = **{verb}** → Past participle = **{past_participle}**\n"
        f"➡ Object = **{obj}** → becomes the subject in passive\n"
        f"➡ Passive = **{passive}**"
    )
    return passive, explanation

# 수동태 보여주기
if st.session_state.show_passive:
    result, explanation = convert_to_passive(current_sentence)
    if result:
        st.markdown(f"<h3 style='font-size: 28px;'>✅ Passive Voice: {result}</h3>", unsafe_allow_html=True)
        st.markdown(f"### 🧠 Explanation:\n{explanation}")
    else:
        st.warning(explanation)
