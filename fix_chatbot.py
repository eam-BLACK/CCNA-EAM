import re

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

new_css = """/* CHATBOT CSS */
#chat-widget { position: fixed; bottom: 15px; right: 15px; z-index: 999999; font-family: 'Patrick Hand', cursive; display: flex; flex-direction: column; align-items: flex-end; }
#chat-toggle { width: 50px; height: 50px; border-radius: 50%; background: var(--blue); color: white; font-size: 1.5rem; border: 2px solid var(--ink); cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s; }
#chat-toggle:hover { transform: scale(1.08); box-shadow: 0 6px 14px rgba(0,0,0,0.4); }
#chat-panel { position: absolute; bottom: 65px; right: 0; width: 340px; height: 480px; max-height: 80vh; background: var(--paper-2); border: 2px solid var(--ink); border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.3); display: flex; flex-direction: column; overflow: hidden; transform-origin: bottom right; transition: transform 0.3s ease, opacity 0.3s ease; }
#chat-panel.hidden { transform: scale(0); opacity: 0; pointer-events: none; }
#chat-header { background: var(--blue); color: white; padding: 10px 15px; font-weight: bold; font-size: 1.2rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--ink); }
#chat-close { background: transparent; border: none; color: white; font-size: 1.3rem; cursor: pointer; font-weight: bold; transition: color 0.2s; padding: 0 5px; }
#chat-close:hover { color: var(--red); }
#chat-messages { flex: 1; padding: 12px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; background: var(--paper); }
.cmsg { padding: 8px 12px; border-radius: 12px; max-width: 85%; font-size: 0.98rem; line-height: 1.4; border: 2px solid var(--ink); word-wrap: break-word;}
.cmsg.bot { background: white; align-self: flex-start; border-bottom-left-radius: 4px; box-shadow: 2px 2px 0 rgba(31,45,77,.1); }
.cmsg.user { background: var(--green); color: white; align-self: flex-end; border-bottom-right-radius: 4px; border-color: #176540; box-shadow: -2px 2px 0 rgba(31,45,77,.1); }
.cmsg.error { background: #fdecea; color: var(--red); border-color: var(--red); }
#chat-input-container { padding: 10px; background: white; border-top: 2px solid var(--ink); display: flex; gap: 8px; }
#chat-input { flex: 1; padding: 8px 12px; border: 2px solid var(--ink); border-radius: 20px; outline: none; font-family: 'Patrick Hand', cursive; font-size: 1rem; }
#chat-input:focus { border-color: var(--blue); box-shadow: 0 0 0 3px rgba(42,93,176,.15); }
#chat-send { background: var(--blue); color: white; border: 2px solid var(--ink); border-radius: 20px; padding: 5px 15px; cursor: pointer; font-family: 'Patrick Hand', cursive; font-weight: bold; font-size: 0.95rem; transition: background 0.2s; }
#chat-send:hover { background: #1c4e7a; }
@media (max-width: 480px) { #chat-panel { width: 90vw; height: 60vh; position: fixed; right: 5vw; bottom: 75px; } }
"""

pattern = r"/\* CHATBOT CSS \*/.*?(?=</style>)"
html = re.sub(pattern, new_css, html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
