puimport tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

BOT_NAME = "Nerd AI 🔮"

BG, PANEL, CHAT_BG = "#150826", "#241040", "#1e0a38"
ENTRY_BG, USER_BUB, BOT_BUB = "#3a1f66", "#7209b7", "#2d1550"
ACCENT, ACCENT2 = "#f72585", "#b5179e"
TEXT, SUBTLE = "#f5ecff", "#d8b4fe"

def reply_for(raw):
    m = raw.lower().strip()
    if not m: return "Say something, I dare you 🤓"
    rules = [
        (["hi","hello","hey","yo","sup","hola"],
         ["Hello, human! ✨","Hey there! 🧪 Ready to nerd out?","Greetings, traveler of the violet void. 🔮"]),
        (["how are you","how's it going","how r u"], ["Running at 42 THz and vibing in violet. You?"]),
        (["your name","who are you"], [f"I'm {BOT_NAME}, a rule-based oracle of trivia and tie-dye."]),
        (["joke","funny"],
         ["Why did the dev go broke? He used up all his cache. 💸",
          "There are 10 kinds of people: those who get binary and those who don't.",
          "I told my PC I need a break. It said: 'No problem — I'll sleep.' 😴"]),
        (["fact","trivia","tell me something"],
         ["🌌 A day on Venus is longer than its year.",
          "🐙 Octopuses have three hearts and blue blood.",
          "🧠 Your brain uses ~20% of your body's energy.",
          "🍯 Honey never spoils — 3000-year-old jars are still edible."]),
        (["help","what can you do"], ["Try: 'joke', 'fact', 'time', 'date', 'thanks', or just say hi."]),
        (["thank"], ["Anytime! 💜","You're most welcome.","Glad to help ✨"]),
        (["love you"], ["Aww 💜 I'm just rules and vibes, but same."]),
        (["exit","bye","quit"], ["Farewell! May your bugs be few. 🌙"]),
    ]
    for keys, answers in rules:
        if any(k in m for k in keys): return random.choice(answers)
    if "time" in m: return f"⏰ It's {datetime.now().strftime('%I:%M %p')} right now."
    if "date" in m or "day" in m: return f"📅 Today is {datetime.now().strftime('%A, %B %d, %Y')}."
    return random.choice(["Interesting… tell me more. 🤔","No rule for that yet — try 'help'.",
                          "Hmm, my circuits are tie-dyed on that one.","Curious! Ask me for a joke or a fact instead."])

root = tk.Tk()
root.title(BOT_NAME); root.geometry("520x600"); root.configure(bg=BG); root.minsize(400, 480)

# --- Header (top) ---
header = tk.Frame(root, bg=PANEL); header.pack(side=tk.TOP, fill=tk.X, padx=14, pady=(14, 6))
tk.Label(header, text="🔮", font=("Segoe UI Emoji", 20), bg=ACCENT, fg="white",
         width=2, padx=6, pady=2).pack(side=tk.LEFT, padx=10, pady=8)
tw = tk.Frame(header, bg=PANEL); tw.pack(side=tk.LEFT, pady=8)
tk.Label(tw, text=BOT_NAME, font=("Segoe UI", 14, "bold"), bg=PANEL, fg=TEXT).pack(anchor="w")
status = tk.Label(tw, text="● online · rule-based", font=("Segoe UI", 9), bg=PANEL, fg=SUBTLE)
status.pack(anchor="w")
tk.Label(header, text="  v1.2  ", font=("Segoe UI", 8, "bold"),
         bg=ACCENT2, fg="white").pack(side=tk.RIGHT, padx=12)

# --- Input row (packed BOTTOM first so it never disappears) ---
row = tk.Frame(root, bg=PANEL); row.pack(side=tk.BOTTOM, fill=tk.X, padx=14, pady=(6, 14))
entry = tk.Entry(row, font=("Segoe UI", 12), bg=ENTRY_BG, fg=TEXT,
                 insertbackground=TEXT, relief=tk.FLAT)
entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10, ipady=6)
btn = tk.Button(row, text="Send  ✨", font=("Segoe UI", 11, "bold"),
                bg=ACCENT, fg="white", activebackground="#ff5ca8",
                activeforeground="white", relief=tk.FLAT, padx=18, pady=8, cursor="hand2")
btn.pack(side=tk.RIGHT, padx=10, pady=10)

