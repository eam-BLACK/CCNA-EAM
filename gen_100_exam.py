import os
import random
import ipaddress

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_mega_exam.html"

# --- 1. Manual Theory Questions (40 questions) ---
theory_q = [
    ("OSI", "À quelle couche OSI fonctionne un routeur ?", ["Couche 1", "Couche 2", "Couche 3", "Couche 4"], 2, "Le routeur transfère les paquets en se basant sur l'adresse IP (Couche 3)."),
    ("OSI", "Quel protocole fonctionne à la couche Transport ?", ["IP", "TCP", "HTTP", "Ethernet"], 1, "TCP et UDP sont les protocoles de la couche Transport (Couche 4)."),
    ("Commutation", "Que fait un switch avec une trame 'Unknown Unicast' ?", ["Il la supprime", "Il la diffuse sur tous les ports (Flooding)", "Il l'envoie au routeur", "Il la renvoie à l'expéditeur"], 1, "Si l'adresse MAC n'est pas dans la table, le switch l'envoie sur tous les ports sauf le port source."),
    ("VLAN", "Quel protocole est utilisé pour négocier un lien Trunk ?", ["VTP", "STP", "DTP", "LACP"], 2, "Dynamic Trunking Protocol (DTP) gère la négociation des Trunks."),
    ("VLAN", "Quel est le standard ouvert pour l'encapsulation Trunk ?", ["ISL", "802.1Q", "HDLC", "PPP"], 1, "802.1Q est le standard IEEE. ISL est propriétaire Cisco."),
    ("STP", "Dans STP, comment est élu le Root Bridge ?", ["Plus haute IP", "Plus haute MAC", "Plus faible Priorité + MAC", "Plus haute Priorité"], 2, "Le switch avec le plus faible Bridge ID (Priorité par défaut 32768 + MAC) devient le Root."),
    ("RSTP", "Quel état n'existe PAS dans Rapid STP (802.1w) ?", ["Discarding", "Learning", "Forwarding", "Listening"], 3, "RSTP fusionne Blocking et Listening en un seul état : Discarding."),
    ("EtherChannel", "Quel protocole EtherChannel est un standard IEEE ?", ["PAgP", "LACP", "VTP", "STP"], 1, "LACP (802.3ad) est le standard. PAgP est propriétaire Cisco."),
    ("Routage", "Quelle est la distance administrative d'une route statique ?", ["1", "90", "110", "120"], 0, "Une route statique a une AD de 1 (très fiable)."),
    ("OSPF", "Que signifie l'état FULL dans OSPF ?", ["Les routeurs ont échangé des Hello", "Les bases de données (LSDB) sont 100% synchronisées", "Le routeur est élu DR", "Le réseau est en panne"], 1, "FULL signifie que les routeurs adjacents ont des LSDB identiques."),
    ("OSPF", "Quelle adresse Multicast est utilisée par les routeurs OSPF (All-OSPF) ?", ["224.0.0.9", "224.0.0.10", "224.0.0.5", "224.0.0.1"], 2, "224.0.0.5 touche tous les routeurs OSPF. 224.0.0.6 touche les DR/BDR."),
    ("Sécurité", "Que bloque DHCP Snooping ?", ["Les attaques DDoS", "Les faux serveurs DHCP (Rogue DHCP)", "Le trafic HTTP", "Le Spanning Tree"], 1, "Il empêche les serveurs non autorisés d'attribuer de fausses adresses IP."),
    ("Sécurité", "Port Security : Quel est le mode de violation par défaut ?", ["Protect", "Restrict", "Shutdown", "Err-disable"], 2, "Le port est mis en état 'Shutdown' (err-disabled) s'il y a violation."),
    ("NAT", "Quel type de NAT utilise des numéros de ports pour partager une seule IP publique ?", ["NAT Statique", "NAT Dynamique", "PAT (Overload)", "NAT IPv6"], 2, "Port Address Translation (PAT) mappe plusieurs IP privées sur une seule publique via les ports TCP/UDP."),
    ("ACL", "Quelle plage correspond à une ACL Standard ?", ["1-99", "100-199", "1000-1999", "2000-2699"], 0, "1-99 et 1300-1999 sont pour les ACL standards."),
    ("IPv6", "Combien de bits compose une adresse IPv6 ?", ["32", "64", "128", "256"], 2, "IPv6 utilise 128 bits, exprimés en hexadécimal."),
    ("IPv6", "Quelle adresse IPv6 est l'équivalent de 127.0.0.1 (Loopback) ?", ["FE80::1", "FF02::1", "::1", "2001::1"], 2, "::1 est l'adresse de loopback en IPv6."),
    ("Wi-Fi", "Quel équipement centralise la gestion des points d'accès légers (LAP) ?", ["Routeur", "Switch Core", "WLC (Wireless LAN Controller)", "Firewall"], 2, "Le WLC gère les LAPs via le tunnel CAPWAP."),
    ("Wi-Fi", "Quelle norme de sécurité Wi-Fi utilise SAE ?", ["WEP", "WPA", "WPA2", "WPA3"], 3, "WPA3 remplace le PSK par SAE (Simultaneous Authentication of Equals)."),
    ("SDN", "Quelle API est utilisée pour que le contrôleur SDN parle aux switchs physiques ?", ["Northbound", "Southbound", "Eastbound", "Westbound"], 1, "Southbound API (ex: OpenFlow, NETCONF) descend vers le matériel."),
    ("SDN", "Quel format de données est le plus utilisé avec les API REST ?", ["XML", "JSON", "CSV", "YAML"], 1, "JSON est le format dominant pour les API REST grâce à sa légèreté."),
    ("Automatisation", "Lequel de ces outils n'utilise PAS d'agent sur l'équipement réseau ?", ["Chef", "Puppet", "Ansible", "Docker"], 2, "Ansible est 'Agentless' et se connecte simplement via SSH."),
    ("Dépannage", "Quelle commande permet de voir la table MAC d'un switch ?", ["show ip route", "show mac address-table", "show arp", "show interfaces"], 1, "'show mac address-table' affiche les MAC apprises par le switch."),
    ("Dépannage", "Quel protocole est utilisé par la commande 'ping' ?", ["TCP", "UDP", "ICMP", "IGMP"], 2, "Ping utilise les messages ICMP Echo Request et Echo Reply."),
    ("IPv4", "Quelle est la taille d'une adresse IPv4 ?", ["16 bits", "32 bits", "64 bits", "128 bits"], 1, "L'IPv4 est codée sur 32 bits (4 octets)."),
    ("CDP", "Quel est le but de Cisco Discovery Protocol (CDP) ?", ["Découvrir les voisins Cisco directement connectés", "Trouver la route la plus courte", "Attribuer des IP", "Bloquer les boucles"], 0, "CDP permet d'obtenir des informations (IP, port, modèle) sur les équipements Cisco voisins."),
    ("LLDP", "Quelle est la différence entre CDP et LLDP ?", ["LLDP est plus rapide", "LLDP est un standard ouvert (IEEE), CDP est propriétaire Cisco", "CDP utilise IPv6", "LLDP ne marche que sur les routeurs"], 1, "LLDP (802.1AB) est supporté par tous les constructeurs, contrairement à CDP."),
    ("HSRP", "Dans HSRP, quel routeur transmet les paquets ?", ["Standby Router", "Active Router", "Backup Router", "Passive Router"], 1, "Le routeur Active est celui qui traite tout le trafic pour l'IP virtuelle."),
    ("HSRP", "Quelle est l'adresse MAC virtuelle par défaut de HSRP v1 pour le groupe 10 ?", ["0000.0c07.ac0a", "0000.0c9f.f00a", "0000.0c07.ac10", "ffff.ffff.ffff"], 0, "0a est l'hexadécimal de 10. Le préfixe est 0000.0c07.acXX."),
    ("NTP", "Quel port utilise NTP pour synchroniser l'heure ?", ["TCP 80", "UDP 123", "TCP 123", "UDP 53"], 1, "NTP utilise le port UDP 123."),
    ("Syslog", "Quel niveau Syslog (Severity) correspond à 'Critical' ?", ["0", "1", "2", "3"], 2, "0=Emerg, 1=Alert, 2=Crit, 3=Err, 4=Warn, 5=Notice, 6=Info, 7=Debug."),
    ("AAA", "Quels sont les deux protocoles serveur utilisés pour l'authentification AAA ?", ["RADIUS et TACACS+", "SSH et Telnet", "HTTP et HTTPS", "OSPF et EIGRP"], 0, "RADIUS (ouvert) et TACACS+ (Cisco) sont les serveurs AAA principaux."),
    ("DHCP", "Quel message le serveur DHCP envoie-t-il pour proposer une IP ?", ["DHCP Discover", "DHCP Offer", "DHCP Request", "DHCP Ack"], 1, "DORA : Discover (Client), Offer (Serveur), Request (Client), Ack (Serveur)."),
    ("DNS", "Quel type d'enregistrement DNS mappe un nom à une adresse IPv6 ?", ["A", "CNAME", "MX", "AAAA"], 3, "'A' est pour IPv4, 'AAAA' est pour IPv6."),
    ("OSPF", "Quel est l'intervalle Hello par défaut d'OSPF sur un réseau Ethernet ?", ["5 secondes", "10 secondes", "30 secondes", "40 secondes"], 1, "Sur les réseaux Broadcast (Ethernet), l'intervalle Hello est de 10s (Dead = 40s)."),
    ("STP", "Que fait la commande 'spanning-tree portfast' ?", ["Désactive STP", "Passe le port directement en état Forwarding", "Accélère les BPDUs", "Bloque le port"], 1, "PortFast ignore les états Listening/Learning pour les PCs/Serveurs afin qu'ils se connectent instantanément."),
    ("BPDU Guard", "Que se passe-t-il si un port avec PortFast et BPDU Guard reçoit un BPDU ?", ["Il devient Root Port", "Il ignore le BPDU", "Il se met en err-disable (Shutdown)", "Il change de VLAN"], 2, "BPDU Guard désactive le port pour empêcher la création d'une boucle par un switch non autorisé."),
    ("Dépannage", "Laquelle de ces adresses est une APIPA (adresse privée automatique) ?", ["10.0.0.1", "172.16.1.1", "169.254.x.x", "192.168.1.1"], 2, "Windows assigne une IP 169.254.x.x si le serveur DHCP est injoignable."),
    ("Routage", "Dans la table de routage, que signifie la lettre 'C' ?", ["Connecté directement", "OSPF", "Statique", "EIGRP"], 0, "'C' = Connected, 'L' = Local, 'O' = OSPF, 'S' = Static."),
    ("Sécurité", "Quel est le mot de passe recommandé pour chiffrer l'accès au mode privilégié ?", ["enable password", "enable secret", "service password-encryption", "line vty"], 1, "'enable secret' utilise un hash MD5/SHA sécurisé, contrairement à 'enable password' qui est en clair.")
]

