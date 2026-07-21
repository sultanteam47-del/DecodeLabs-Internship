import speech_recognition as sr
import pyttsx3

import customtkinter as ctk
from datetime import datetime

# ---------------- THEME ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ---------------- WINDOW ----------------
engine = pyttsx3.init()

engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

app = ctk.CTk()
app.title("AI Assistant")
app.geometry("950x720")
app.resizable(False, False)

# ---------------- HEADER ----------------

header = ctk.CTkFrame(
    app,
    height=70,
    fg_color="#5B21B6"
)
header.pack(fill="x")

title = ctk.CTkLabel(
    header,
    text="🤖 AI Assistant",
    font=("Segoe UI",26,"bold"),
    text_color="white"
)

title.pack(side="left",padx=20,pady=18)

status = ctk.CTkLabel(
    header,
    text="🟢 Online",
    font=("Segoe UI",15),
    text_color="white"
)

status.pack(side="right",padx=20)

# ---------------- CHAT BOX ----------------

chat_box = ctk.CTkTextbox(
    app,
    width=850,
    height=520,
    font=("Segoe UI",15),
    corner_radius=15,
    fg_color="#1E1E1E",
    text_color="white"
)

chat_box.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

chat_box.insert(
    "end",
    "🤖 AI Assistant\n\n"
)

chat_box.insert(
    "end",
    "Hello Abdullah 👋\n"
)

chat_box.insert(
    "end",
    "Welcome to Professional AI Chatbot.\n\n"
)

chat_box.configure(state="disabled")
# ---------------- SEND MESSAGE ----------------

def voice_input():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            chat_box.configure(state="normal")
            chat_box.insert("end", "\n🎤 Listening...\n")
            chat_box.configure(state="disabled")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        user_entry.delete(0, "end")
        user_entry.insert(0, text)

        send_message()

    except Exception:

        chat_box.configure(state="normal")
        chat_box.insert("end", "\n❌ Voice not recognized.\n")
        chat_box.configure(state="disabled")

def send_message(event=None):

    message = user_entry.get().strip().lower()

    if message == "":
        return

    chat_box.configure(state="normal")

    chat_box.insert("end", f"\n👤 You: {message}\n")

    if message == "hello":
        reply = "Hello Abdullah! 👋"

    elif message == "hi":
        reply = "Hi! Nice to meet you."

    elif message == "hey":
        reply = "Hey! How can I help you?"

    elif message == "how are you":
        reply = "I'm doing great! 😊"

    elif message == "your name":
        reply = "My name is AI Assistant."

    elif message == "who made you":
        reply = "I was created by Abdullah."

    elif message == "what is ai":
        reply = "AI stands for Artificial Intelligence."

    elif message == "time":
        reply = datetime.now().strftime("%I:%M %p")

    elif message == "date":
        reply = datetime.now().strftime("%d-%m-%Y")

    elif message == "thanks":
        reply = "You're welcome! 😊"

    elif message == "bye":
        reply = "Goodbye Abdullah! 👋"

    else:
        reply = "Sorry! I don't understand."

    chat_box.insert("end", f"🤖 AI: {reply}\n")
    speak(reply)

    chat_box.configure(state="disabled")
    chat_box.see("end")

    user_entry.delete(0, "end")
    # ---------------- INPUT AREA ----------------

bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(fill="x", padx=20, pady=(0,20))

user_entry = ctk.CTkEntry(
    bottom_frame,
    placeholder_text="Type your message...",
    width=560,
    height=45,
    font=("Segoe UI",15)
)
user_entry.pack(side="left", padx=10, pady=10)

voice_button = ctk.CTkButton(
    bottom_frame,
    text="🎤 Speak",
    width=120,
    height=45,
    command=voice_input,
    fg_color="#9333EA",
    hover_color="#7E22CE"
)
voice_button.pack(side="right", padx=10)

send_button = ctk.CTkButton(
    bottom_frame,
    text="Send",
    width=120,
    height=45,
    command=send_message
)
send_button.pack(side="right")

user_entry.bind("<Return>", send_message)

app.mainloop()