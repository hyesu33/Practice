
'''
import random
import ipywidgets as widgets
from IPython.display import display, clear_output

questions = [
    {"q": "Sarah sneaks into the library during the day.", "a": False, "e": "She sneaks in at night."},
    {"q": "The library in Willowby is said to be enchanted.", "a": True, "e": "It is rumored to be enchanted."},
    {"q": "At midnight, the characters in the books come to life.", "a": True, "e": "They whisper and step out of pages."},
    {"q": "Sarah met Harry Potter in the Midnight Library.", "a": False, "e": "She met Alice and pirates, not Harry Potter."},
    {"q": "The characters return to their pages at dawn.", "a": True, "e": "They return as dawn approaches."}
]

random.shuffle(questions)
answers = [None] * len(questions)
idx = [0]

q_text = widgets.HTML()
choice = widgets.RadioButtons(options=["True", "False"])
submit = widgets.Button(description="Submit")
feedback = widgets.Output()
nav = widgets.HBox()
prev = widgets.Button(description="◀")
next_ = widgets.Button(description="▶")
score_btn = widgets.Button(description="Show Score", button_style='success')

def update():
    i = idx[0]
    q_text.value = f"<b>Q{i+1}/{len(questions)}:</b> {questions[i]['q']}"
    choice.value = None if answers[i] is None else "True" if answers[i] else "False"
    feedback.clear_output()

def on_submit(b):
    i = idx[0]
    ans = choice.value
    if ans is None: return
    answers[i] = (ans == "True")
    correct = questions[i]["a"]
    with feedback:
        clear_output()
        if answers[i] == correct:
            print("✅ Correct!")
        else:
            print("❌ Incorrect.")
        print("💡", questions[i]["e"])

def on_prev(b): idx[0] = max(0, idx[0]-1); update()
def on_next(b): idx[0] = min(len(questions)-1, idx[0]+1); update()

def on_score(b):
    score = sum([a == q["a"] for a, q in zip(answers, questions) if a is not None])
    with feedback:
        clear_output()
        print(f"🏁 Your score: {score} / {len(questions)}")

submit.on_click(on_submit)
prev.on_click(on_prev)
next_.on_click(on_next)
score_btn.on_click(on_score)

nav.children = [prev, next_, score_btn]
display(q_text, choice, submit, feedback, nav)
update()
'''
