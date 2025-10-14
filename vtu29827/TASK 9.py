import openai
import gradio as gr
import os

openai.api_key = os.getenv("sk-projs")

messages = [
    {"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation."}
]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="INTELLIGENT CHATBOT"
)

demo.launch(share=True)
