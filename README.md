# AI_DUNGEON_GENERATOR
# ai-dungeon-generator
https://ai-dungeon-generator-trwudxhud3qzqlqrpessg6.streamlit.app/

🏰 AI Dungeon Story Generator

📖 Overview
The AI Dungeon Story Generator is an interactive web application that generates fantasy-style adventure stories using Artificial Intelligence. The project demonstrates how generative AI models can create dynamic story continuations based on user prompts.
Users can enter a starting idea or scenario, choose a genre, and the AI will automatically generate multiple story continuations. This allows users to explore different story paths and create unique narratives.
The application is built using Python, Hugging Face Transformers, and Streamlit, making it easy to deploy and use directly from a web browser.
The goal of this project is to build an end-to-end AI application, combining Natural Language Processing with an interactive user interface.

Features

🧠 AI Story Generation
Uses a pretrained GPT-2 language model from Hugging Face to generate creative story continuations.

🎭 Genre Selection
Users can select different story genres such as:
Fantasy
Mystery
Adventure
Horror
The genre influences the style of the generated story.

📜 Multiple Story Continuations
The application generates multiple story paths, allowing users to choose different directions for their adventure.
💬 Prompt-Based Input
Users can enter their own story prompt to start the narrative.
Example:
"A brave knight enters a mysterious dungeon searching for a lost treasure."

💾 Save Story Feature
Generated stories can be saved as a text file for later reading or sharing.


🌐 Web Interface
A clean and simple Streamlit interface allows users to interact with the AI easily through their browser.
🛠️ Technologies Used
Programming Language
Python
Web Framework
Streamlit
AI / NLP Libraries
Hugging Face Transformers
GPT-2
Deep Learning Framework
PyTorch
Environment
Virtual Environment / Conda
Version Control
Git & GitHub

🚀 Setup and Run Instructions
Follow these steps to run the project locally.

1️⃣ Clone the Repository
Bash
Copy code
git clone https://github.com/yourusername/ai-dungeon-story-generator.git
cd ai-dungeon-story-generator

2️⃣ Create Virtual Environment
Create a new Python environment to avoid dependency conflicts.
Bash
Copy code
python -m venv dungeon_env
Activate the environment:
Windows
Bash
Copy code
dungeon_env\Scripts\activate
Mac / Linux
Bash
Copy code
source dungeon_env/bin/activate

3️⃣ Install Dependencies
Install required libraries.
Bash
Copy code
pip install -r requirements.txt
Main libraries include:
streamlit
transformers
torch

4️⃣ Run the Application
Start the Streamlit app.
Bash
Copy code
streamlit run app.py

5️⃣ Open in Browser
After running the command, open the link:
Copy code

http://localhost:8501
You will see the AI Dungeon Story Generator interface.

👣 Step-by-Step Work Done
The project was developed step by step.
Environment Setup
A Python environment was created to manage project dependencies and avoid conflicts.
Loading the AI Model
We loaded the pretrained GPT-2 model from Hugging Face using the Transformers library.

Example:
Python
Copy code
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
This allows the system to generate human-like text based on prompts.
Prompt-Based Story Generation
Users enter a story prompt, which is sent to the GPT-2 model to generate story continuations.

Example:
Python
Copy code
story = generator(prompt, max_length=200)
Generating Multiple Continuations
The model generates multiple story outputs so users can explore different story possibilities.
Genre Selection
We added a genre selection option using Streamlit widgets.
The genre is appended to the user prompt to influence the story style.

Example:
Copy code

Fantasy story about a lost kingdom
Mystery story about a haunted mansion
Building the Web Interface
We created a simple interface using Streamlit.
Components include:
Text input for story prompt
Genre selection dropdown
Generate story button
Display multiple continuations
Save Story Feature
Users can save generated stories as a text file for later use.

Example:
Python
Copy code
with open("story.txt", "w") as file:
    file.write(story)
Deployment
Finally, the application was deployed using Streamlit Cloud, allowing anyone to access the app online.
⚠️ Errors Faced and How We Solved Them


1️⃣ Model Loading Delay

Error
The application took a long time to load the GPT-2 model during startup.
Reason
Large pretrained models require time to download and initialize.
Solution
We cached the model loading process using Streamlit.
Python
Copy code
@st.cache_resource
This prevents the model from reloading every time the app refreshes.

2️⃣ Streamlit App Not Running
Error
The application did not open in the browser.
Reason
Streamlit was not installed in the environment.
Solution
Bash
Copy code
pip install streamlit
Then run:
Bash
Copy code
streamlit run app.py

3️⃣ Git Push Errors
Error
Copy code

fatal: 'main' does not appear to be a git repository
Reason
Incorrect remote repository configuration.
Solution
Bash
Copy code
git branch -M main
git remote add origin <repo-url>
git push -u origin main

✅ Final Output
The final result is a fully functional AI-powered story generator.
Users can:
Enter a story prompt
Select a genre
Generate multiple story continuations
Read interactive fantasy adventures
Save generated stories
The application provides a simple and engaging way to experience AI-generated storytelling.

🎓 Conclusion & Learnings
This project helped demonstrate how generative AI can be used for creative storytelling.
Key learnings include:

🤖 Generative AI Applications
We learned how GPT-2 can generate meaningful and creative text.

🧠 Natural Language Processing
Understanding how language models work for text generation.

🌐 Web App Development
Connecting AI models with a user-friendly interface using Streamlit.

🧩 Problem Solving
Handling real-world issues such as model loading time and deployment errors.

📂 Project Organization
Creating a well-structured project with proper documentation and GitHub version control.

👨‍💻 Author
Sri
AI / Python Enthusiast
Project: AI Dungeon Story Generator
