import os

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

mobile_fixes = """
/* AMELIORATIONS MOBILE (SMARTPHONE) */
html, body { max-width: 100vw; overflow-x: hidden !important; }
img, svg { max-width: 100%; height: auto; }
.mermaid { max-width: 100%; overflow-x: auto; }
pre { max-width: 100%; overflow-x: auto; }

@media (max-width: 768px) {
  .cover { 
    margin: 15px 10px 20px; 
    padding: 25px 15px; 
    border-radius: 20px !important; /* Retire la forme bizarre sur mobile */
  }
  .cover::before, .cover::after { display: none; } /* Retire les deco de fond qui debordent */
  .cover h1 { font-size: 2.2rem; }
  
  .layout { padding: 0 10px; gap: 15px; }
  .poster { padding: 25px 15px 20px; border-radius: 15px !important; }
  
  .topbar { padding: 10px; }
  .topbar-inner { flex-direction: column; align-items: stretch; gap: 10px; }
  .search-wrap { width: 100%; }
  
  .progress-wrap { justify-content: space-between; }
  
  table { font-size: 0.85rem; }
  th, td { padding: 8px 6px; }
}
"""

if "AMELIORATIONS MOBILE" not in html:
    html = html.replace("</style>", mobile_fixes + "\n</style>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
