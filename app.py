# streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project",page_icon="⭐")
st.title("Growth Mindset challenge:Web App With steamlit")

st.header("🚀Welcome to your Growth Journey!")
st.write("Embrace challenges,learn from mistakes, and unlock your  full potential.This AI-powered app helps you build a growth mindset with reflection,challenges, and achievements!🌟")

# quote section
st.header("💡Today's Growth Mindset quote")
st.write("❝Success is not final,failure, is not fatal:it is the courage to continue that counts.❞-Winstow churchill")

st.header("🔧What's your Challenge Today?") 
user_input = st.text_input("Describe a challenge you're facing:")

# Condition:
if user_input:
    st.success(f"💪you are facing:{user_input}.keep pushing forward towards your goals!🚀")
else:
        st.warning("Tell us about your challenge to get started!")

 # Reflecting:


st.header("Reflect on your learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"🎉 Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

 # achivements:

st.header("🏆 Celebrate your wins!")

achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🌟 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🤩")

 # footer :

st.write("---")  
st.write("Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**Created by •❣• Uzaira Waheed •❣•**")