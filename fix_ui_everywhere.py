import os

# 1. Update Navigation in ccna_pro_complet.html
main_file = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(main_file, "r", encoding="utf-8") as f:
    main_html = f.read()

mega_exam_btn = '<a href="ccna_mega_exam.html" class="btn red" style="text-decoration:none; margin-left: 10px; border-color:var(--red); color:var(--red);">💯 Mega Exam</a>'

if "ccna_mega_exam.html" not in main_html:
    # Inject it before the progress-wrap
    main_html = main_html.replace('<div class="progress-wrap"', mega_exam_btn + '\n    <div class="progress-wrap"')
    with open(main_file, "w", encoding="utf-8") as f:
        f.write(main_html)


# 2. Extract good CSS from ccna_pro_complet.html
import re
# The good CSS starts with /* CHATBOT CSS AMELIORE */ (actually wait, let's just write it fresh to be 100% sure)
good_css = """
/* CHATBOT CSS */
#chat-widget { position: fixed; bottom: 80px; right: 22px; z-index: 999999; font-family: 'Patrick Hand', cursive; display: flex; flex-direction: column; align-items: flex-end; }
#chat-toggle { width: 50px; height: 50px; border-radius: 50%; background: var(--blue); color: white; font-size: 1.5rem; border: 2px solid var(--ink); cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s; }
#chat-toggle:hover { transform: scale(1.08); box-shadow: 0 6px 14px rgba(0,0,0,0.4); }
#chat-panel { position: absolute; bottom: 55px; right: 0; width: 340px; height: 430px; max-height: 65vh; background: var(--paper-2); border: 2px solid var(--ink); border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.3); display: flex; flex-direction: column; overflow: hidden; transform-origin: bottom right; transition: transform 0.3s ease, opacity 0.3s ease; }
#chat-panel.hidden { transform: scale(0); opacity: 0; pointer-events: none; }
#chat-header { background: var(--blue); color: white; padding: 10px 15px; font-weight: bold; font-size: 1.2rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--ink); }
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
@media (max-width: 480px) { #chat-widget { bottom: 80px; right: 15px; } #chat-panel { position: absolute; right: 0; bottom: 60px; width: calc(100vw - 30px); height: 70vh; max-height: 450px; } }
"""

# Replace in the 3 generated files
files_to_fix = [
    r"C:\Users\PC\Desktop\ccna7\ccna_50_labs.html",
    r"C:\Users\PC\Desktop\ccna7\ccna_50_exams.html",
    r"C:\Users\PC\Desktop\ccna7\ccna_mega_exam.html"
]

for fp in files_to_fix:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract the bad CSS block (starts at /* CHATBOT CSS */ and ends at @media... })
    # We'll use regex to replace it
    pattern = r"/\* CHATBOT CSS \*/.*?@media \(max-width: 480px\) \{[^\}]+\}[^\}]+\}"
    new_content = re.sub(pattern, good_css.strip(), content, flags=re.DOTALL)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Fixed CSS in {os.path.basename(fp)}")

