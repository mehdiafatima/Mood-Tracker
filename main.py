import streamlit as st
import pandas as pd
import datetime
import csv
import os
import matplotlib.pyplot as plt

# Constants
MOOD_FILE = 'mood_log.csv'

# Mood Messages & Colors
mood_data = {
    "Happy": {"msg": "Stay happy and spread the joy! 😊", "color": "#FFD700"},
    "Neutral": {"msg": "Feeling neutral? Take a deep breath and enjoy the moment. 😌", "color": "#B0C4DE"},
    "Sad": {"msg": "It's okay to be sad. Remember, this too shall pass. ❤️", "color": "#4682B4"},
    "Angry": {"msg": "Don't be angry, bruh! Take a deep breath and let it go. 😤➡️😌", "color": "#FF4500"},
    "Stressed": {"msg": "You're strong! Take a break, sip some tea, and relax. ☕", "color": "#FF8C00"},
    "Tired": {"msg": "Rest up, champ! Your energy will bounce back soon. 😴", "color": "#778899"},
    "Excited": {"msg": "Woohoo! Ride the excitement wave and make today awesome! 🎉", "color": "#32CD32"},
    "Anxious": {"msg": "Breathe in... Breathe out... Everything will be okay. 🌿", "color": "#20B2AA"},
    "Depressed": {"msg": "You're not alone. Reach out, talk, and take things one step at a time. 💙", "color": "#4B0082"},
    "Other": {"msg": "Whatever you're feeling, it's valid. Take care of yourself! 💖", "color": "#DDA0DD"}
}

# Functions
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=['Date', 'Mood'])
    data = pd.read_csv(MOOD_FILE, names=['Date', 'Mood'], header=None, encoding='utf-8')
    return data

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Custom Styling with CSS
st.markdown("""
    <style>
        .title-text {
            color: #ffffff;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }
        .stButton > button {
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            color: white;
            font-weight: bold;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
            border: none;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            color: white;
        }
        .stAlert {
            border-radius: 10px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title with Animation
st.markdown('<h1 class="title-text">Mood Tracker</h1>', unsafe_allow_html=True)
st.write("Log your mood and track your emotions over time.")

# User Input
date = st.date_input("📅 Select Date:", datetime.date.today())
mood = st.selectbox("😃 Select your mood:", list(mood_data.keys()))

if st.button("💾 Log Mood"):
    save_mood_data(date, mood)
    st.success(f"✅ Mood logged for {date} as {mood}!")
    st.info(mood_data[mood]["msg"])

# Load data
data = load_mood_data()

if not data.empty:
    st.subheader("📊 Mood Trends Over Time")

    # Convert date to datetime format
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # Count occurrences of each mood
    mood_counts = data.groupby('Mood').count()["Date"]
    st.bar_chart(mood_counts)

st.markdown("""
    <hr style="border: 2px solid #ddd;">
    <h2 style="text-align: center;">Mood-Based Fun Corner!</h2>
    <p style="text-align: center;">Your mood, your treat! Check out these fun surprises:</p>
    <ul>
        <li>😊 <b>Feeling Happy?</b> *Why don’t skeletons fight each other? Because they don’t have the guts!* 😂</li>
        <li>😐 <b>Neutral?</b> Flip a virtual coin and let fate decide your next adventure! 🪙</li>
        <li>😢 <b>Sad?</b> <a href='https://www.youtube.com/results?search_query=cute+funny+animals' target='_blank'>Watch a cute animal video! 🐶🐱</a></li>
        <li>😡 <b>Angry?</b> <a href='https://www.puffgames.com/bubblewrap/' target='_blank'>Smash virtual bubble wrap! 💥</a></li>
        <li>😪 <b>Tired?</b> *Did you know that octopuses have three hearts?* 🐙💙</li>
        <li>🤩 <b>Excited?</b> Click the button below to unleash a virtual confetti party! 🎊</li>
    </ul>
""", unsafe_allow_html=True)

if st.button("🎊 Confetti Party!"):
    st.snow()

# Mini Games & Fun Links
st.markdown("""
    ---
    ### 🎮 Mini Games & Fun Links
    - **Test Your Reflexes!** [Play a quick reaction game](https://humanbenchmark.com/tests/reactiontime/) ⏳
    - **Silly Doodles!** [Make AI draw something funny](https://quickdraw.withgoogle.com/) ✏️
    - **Solve a Riddle!** What has keys but can’t open locks? *A piano!* 🎹
    - **Random Meme Generator:** [Click here for instant laughs](https://imgflip.com/memegenerator) 😂
    ---
""", unsafe_allow_html=True)

# Useless But Fun Facts
st.markdown("""
    ### 😂 Useless But Fun Facts!
    - Did you know that pigs can't look up into the sky?😜
    - A group of flamingos is called a **flamboyance**! 🦩✨
    - Octopuses have three hearts, and two of them stop beating when they swim. 🐙
    ---
""", unsafe_allow_html=True)

# Your Mood, Your Theme Song
st.markdown("""
    ### 🎶 Your Mood, Your Theme Song!
    - **Feeling happy?** Listen to *Happy* by Pharrell Williams 🎵
    - **Feeling meh?** Try *Here Comes the Sun* by The Beatles 🌞
    - **Feeling sad?** Play *Don’t Worry, Be Happy* by Bobby McFerrin 🎶
    - **Feeling tired?** Wake up with *Eye of the Tiger* by Survivor 🐅
    ---
""", unsafe_allow_html=True)

st.markdown("""
    <hr style="border: 2px solid #ddd;">
    <p style="text-align: center;">❤️ See you again soon! Your mood matters, and so do you! ❤️</p>
""", unsafe_allow_html=True)
