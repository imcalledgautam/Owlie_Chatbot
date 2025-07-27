# src/ui.py
import gradio as gr
from generator import query_groq

def run_chat_interface():
    def respond(user_input):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return "API key not found. Please set GROQ_API_KEY environment variable."
        return query_groq(user_input, api_key)

    iface = gr.Interface(fn=respond, inputs="text", outputs="text", title="Owlie Chatbot (Groq-powered)")
    iface.launch()

if __name__ == "__main__":
    run_chat_interface()
