import os

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix the position so it doesn't overlap the #toTop arrow button (bottom: 22px, height: 54px)
html = html.replace("bottom: 15px; right: 15px;", "bottom: 90px; right: 22px;")

# Hide Gemini branding
html = html.replace("<span>🤖 CCNA Bot (Gemini)</span>", "<span>🤖 CCNA Bot</span>")
html = html.replace("basé sur l'IA <b>Gemini</b>. ", "")
html = html.replace("<br><br>As-tu bien ajouté <code>GEMINI_API_KEY</code> dans les variables d'environnement Vercel ?", "")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
