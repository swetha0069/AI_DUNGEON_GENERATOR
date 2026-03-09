
import streamlit as st
from transformers import pipeline

st.title("AI Dungeon Story Generator")

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

genre = st.selectbox(
    "Choose a Genre",
    ["Fantasy", "Mystery", "Adventure", "Horror"]
)

prompt = st.text_input("Enter the beginning of your story")

if st.button("Generate Story"):

    full_prompt = genre + " story: " + prompt

    story = generator(
        full_prompt,
        max_length=150,
        num_return_sequences=3
    )

    st.subheader("Story Continuations")

    for i, s in enumerate(story):
        st.write(f"Story {i+1}:")
        st.write(s["generated_text"])
        story_text = s["generated_text"]
        st.download_button(
            label=f"Download Story {i+1}",
            data=story_text,
            file_name=f"my_adventure_{i+1}.txt",
            key=f"btn_{i}"                # Unique key for each button
        )
