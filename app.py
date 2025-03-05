import streamlit as st
import random
import time

# Function to generate a random Growth Mindset tip
def get_mindset_tip():
    tips = [
        "Failures are just steps toward success! Keep going.",
        "Your brain is like a muscle—the more you use it, the stronger it gets!",
        "Mistakes are proof that you are learning.",
        "Embrace challenges, they make you grow!",
        "Seek feedback—it’s the fastest way to improve.",
        "Effort matters more than talent!",
        "Learning never stops. Keep pushing forward!"
    ]
    return random.choice(tips)

# Streamlit App Layout with Sidebar and Styling
st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")
st.sidebar.title("🌱 Growth Mindset Menu")
st.sidebar.markdown("*Select an option below:*")
menu = st.sidebar.radio("Navigation", ["Home", "Quiz", "Daily Challenges", "Leaderboard", "Feedback"])

# Home Page
if menu == "Home":
    st.title("🚀 Growth Mindset Challenge")
    st.write("### Welcome! Let's develop a growth mindset together.")
    st.image("img1.png", use_column_width=True)
    
    # Display a random mindset tip
    if st.button("Click for a Growth Mindset Tip! 🧠"):
        st.success(get_mindset_tip())
    
    st.write("---")
    st.write("💡 Remember: Intelligence isn’t fixed. Keep learning, keep growing!")

# Quiz Section
elif menu == "Quiz":
    st.write("## Test Your Growth Mindset! 🎯")
    questions = {
        "Challenges should be...": ["Avoided", "Embraced"],
        "Effort is...": ["Pointless", "Key to success"],
        "Mistakes are...": ["A sign of failure", "A learning opportunity"],
        "When receiving feedback, I should...": ["Ignore it", "Use it to improve"]
    }
    
    score = 0
    for question, options in questions.items():
        answer = st.radio(question, options)
        if options.index(answer) == 1:  # Correct option is always second
            score += 1
    
    if st.button("Submit Quiz"):
        st.success(f"You got {score}/{len(questions)} correct! Keep growing! 🌱")

# Daily Challenges
elif menu == "Daily Challenges":
    st.write("## 🌟 Today's Growth Mindset Challenge!")
    challenges = [
        "Write down 3 things you learned today.",
        "Try a new skill or hobby for 15 minutes.",
        "Help someone who is struggling with a task.",
        "Replace a negative thought with a positive one.",
        "Seek feedback from a mentor or friend."
    ]
    st.info(random.choice(challenges))

# Leaderboard (Placeholder for future enhancement)
elif menu == "Leaderboard":
    st.write("## 🏆 Growth Mindset Leaderboard (Coming Soon!)")
    st.info("Complete more challenges to climb the leaderboard!")

# Feedback Collection
elif menu == "Feedback":
    st.write("## 💬 Share Your Thoughts!")
    feedback = st.text_area("What did you learn from this challenge?")
    if st.button("Submit Feedback"):
        time.sleep(1)
        st.success("Thank you for your response! Keep learning and improving. 📈")