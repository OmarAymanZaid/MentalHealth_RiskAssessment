import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------
# Example cluster profiles
# (feature percentages per cluster)
# ----------------------------
cluster_profiles = {
    0: {'Coping Difficulty': 78, 'Sought Treatment': 12, 'Mood Swings': 54},
    1: {'Coping Difficulty': 0, 'Sought Treatment': 100, 'Mood Swings': 40},
    2: {'Coping Difficulty': 0, 'Sought Treatment': 0, 'Mood Swings': 45},
    3: {'Coping Difficulty': 60, 'Sought Treatment': 75, 'Mood Swings': 50},
}

cluster_labels = {
    0: "Struggling Silently",
    1: "Proactive Care",
    2: "Self-Managing",
    3: "Supported but Challenged"
}

# ----------------------------
# Calm UI Layout
# ----------------------------

st.set_page_config(page_title="Mental Health Pattern Explorer", layout="centered")

# Hero / Intro Section
st.markdown("<h2 style='text-align:center; color:#4b6e65;'>🌿 Mental Health Response Pattern Explorer</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#4b6e65;'>A reflective tool exploring patterns in survey responses. This tool does not provide medical diagnosis.</p>", unsafe_allow_html=True)
st.write("---")

# ----------------------------
# Form Sections
# ----------------------------
with st.form("assessment_form"):

    st.subheader("🧍 Personal Context")
    col1, col2 = st.columns(2)
    gender = col1.selectbox("Gender", ["Male", "Female", "Other"])
    country = col2.text_input("Country")
    occupation = col1.text_input("Occupation")
    self_employed = col2.selectbox("Self-employed?", ["Yes", "No"])

    st.subheader("🧠 Emotional Indicators")
    mood_swings = st.selectbox("Mood Swings", ["None", "Sometimes", "Frequent"])
    noticed_stress = st.selectbox("Noticed growing stress?", ["Yes", "No"])
    habit_changes = st.selectbox("Noticed habit changes?", ["Yes", "No"])
    coping_difficulty = st.selectbox("Coping difficulty?", ["Yes", "No"])

    st.subheader("💼 Work & Social Impact")
    work_engagement = st.selectbox("Work engagement", ["Low", "Moderate", "High"])
    social_difficulty = st.selectbox("Social difficulty?", ["Yes", "No"])
    days_indoors = st.number_input("Days spent indoors (per week)", min_value=0, max_value=7, value=3)

    st.subheader("🤝 Support & Awareness")
    sought_treatment = st.selectbox("Have you sought treatment?", ["Yes", "No"])
    family_history = st.selectbox("Family mental health history?", ["Yes", "No"])
    personal_history = st.selectbox("Personal mental health history?", ["Yes", "No"])
    care_awareness = st.selectbox("Aware of care options?", ["Yes", "No"])
    disclose_employer = st.selectbox("Would you disclose mental health to employer?", ["Yes", "No"])

    # Submit button
    submitted = st.form_submit_button("🌿 Explore My Response Pattern")

# ----------------------------
# Process Submission
# ----------------------------
if submitted:

    # ----------------------------
    # Placeholder: Encode and predict
    # ----------------------------
    # Here you would transform the user input to match your one-hot encoded features
    # For demonstration, we randomly assign a cluster
    user_cluster = np.random.choice([0, 1, 2, 3])

    # ----------------------------
    # Result Reveal Section
    # ----------------------------
    st.write("---")
    st.markdown(f"<h3 style='color:#4b6e65;'>🌿 Your Response Pattern: {cluster_labels[user_cluster]}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#4b6e65;'>Cluster {user_cluster}</p>", unsafe_allow_html=True)

    st.markdown("**Interpretation:**")
    if user_cluster == 0:
        st.write("Your responses are most similar to individuals who report experiencing coping difficulty while not actively seeking professional support. This group tends to show moderate stress indicators and balanced mood patterns.")
    elif user_cluster == 1:
        st.write("Your responses align with individuals who proactively seek care and maintain balanced emotional patterns.")
    elif user_cluster == 2:
        st.write("You share characteristics with individuals managing stress independently with balanced behavioral patterns.")
    else:
        st.write("Your responses resemble individuals who experience coping challenges but have sought support, showing moderate engagement.")

    st.markdown("_This tool does not provide medical advice. It simply reflects similarity patterns within survey data._")

    # ----------------------------
    # Personalized Feature Comparison
    # ----------------------------
    st.subheader("How Your Responses Compare to This Pattern")

    profile = cluster_profiles[user_cluster]
    for feature, percent in profile.items():
        st.write(f"{feature}")
        bar = f"[{'█' * int(percent/10)}{'░' * (10 - int(percent/10))}] {percent}% (Cluster)"
        # Compare user input
        user_answer = None
        if feature == "Coping Difficulty":
            user_answer = coping_difficulty
        elif feature == "Sought Treatment":
            user_answer = sought_treatment
        elif feature == "Mood Swings":
            user_answer = mood_swings
        st.write(f"{bar} — You: {user_answer}")
        st.write("")  # small spacing

    # Gentle reflection
    st.markdown("🌿 _Exploring patterns can be a helpful first step toward understanding experiences. If any of these topics resonate strongly with you, consider speaking with a qualified professional._")