q_db = list(theory_q)

# --- 2. Dynamic Practical Questions ---

# Subnetting (Network ID)
for _ in range(15):
    ip = f"192.168.{random.randint(1, 250)}.{random.randint(10, 240)}"
    prefix = random.choice([25, 26, 27, 28, 29, 30])
    net = ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False)
    
    wrong_1 = str(net.network_address + random.choice([1, 2, 3]))
    wrong_2 = str(net.broadcast_address)
    wrong_3 = str(net.network_address - 1 if net.network_address.packed[-1] > 0 else net.network_address + 16)
    
    opts = [str(net.network_address), wrong_1, wrong_2, wrong_3]
    random.shuffle(opts)
    ans = opts.index(str(net.network_address))
    
    q_db.append(("Subnetting", f"Quelle est l'adresse réseau (Network ID) pour l'IP {ip}/{prefix} ?", opts, ans, f"L'IP {ip} avec un /{prefix} appartient au bloc réseau {net.network_address}."))

# Subnetting (Broadcast)
for _ in range(15):
    ip = f"10.{random.randint(1, 10)}.{random.randint(1, 10)}.{random.randint(10, 200)}"
    prefix = random.choice([25, 26, 27, 28, 29])
    net = ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False)
    
    wrong_1 = str(net.network_address)
    wrong_2 = str(net.broadcast_address - 1)
    wrong_3 = str(net.network_address + 1)
    
    opts = [str(net.broadcast_address), wrong_1, wrong_2, wrong_3]
    random.shuffle(opts)
    ans = opts.index(str(net.broadcast_address))
    
    q_db.append(("Subnetting", f"Quelle est l'adresse de Broadcast pour l'IP {ip}/{prefix} ?", opts, ans, f"L'IP {ip} avec un /{prefix} se termine à l'adresse de diffusion {net.broadcast_address}."))

