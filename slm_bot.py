name = input("😃 Hi, what is your name? ")
print(f"✨ Welcome, {name}! ✨")

mood = input("How are you today? 🙂 ").strip().lower()

if any(word in mood for word in ["good", "fine", "great", "well","nice"]):
    print(f"🌸 That's great, {name}! I'm glad you're feeling good.")
elif any(word in mood for word in ["tired", "exhausted", "sick", "unwell"]):
    print(f"😴 Take care, {name}. Rest well and get better soon.")
elif any(word in mood for word in ["happy", "joyful", "glad", "cheerful"]):
    print(f"🎉 That's wonderful, {name}! I hope your happiness continues.")
elif any(word in mood for word in ["sad", "upset", "angry", "depressed"]):
    print(f"🤗 Stay strong, {name}. Better days are coming, God willing.")
elif any(word in mood for word in ["so-so", "not bad"]):
    print(f"🙂 Hope your day gets better, {name} and becomes more beautiful.")
elif any(word in mood for word in ["kizeft"]):
    print(f"💀 iwa sir t3awed lmohkek a {name}.")
else:
    print(f"🌟 Wishing you a wonderful day, {name}, no matter how you feel.")

# السؤال دائما خارج أي شرط
answer = input(f"Do you want something, {name}? ").strip().lower()

if answer in ["yes", "y"]:
    print("sir 3end chatgpt")
else:
    print("iwa meziyan 7itax kent ghadi n9em3ek")