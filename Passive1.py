# 목적격 변환 딕셔너리 추가
subject_to_object = {
    "I": "me", "you": "you", "he": "him", "she": "her", "it": "it",
    "we": "us", "they": "them",
    "Tom": "Tom", "John": "John", "Mary": "Mary",  # 이름은 그대로
}

def convert_to_passive(sentence):
    sentence = sentence.strip().rstrip(".")
    words = sentence.split()

    # 주어, 동사, 목적어 분리
    if words[0].lower() in ["the", "a", "an"]:
        subject = f"{words[0]} {words[1]}"
        verb = words[2]
        obj_words = words[3:]
    else:
        subject = words[0]
        verb = words[1]
        obj_words = words[2:]

    obj = " ".join(obj_words)
    subject_lower = subject.lower()
    plural_subjects = ["they", "we", "you"]
    is_plural = any(plural in subject_lower for plural in plural_subjects)

    # 동사 형태 결정
    if verb in past_to_pp:
        be = "were" if is_plural else "was"
        past_participle = past_to_pp[verb]
    elif verb.endswith("s"):
        base = verb[:-1]
        be = "are" if is_plural else "is"
        past_participle = base_to_pp.get(base, base + "ed")
    elif verb.endswith("ed"):
        be = "were" if is_plural else "was"
        past_participle = verb
    else:
        return None, f"❗ Unknown verb: '{verb}'"

    # 주어 목적격으로 변환
    subject_key = subject.strip().capitalize()
    object_form = subject_to_object.get(subject_key, subject)

    # 최종 수동태 문장
    passive = f"{obj.capitalize()} {be} {past_participle} by {object_form}."
    explanation = (
        f"➡ Subject = **{subject}** → **by {object_form}** (objective form)\n"
        f"➡ Verb = **{verb}** → Past participle = **{past_participle}**\n"
        f"➡ Object = **{obj}** → becomes the subject in passive\n"
        f"➡ Passive = **{passive}**"
    )
    return passive, explanation