# Ports Numbers
ports = {"HTTP": "80", "HTTPS": "443", "SSH": "22", "Telnet": "23", "DNS": "53", "DHCP (Serveur)": "67", "NTP": "123", "TFTP": "69", "FTP": "21", "SMTP": "25"}
for prot, port in ports.items():
    wrong_ports = list(ports.values())
    wrong_ports.remove(port)
    opts = [port] + random.sample(wrong_ports, 3)
    random.shuffle(opts)
    ans = opts.index(port)
    q_db.append(("Ports TCP/UDP", f"Quel port par défaut est utilisé par le protocole {prot} ?", opts, ans, f"Le protocole {prot} utilise le port standard {port}."))

# Wildcard Masks
wildcards = {24: "0.0.0.255", 25: "0.0.0.127", 26: "0.0.0.63", 27: "0.0.0.31", 28: "0.0.0.15", 29: "0.0.0.7", 30: "0.0.0.3"}
for prefix, mask in wildcards.items():
    wrong_masks = list(wildcards.values())
    wrong_masks.remove(mask)
    opts = [mask] + random.sample(wrong_masks, 3)
    random.shuffle(opts)
    ans = opts.index(mask)
    q_db.append(("Wildcard Mask", f"Quel est le masque générique (Wildcard Mask) utilisé dans OSPF pour un sous-réseau /{prefix} ?", opts, ans, f"Un /{prefix} a un masque de sous-réseau normal. Son Wildcard Mask (inversé) est {mask}."))

