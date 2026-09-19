import os

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Lower the chatbot widget container slightly (from 90px to 80px)
html = html.replace("bottom: 90px; right: 22px;", "bottom: 80px; right: 22px;")

# 2. Lower the chat panel relative to the widget, and reduce max-height so the header is never cut off
html = html.replace(
    "bottom: 65px; right: 0; width: 340px; height: 480px; max-height: 80vh;",
    "bottom: 55px; right: 0; width: 340px; height: 430px; max-height: 65vh;"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
