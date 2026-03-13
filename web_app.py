import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from questions import questions

# Page config
st.set_page_config(
    page_title="AI Mock Interview Agent",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Mock Interview Agent")
st.write("Practice interview questions and get instant feedback.")

# Load model
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# Question selection
question_list = list(questions.keys())

selected_question = st.selectbox(
    "Select an Interview Question",
    question_list
)

# Show question
st.subheader("Question")
st.write(selected_question)

# User answer
user_answer = st.text_area(
    "Write your answer here",
    height=150
)

# Evaluate button
if st.button("Evaluate Answer"):

    if user_answer.strip() == "":
        st.warning("Please enter your answer first.")
    else:

        expected_answer = questions[selected_question]

        emb1 = model.encode([user_answer])
        emb2 = model.encode([expected_answer])

        score = cosine_similarity(emb1, emb2)[0][0]

        st.subheader("Result")

        st.write("Similarity Score:", round(score,2))

        if score > 0.7:
            st.success("✅ Your answer looks correct.")
        elif score > 0.4:
            st.warning("⚠️ Your answer is partially correct.")
        else:
            st.error("❌ Your answer seems incorrect.")

        # Show expected answer
        with st.expander("See Expected Answer"):
            st.write(expected_answer)

# Footer
st.markdown("---")
st.caption("Built with Python, Sentence Transformers and Streamlit.")