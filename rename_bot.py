import os
import glob
import re

html_files = glob.glob(r"C:\Users\PC\Desktop\ccna7\*.html")

for fp in html_files:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    # 1. Update the Header Title
    content = re.sub(r'<span>🤖 CCNA Bot \(Groq AI\)</span>', r'<span>🤖 CCNA Bot</span>', content)
    content = re.sub(r'<span>🤖 CCNA Bot \(Gemini\)</span>', r'<span>🤖 CCNA Bot</span>', content)
    content = re.sub(r'<span>🤖- CCNA Bot \(Gemini\)</span>', r'<span>🤖 CCNA Bot</span>', content)
    
    # 2. Update the Welcome Message
    content = re.sub(r'basé sur l\'IA <b>Groq \(Llama 3\)</b>\.', r'basé sur l\'IA.', content)
    content = re.sub(r'basé sur l\'IA <b>Gemini</b>\.', r'basé sur l\'IA.', content)
    content = re.sub(r'basé sur l\'IA <b>.*?</b>', r'basé sur l\'IA', content)
    
    if content != original_content:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Renamed bot in {os.path.basename(fp)}")
    else:
        print(f"No changes needed in {os.path.basename(fp)}")