# --- Chips (above input) ---
chips = tk.Frame(root, bg=BG); chips.pack(side=tk.BOTTOM, fill=tk.X, padx=14, pady=(0, 2))

# --- Chat (fills remaining middle) ---
chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 11),
    bg=CHAT_BG, fg=TEXT, state=tk.DISABLED, relief=tk.FLAT,
    padx=14, pady=14, spacing1=4, spacing3=8, borderwidth=0, highlightthickness=0)
chat.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=14, pady=4)
chat.tag_config("bot_name", foreground=SUBTLE, font=("Segoe UI", 9, "bold"), spacing1=6)
chat.tag_config("bot_msg", background=BOT_BUB, foreground=TEXT,
                lmargin1=18, lmargin2=18, rmargin=80, spacing1=2, spacing3=6)
chat.tag_config("user_msg", background=USER_BUB, foreground="white",
                justify=tk.RIGHT, lmargin1=80, lmargin2=80, rmargin=8, spacing3=6)
chat.tag_config("typing", background=BOT_BUB, foreground=SUBTLE,
                font=("Segoe UI", 11, "italic"),
                lmargin1=18, lmargin2=18, rmargin=80, spacing1=2, spacing3=6)

def bubble(text, who):
    chat.config(state=tk.NORMAL)
    if who == "bot":
        chat.insert(tk.END, f"🔮  {BOT_NAME}\n", "bot_name")
        chat.insert(tk.END, f"  {text}  \n\n", "bot_msg")
    else:
        chat.insert(tk.END, f"  {text}  \n\n", "user_msg")
    chat.config(state=tk.DISABLED); chat.see(tk.END)

typing = {"on": False, "job": None, "step": 0}

def animate_typing():
    if not typing["on"]: return
    frames = ["  •      ", "  • •    ", "  • • •  "]
    chat.config(state=tk.NORMAL)
    line = int(chat.index("end-1c").split(".")[0]) - 2
    chat.delete(f"{line}.0", f"{line}.end")
    chat.insert(f"{line}.0", frames[typing["step"] % 3], "typing")
    chat.config(state=tk.DISABLED)
    typing["step"] += 1
    typing["job"] = root.after(350, animate_typing)

def show_typing():
    typing["on"] = True; typing["step"] = 0
    status.config(text="● typing…")
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f"🔮  {BOT_NAME}\n", "bot_name")
    chat.insert(tk.END, "  •    \n\n", "typing")
    chat.config(state=tk.DISABLED); chat.see(tk.END)
    animate_typing()

def hide_typing():
    if not typing["on"]: return
    typing["on"] = False
    if typing["job"]: root.after_cancel(typing["job"]); typing["job"] = None
    status.config(text="● online · rule-based")
    chat.config(state=tk.NORMAL)
    last = int(chat.index("end-1c").split(".")[0])
    chat.delete(f"{last-2}.0", f"{last}.0")
    chat.config(state=tk.DISABLED)

def send(_=None):
    txt = entry.get().strip()
    if not txt or typing["on"]: return "break"
    bubble(txt, "user"); entry.delete(0, tk.END)
    show_typing()
    root.after(700 + min(1600, len(txt) * 40), lambda: after_send(txt))
    return "break"

def after_send(txt):
    hide_typing(); bubble(reply_for(txt), "bot")
    if txt.lower().strip() in ("exit","bye","quit"):
        entry.config(state=tk.DISABLED); btn.config(state=tk.DISABLED)

def quick(t):
    if typing["on"]: return
    entry.delete(0, tk.END); entry.insert(0, t); send()

entry.bind("<Return>", send)
btn.config(command=send)

for c in ("😂 Joke", "🌌 Fact", "⏰ Time", "❓ Help"):
    tk.Button(chips, text=c, command=lambda x=c.split(" ",1)[1]: quick(x),
              font=("Segoe UI", 9, "bold"), bg=ENTRY_BG, fg=SUBTLE,
              activebackground=ACCENT2, activeforeground="white",
              relief=tk.FLAT, padx=12, pady=5, cursor="hand2"
              ).pack(side=tk.LEFT, padx=(0,6), pady=4)

bubble('Hello! 💜 Ask me for a joke, a fact, or say hi. Type "exit" to leave.', "bot")
entry.focus()
root.mainloop()
