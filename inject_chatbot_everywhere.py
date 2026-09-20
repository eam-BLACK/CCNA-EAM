import os
import glob

# The files we want to ensure have the chatbot
html_files = glob.glob(r"C:\Users\PC\Desktop\ccna7\*.html")

css_code = """
/* CHATBOT CSS */
#chat-widget { position: fixed; bottom: 20px; right: 20px; z-index: 9999; font-family: 'Patrick Hand', cursive; }
#chat-toggle { width: 65px; height: 65px; border-radius: 50%; background: var(--blue); color: white; font-size: 2rem; border: 3px solid var(--ink); cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s; }
#chat-toggle:hover { transform: scale(1.08); box-shadow: 0 6px 16px rgba(0,0,0,0.4); }
#chat-panel { width: 360px; height: 500px; background: var(--paper-2); border: 2px solid var(--ink); border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); display: flex; flex-direction: column; overflow: hidden; transform-origin: bottom right; transition: transform 0.3s ease, opacity 0.3s ease; }
#chat-panel.hidden { transform: scale(0); opacity: 0; pointer-events: none; }
#chat-header { background: var(--blue); color: white; padding: 12px 18px; font-weight: bold; font-size: 1.3rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--ink); }
#chat-close { background: transparent; border: none; color: white; font-size: 1.4rem; cursor: pointer; font-weight: bold; transition: color 0.2s; }
#chat-close:hover { color: var(--red); }
#chat-messages { flex: 1; padding: 15px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; background: var(--paper); }
.cmsg { padding: 10px 14px; border-radius: 14px; max-width: 85%; font-size: 1.05rem; line-height: 1.4; border: 2px solid var(--ink); word-wrap: break-word;}
.cmsg.bot { background: white; align-self: flex-start; border-bottom-left-radius: 4px; box-shadow: 2px 2px 0 rgba(31,45,77,.1); }
.cmsg.user { background: var(--green); color: white; align-self: flex-end; border-bottom-right-radius: 4px; border-color: #176540; box-shadow: -2px 2px 0 rgba(31,45,77,.1); }
.cmsg.error { background: #fdecea; color: var(--red); border-color: var(--red); }
#chat-input-container { padding: 12px; background: white; border-top: 2px solid var(--ink); display: flex; gap: 8px; }
#chat-input { flex: 1; padding: 10px 14px; border: 2px solid var(--ink); border-radius: 20px; outline: none; font-family: 'Patrick Hand', cursive; font-size: 1.05rem; }
#chat-input:focus { border-color: var(--blue); box-shadow: 0 0 0 3px rgba(42,93,176,.15); }
#chat-send { background: var(--blue); color: white; border: 2px solid var(--ink); border-radius: 20px; padding: 5px 18px; cursor: pointer; font-family: 'Patrick Hand', cursive; font-weight: bold; font-size: 1rem; transition: background 0.2s; }
#chat-send:hover { background: #1c4e7a; }
@media (max-width: 480px) { #chat-panel { width: 90vw; height: 60vh; position: fixed; right: 5vw; bottom: 85px; } }
"""

html_code = """
<!-- CHATBOT HTML -->
<div id="chat-widget">
  <button id="chat-toggle" title="Discuter avec l'IA">🤖</button>
  <div id="chat-panel" class="hidden">
    <div id="chat-header">
      <span>🤖 CCNA Bot (Groq AI)</span>
      <button id="chat-close">✖</button>
    </div>
    <div id="chat-messages">
      <div class="cmsg bot">Salut ! Je suis ton assistant CCNA virtuel basé sur l'IA <b>Groq (Llama 3)</b>. Pose-moi n'importe quelle question sur le cours ou les exercices !</div>
    </div>
    <div id="chat-input-container">
      <input type="text" id="chat-input" placeholder="Pose ta question..." autocomplete="off"/>
      <button id="chat-send">Send</button>
    </div>
  </div>
</div>
<script>
  const chatToggle = document.getElementById('chat-toggle');
  const chatPanel = document.getElementById('chat-panel');
  const chatClose = document.getElementById('chat-close');
  const chatInput = document.getElementById('chat-input');
  const chatSend = document.getElementById('chat-send');
  const chatMessages = document.getElementById('chat-messages');

  chatToggle.addEventListener('click', () => { 
    chatPanel.classList.remove('hidden'); 
    chatToggle.style.display = 'none'; 
    setTimeout(() => chatInput.focus(), 300);
  });
  
  chatClose.addEventListener('click', () => { 
    chatPanel.classList.add('hidden'); 
    setTimeout(() => chatToggle.style.display = 'flex', 300); 
  });

  chatInput.addEventListener('keypress', (e) => { 
    if(e.key === 'Enter') chatSend.click(); 
  });

  function parseMarkdown(text) {
    let html = text.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
    html = html.replace(/\\*(.*?)\\*/g, '<em>$1</em>');
    html = html.replace(/```([\\s\\S]*?)```/g, '<pre><code>$1</code></pre>');
    html = html.replace(/`(.*?)`/g, '<code>$1</code>');
    return html.replace(/\\n/g, '<br>');
  }

  chatSend.addEventListener('click', async () => {
    const text = chatInput.value.trim();
    if(!text) return;
    chatInput.value = '';
    
    chatMessages.innerHTML += `<div class="cmsg user">${text}</div>`;
    chatMessages.scrollTop = chatMessages.scrollHeight;

    const loadingId = 'loading-' + Date.now();
    chatMessages.innerHTML += `<div class="cmsg bot" id="${loadingId}">... en train de réfléchir ...</div>`;
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
      });
      
      const data = await res.json();
      document.getElementById(loadingId).remove();
      
      if(data.error) throw new Error(data.error);
      
      chatMessages.innerHTML += `<div class="cmsg bot">${parseMarkdown(data.reply)}</div>`;
    } catch (e) {
      document.getElementById(loadingId)?.remove();
      chatMessages.innerHTML += `<div class="cmsg bot error"><b>Erreur :</b> ${e.message}<br><br>As-tu bien ajouté <code>GROQ_API_KEY</code> dans les variables d'environnement Vercel ?</div>`;
    }
    chatMessages.scrollTop = chatMessages.scrollHeight;
  });
</script>
"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    if 'id="chat-widget"' not in html:
        # Inject CSS
        html = html.replace("</style>", css_code + "\n</style>")
        # Inject HTML/JS
        html = html.replace("</body>", html_code + "\n</body>")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Injected chatbot into {os.path.basename(file_path)}")
    else:
        print(f"Chatbot already exists in {os.path.basename(file_path)}")