# Admin Distances
ads = {"OSPF": "110", "EIGRP (Interne)": "90", "RIP": "120", "Statique": "1", "Connecté": "0", "eBGP": "20", "IS-IS": "115"}
for prot, ad in ads.items():
    wrong_ads = list(ads.values())
    wrong_ads.remove(ad)
    opts = [ad] + random.sample(wrong_ads, 3)
    random.shuffle(opts)
    ans = opts.index(ad)
    q_db.append(("Routage (AD)", f"Quelle est la Distance Administrative (AD) par défaut du protocole {prot} ?", opts, ans, f"L'AD indique la fiabilité. Pour {prot}, c'est {ad}."))

# Shuffle to mix them up nicely, keeping exact 100 questions
random.shuffle(q_db)
q_db = q_db[:100]

# --- HTML Generation ---
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>💯 Mega Examen CCNA - 100 Questions</title>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Kalam:wght@400;700&family=Patrick+Hand&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
:root{ --paper:#f7f1e1; --paper-2:#fffdf6; --ink:#1f2d4d; --blue:#2a5db0; --red:#c0392b; --green:#1e7a4c; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Patrick Hand', cursive; background: var(--paper); color: var(--ink); padding: 15px; font-size: 1.15rem; }
.header { text-align: center; margin: 20px 0 40px; }
.header h1 { font-family: 'Caveat', cursive; font-size: 3rem; color: var(--blue); line-height:1.1; }
.header p { color: var(--ink); font-size: 1.2rem; }
.header a { display: inline-block; margin-top: 15px; padding: 10px 25px; background: var(--ink); color: white; text-decoration: none; border-radius: 20px; font-family:'Kalam',cursive; font-weight:bold; }
.controls { text-align:center; margin-bottom: 20px; position: sticky; top: 0; background: rgba(247,241,225,0.9); padding: 10px; z-index: 50; border-bottom: 2px dashed var(--ink); backdrop-filter: blur(5px); }
.controls button { font-family: 'Kalam', cursive; font-size: 1.1rem; padding: 8px 15px; background: var(--green); color: white; border: 2px solid var(--ink); border-radius: 10px; cursor: pointer; font-weight: bold; }
.exam-container { max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 25px; padding-bottom: 100px; }
.q-card { background: var(--paper-2); border: 2px solid var(--ink); border-radius: 15px; padding: 25px; box-shadow: 4px 4px 0 rgba(31,45,77,.1); }
.q-card h3 { font-family: 'Kalam', cursive; color: var(--red); margin-bottom: 12px; border-bottom: 2px dashed var(--ink); padding-bottom: 5px; }
.q-text { font-size: 1.25rem; margin-bottom: 15px; font-weight:bold; }
.options { list-style: none; margin-bottom: 15px; }
.options li { margin-bottom: 10px; padding: 12px 15px; background: rgba(0,0,0,0.03); border: 2px solid rgba(0,0,0,0.05); border-radius: 8px; cursor: pointer; transition: 0.2s; }
.options li:hover { background: rgba(42,93,176,0.1); border-color: var(--blue); }
.options li.correct { background: #eaf7ef !important; border-color: var(--green) !important; font-weight: bold; }
.options li.wrong { background: #fdecea !important; border-color: var(--red) !important; text-decoration: line-through; }
.options li.selected { background: #ffe680; border-color: #d97706; }
.corrige { margin-top: 15px; padding: 15px; background: #eaf7ef; border: 2px dashed var(--green); border-radius: 8px; display: none; }
.score-box { position:fixed; bottom:20px; left:50%; transform:translateX(-50%); background:var(--ink); color:white; padding:15px 30px; border-radius:30px; font-family:'Kalam',cursive; font-size:1.5rem; font-weight:bold; box-shadow:0 5px 15px rgba(0,0,0,0.3); z-index:100; display:none; }
</style>
</head>
<body>
  <div class="header">
    <h1>💯 Mega Examen CCNA (100 Questions)</h1>
    <p>Le simulateur ultime pour s'entraîner à la certification 200-301.</p>
    <a href="ccna_pro_complet.html">⬅ Retourner au Cours Principal</a>
  </div>
  
  <div class="controls">
    <button id="btn-submit">Voir mon Score Final</button>
  </div>

  <div class="exam-container" id="exam-box">
"""

letters = ["A", "B", "C", "D"]

for i, (topic, q, opts, ans_idx, expl) in enumerate(q_db, start=1):
    opts_html = ""
    for j, opt in enumerate(opts):
        # We store the correct index in dataset to validate in JS
        opts_html += f"<li data-idx='{j}' data-correct='{ans_idx}'><strong>{letters[j]}.</strong> {opt}</li>\n"
    
    html_content += f"""
    <div class="q-card" id="q{i}">
      <h3>Question {i} - {topic}</h3>
      <p class="q-text">{q}</p>
      <ul class="options">
        {opts_html}
      </ul>
      <div class="corrige">
        <p><strong>✅ {letters[ans_idx]}</strong> - {expl}</p>
      </div>
    </div>
"""

html_content += """
  </div>
  
  <div class="score-box" id="score-box">Score : 0 / 100</div>

  <script>
    let score = 0;
    let answered = 0;

    // Interaction de sélection
    document.querySelectorAll('.options li').forEach(li => {
      li.addEventListener('click', function() {
        const ul = this.parentNode;
        if(ul.dataset.locked) return; // Empêche de changer la réponse après validation globale si on veut, mais ici on permet de changer avant le submit
        
        ul.querySelectorAll('li').forEach(el => el.classList.remove('selected'));
        this.classList.add('selected');
      });
    });

    // Bouton de validation globale
    document.getElementById('btn-submit').addEventListener('click', () => {
      score = 0;
      let total_answered = 0;

      document.querySelectorAll('.options').forEach(ul => {
        ul.dataset.locked = "true"; // Bloque les clics
        const selected = ul.querySelector('li.selected');
        const correct_idx = ul.querySelector('li').dataset.correct;
        
        // Afficher la correction
        ul.parentNode.querySelector('.corrige').style.display = 'block';

        if(selected) {
          total_answered++;
          if(selected.dataset.idx === correct_idx) {
            selected.classList.add('correct');
            score++;
          } else {
            selected.classList.add('wrong');
            // Mettre en vert la bonne
            ul.querySelector(`li[data-idx="${correct_idx}"]`).classList.add('correct');
          }
        } else {
          // Si rien n'est sélectionné, juste montrer la bonne
          ul.querySelector(`li[data-idx="${correct_idx}"]`).classList.add('correct');
        }
      });

      const scoreBox = document.getElementById('score-box');
      scoreBox.innerHTML = `Score : ${score} / 100`;
      scoreBox.style.display = 'block';
      
      // Scroll smoothly to top to see score or let them browse
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  </script>
</body>
</html>
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Add the button to the main file if it doesn't already point to the MEGA exam
main_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(main_path, "r", encoding="utf-8") as f:
    main_html = f.read()

# Replace the previous "50 Exams" link if it exists, or just add the new one
btn_link = '<a href="ccna_mega_exam.html" class="btn green" style="text-decoration:none; margin-left: 10px;">💯 Mega Exam (100 Qs)</a>'

if "ccna_mega_exam.html" not in main_html:
    if "ccna_exams.html" in main_html:
        import re
        main_html = re.sub(r'<a href="ccna_exams\.html".*?</a>', btn_link, main_html)
    else:
        main_html = main_html.replace('<div class="progress-wrap"', btn_link + '\n    <div class="progress-wrap"')

    with open(main_path, "w", encoding="utf-8") as f:
        f.write(main_html)
