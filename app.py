import os
import gradio as gr
import random
from groq import Groq

client = Groq(
    api_key="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",
)

moods = ["Happy", "Sad", "Excited", "Relaxed", "Tense", "Romantic", "Thoughtful"]

def recommend_movie(genre, mood):
    genre = genre.lower()
    mood = mood.lower()
    # This function is empty, so we'll return a placeholder message
    return f"Recommending a {mood} {genre} movie."

def chatbot(user_input, mood):
    # Combine user input with mood for a more contextual response
    prompt = f"User mood: {mood}. User message: {user_input}\nRecommend a movie based on this information."
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content

iface = gr.Interface(
    fn=chatbot,
    inputs=[
        gr.Textbox(lines=2, placeholder="Type your message here...", label="Your Message"),
        gr.Radio(choices=moods, label="Mood")
    ],
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Movie Recommendation Chatbot",
    description="Chat with me to get movie recommendations based on your mood!"
)

iface.launch()