import os

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Update mentions of Gemini in the frontend
html = html.replace("basé sur l'IA <b>Gemini</b>", "basé sur l'IA (Llama 3)")
html = html.replace("GEMINI_API_KEY", "l'API Key")
html = html.replace("Gemini", "Groq/Llama")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
