
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

answer = random.choice(list(core_words.keys()))
definition = core_words[answer]
answer_len = len(answer)

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

print(f"🎯 Welcome to Wordle! Guess the word.")
print(f"Hint: Definition - {definition}")
print(f"The word has {answer_len} letters.")
print("You have 6 attempts.\n")

max_attempts = 6

for attempt in range(max_attempts):
    guess = input(f"Attempt {attempt+1}: Enter your guess: ").lower()
    if guess not in word_list:
        print("⚠️ Please guess a valid word from the list.\n")
        continue
    feedback = compare_words(guess, answer)
    print("Result:", feedback)
    if guess == answer:
        print(f"\n✅ Correct! The word is '{answer.upper()}'.")
        print(f"📘 Meaning: {definition}")
        break
else:
    print(f"\n❌ Sorry, you used all attempts. The word was '{answer.upper()}'.")
    print(f"📘 Meaning: {definition}")
