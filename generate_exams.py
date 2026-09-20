import os
import random

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_exams.html"

q_data = [
    # Module 1 & 2 : Bases, OSI, TCP/IP, IP
    ("Modèle OSI", "À quelle couche du modèle OSI se trouve l'adresse MAC ?", ["Couche 1 (Physique)", "Couche 2 (Liaison)", "Couche 3 (Réseau)", "Couche 4 (Transport)"], 1, "La couche Liaison de données (Data Link) utilise les adresses MAC pour la communication locale."),
    ("Modèle OSI", "Quel protocole fonctionne à la couche Transport et garantit la livraison (fiable) ?", ["UDP", "IP", "TCP", "ICMP"], 2, "TCP est orienté connexion et garantit la livraison grâce aux acquittements (ACK). UDP ne le fait pas."),
    ("Câblage", "Quel type de câble est nécessaire pour relier deux Switchs directement entre eux (anciens modèles sans Auto-MDIX) ?", ["Câble Droit (Straight-through)", "Câble Croisé (Crossover)", "Câble Console (Rollover)", "Fibre monomode"], 1, "Les équipements de même type (Switch vers Switch, PC vers PC) nécessitent un câble croisé si Auto-MDIX n'est pas actif."),
    ("IPv4", "Quelle est l'adresse de réseau pour l'IP 192.168.10.45/28 ?", ["192.168.10.0", "192.168.10.32", "192.168.10.40", "192.168.10.48"], 1, "Le masque /28 donne un pas de 16. Les réseaux sont 0, 16, 32, 48. 45 est dans le bloc [32-47], donc le réseau est .32."),
    ("IPv4", "Quelle est l'adresse de diffusion (Broadcast) du réseau 10.1.1.0/24 ?", ["10.1.1.0", "10.1.1.1", "10.1.1.254", "10.1.1.255"], 3, "Dans un /24, la dernière adresse du bloc est .255, qui est le broadcast."),
    ("IPv4", "Quelle plage d'adresses correspond à la classe B privée ?", ["10.0.0.0 - 10.255.255.255", "172.16.0.0 - 172.31.255.255", "192.168.0.0 - 192.168.255.255", "169.254.0.0 - 169.254.255.255"], 1, "Les adresses privées classe B sont définies par la RFC 1918 de 172.16.0.0 à 172.31.255.255."),
    ("IPv6", "Comment peut-on abréger l'adresse IPv6 : 2001:0db8:0000:0000:0000:ff00:0042:8329 ?", ["2001:db8::ff00:42:8329", "2001:db8::ff::42:8329", "2001:0db8::ff00:0042:8329", "2001:db8:0:0:0:ff00:42:8329"], 0, "Les zéros de gauche sont supprimés, et la plus longue suite de blocs de zéros est remplacée par :: (une seule fois)."),
    ("IPv6", "Quel est l'équivalent IPv6 de l'adresse de boucle locale (loopback) 127.0.0.1 ?", ["FE80::1", "FF02::1", "::1", "2000::1"], 2, "::1 est l'adresse de loopback en IPv6."),
    ("IPv6", "À quoi sert une adresse commençant par FE80:: ?", ["C'est une adresse Multicast", "C'est une adresse Link-Local", "C'est une adresse Globale (Publique)", "C'est une adresse Anycast"], 1, "FE80::/10 désigne les adresses Link-Local, valables uniquement sur le lien local (le segment réseau)."),
    ("TCP/UDP", "Quel port est utilisé par défaut pour HTTPS ?", ["80", "21", "22", "443"], 3, "Le port 443 est utilisé pour HTTPS (HTTP sécurisé via TLS/SSL)."),
    
    # Module 3 : Commutation, VLAN, STP
    ("Switch", "Que fait un switch lorsqu'il reçoit une trame dont l'adresse MAC de destination est inconnue ?", ["Il supprime la trame", "Il l'envoie à la passerelle par défaut", "Il la diffuse (flood) sur tous les ports sauf celui de réception", "Il demande au routeur"], 2, "C'est l'opération de 'Flooding'. Les trames Unknown Unicast sont envoyées sur tous les autres ports."),
    ("VLAN", "Quelle commande permet d'assigner le port FastEthernet 0/1 au VLAN 10 ?", ["switchport mode trunk", "switchport access vlan 10", "vlan 10 name SALES", "ip address 192.168.10.1"], 1, "La commande 'switchport access vlan 10' place l'interface physique en mode accès pour le VLAN spécifié."),
    ("Trunking", "Quel protocole d'encapsulation est le standard ouvert pour les liens Trunk ?", ["ISL", "802.1Q", "DTP", "VTP"], 1, "IEEE 802.1Q est le standard ouvert universel. ISL est propriétaire Cisco et obsolète."),
    ("VLAN", "Qu'est-ce que le VLAN natif (Native VLAN) dans 802.1Q ?", ["Le VLAN où passent toutes les données de gestion", "Le VLAN pour les paquets non tagués sur un lien trunk", "Le VLAN par défaut (VLAN 1) qui ne peut pas être changé", "Le VLAN utilisé par DTP"], 1, "Le Native VLAN permet de faire passer du trafic sans étiquette (untagged) sur un lien Trunk. Par défaut c'est le VLAN 1."),
    ("DTP", "Si l'interface A est en 'dynamic auto' et l'interface B en 'dynamic auto', quel sera l'état du lien ?", ["Access", "Trunk", "Désactivé", "Erreur"], 0, "Deux interfaces en 'dynamic auto' négocieront un lien Access car aucune des deux n'initie activement la négociation Trunk."),
    ("STP", "Dans STP (802.1D), quel est l'état d'un port qui reçoit des BPDUs mais ne transmet aucune donnée ?", ["Forwarding", "Learning", "Blocking", "Listening"], 2, "L'état Blocking empêche les boucles. Le port reçoit les BPDUs pour détecter les changements, mais ne transmet pas de trames utilisateur."),
    ("RSTP", "Quels sont les états de port dans Rapid STP (802.1w) ?", ["Blocking, Listening, Learning, Forwarding", "Discarding, Learning, Forwarding", "Disabled, Blocking, Forwarding", "Listening, Learning, Forwarding"], 1, "RSTP fusionne Disabled, Blocking et Listening en un seul état : Discarding."),
    ("EtherChannel", "Quels sont les protocoles utilisés pour négocier un EtherChannel ?", ["STP et RSTP", "PAgP et LACP", "VTP et DTP", "CDP et LLDP"], 1, "PAgP (Cisco) et LACP (Standard IEEE 802.3ad) sont utilisés pour agréger plusieurs liens physiques en un lien logique."),
    ("EtherChannel", "En LACP, quels modes formeront un EtherChannel avec succès ?", ["Passive et Passive", "Active et Passive", "On et Active", "Auto et Desirable"], 1, "LACP utilise Active/Passive. Si l'un est Active et l'autre Passive (ou Active), le canal se forme. PAgP utilise Desirable/Auto."),
    ("CDP/LLDP", "Quelle est la principale différence entre CDP et LLDP ?", ["LLDP est pour la couche 3, CDP pour la couche 2", "CDP est propriétaire Cisco, LLDP est un standard ouvert", "CDP consomme moins de bande passante", "LLDP est utilisé pour le routage"], 1, "Cisco Discovery Protocol (CDP) ne fonctionne qu'entre équipements Cisco. LLDP est le standard IEEE 802.1AB inter-constructeurs."),

    # Module 4 : Routage
    ("Routage Statique", "Quelle est la syntaxe exacte d'une route statique vers le réseau 10.1.2.0/24 via 192.168.1.1 ?", ["ip route 10.1.2.0 255.255.255.0 192.168.1.1", "route 10.1.2.0/24 192.168.1.1", "ip route 192.168.1.1 10.1.2.0 255.255.255.0", "ip route static 10.1.2.0/24 next-hop 192.168.1.1"], 0, "La syntaxe est : ip route [réseau_destination] [masque] [ip_prochain_saut]"),
    ("Routage Statique", "Qu'est-ce qu'une Floating Static Route (Route statique flottante) ?", ["Une route avec une métrique OSPF de 0", "Une route de secours avec une distance administrative (AD) artificiellement élevée", "Une route qui s'efface quand le routeur redémarre", "Une route par défaut"], 1, "En augmentant l'AD (ex: ip route x.x.x.x y.y.y.y z.z.z.z 200), la route ne s'active que si la route principale (AD plus faible) tombe."),
    ("OSPF", "Que représente l'ID de routeur (Router ID) dans OSPF ?", ["L'adresse MAC de l'interface", "L'adresse IP la plus élevée configurée sur les interfaces loopback, sinon l'IP physique la plus élevée", "Le numéro de l'Area OSPF", "Le processus ID OSPF"], 1, "Le Router ID identifie le routeur. Il choisit d'abord la commande 'router-id', puis la plus haute IP Loopback, puis la plus haute IP physique active."),
    ("OSPF", "Dans un réseau Broadcast (Ethernet), quels routeurs OSPF forment une adjacence complète (FULL) avec tous les autres routeurs ?", ["Tous les routeurs entre eux", "Seulement le DR (Designated Router) et BDR", "Aucun routeur", "Les routeurs DROther entre eux"], 1, "Dans un réseau multi-accès, les routeurs (DROther) ne forment des adjacences complètes qu'avec le DR et le BDR pour limiter le trafic (état 2-WAY entre DROthers)."),
    ("OSPF", "Quelle table OSPF contient l'image de la topologie réseau complète (LSDB) ?", ["Table de routage", "Table de voisinage", "Table topologique", "Table ARP"], 2, "La LSDB (Link State Database) ou table topologique contient tous les LSA reçus pour cartographier l'Area complète."),
    ("Routage inter-VLAN", "Comment s'appelle l'approche où l'on configure des sous-interfaces sur un routeur pour router entre des VLANs ?", ["Switch Virtual Interface (SVI)", "Router-on-a-Stick (ROAS)", "Port Routing", "Layer 3 EtherChannel"], 1, "ROAS utilise une seule interface physique divisée en sous-interfaces (ex: int g0/0.10) connectée à un port Trunk sur le switch."),
    ("SVI", "Que faut-il configurer sur un Switch Multicouche pour faire du routage inter-VLAN ?", ["Des sous-interfaces physiques", "Des interfaces virtuelles SVI (ex: int vlan 10) et activer 'ip routing'", "Un protocole VTP", "Des routes statiques flottantes"], 1, "Un switch Layer 3 utilise des SVI (Switch Virtual Interfaces) comme passerelles par défaut pour chaque VLAN et la commande 'ip routing' globale."),
    ("Processus de Routage", "Que se passe-t-il avec l'adresse MAC source et destination lorsqu'un paquet traverse un routeur ?", ["Elles restent identiques de bout en bout", "Elles sont remplacées par celles du routeur entrant et sortant", "Elles sont supprimées", "Seule l'adresse MAC destination change"], 1, "Contrairement aux adresses IP (qui restent de bout en bout sauf en cas de NAT), les adresses MAC sont réécrites à chaque saut de routeur (Hop)."),
    ("FHR (HSRP)", "Quel protocole propriétaire Cisco fournit une redondance de passerelle par défaut ?", ["VRRP", "GLBP", "HSRP", "STP"], 2, "Hot Standby Router Protocol (HSRP) permet à deux routeurs de partager une IP Virtuelle (VIP) et une MAC Virtuelle pour servir de passerelle redondante."),
    ("FHR (HSRP)", "Quel est l'état du routeur de secours dans HSRP ?", ["Passive", "Backup", "Standby", "Secondary"], 2, "Dans HSRP, on a un routeur Active (qui transmet le trafic) et un routeur Standby (en attente)."),

    # Module 5 : Services, Sécurité
    ("ACL", "Quelle est la plage des numéros pour une Access Control List (ACL) standard ?", ["1-99", "100-199", "2000-2999", "1000-1999"], 0, "Les ACL Standards utilisent les numéros 1-99 (et 1300-1999). Les étendues utilisent 100-199."),
    ("ACL", "Que contient toujours, de manière invisible, la fin d'une ACL Cisco ?", ["Un permit ip any any", "Un deny any (Implicit deny)", "Un log all", "Un return"], 1, "Il y a toujours un 'Implicit Deny' (deny any) à la fin. Si un paquet ne correspond à aucune règle 'permit', il est rejeté."),
    ("ACL", "Où doit-on placer une ACL Standard (bonne pratique) ?", ["Le plus près de la source", "Le plus près de la destination", "Sur le routeur de cœur (Core)", "Sur l'interface WAN"], 1, "Une ACL standard filtrant uniquement sur l'IP Source, la placer trop près de la source bloquerait l'accès à tous les autres réseaux. On la place donc près de la destination."),
    ("NAT", "Quel type de NAT mappe plusieurs IPs privées vers une seule IP publique en utilisant les numéros de port (Port Address Translation) ?", ["NAT Statique", "NAT Dynamique", "PAT (NAT Overload)", "NAT IPv6"], 2, "PAT (souvent appelé NAT Overload chez Cisco) surcharge une IP publique en différenciant les sessions via les ports TCP/UDP source (Layer 4)."),
    ("DHCP", "Quelle est la première étape (message) du processus DORA d'un client DHCP ?", ["DHCP Offer", "DHCP Request", "DHCP Discover", "DHCP Ack"], 2, "Le client diffuse un DHCP Discover (en Broadcast) pour trouver un serveur DHCP disponible."),
    ("DNS", "Quel port est utilisé par le protocole DNS ?", ["TCP 80", "UDP 53", "TCP 21", "UDP 67"], 1, "DNS utilise l'UDP port 53 pour les requêtes normales, et parfois TCP 53 pour les transferts de zone ou les très grandes réponses."),
    ("NTP", "À quoi sert le protocole NTP ?", ["Traduire les noms de domaine en IPs", "Attribuer des IPs dynamiquement", "Synchroniser l'horloge (l'heure) des équipements réseau", "Transférer des fichiers de configuration"], 2, "Network Time Protocol (NTP) est essentiel pour que tous les équipements aient la même heure, critique pour l'analyse des logs (Syslog) et la sécurité (certificats)."),
    ("Port Security", "Quel est le comportement par défaut d'un port switch Cisco (Port Security Violation mode = Shutdown) lorsqu'une MAC non autorisée se connecte ?", ["Il ignore l'adresse et continue", "Il supprime la trame et génère un log (Restrict)", "Il passe le port en état err-disabled (Désactivé)", "Il bloque juste le trafic de cette MAC (Protect)"], 2, "Le mode Shutdown (défaut) coupe complètement le port et le met en 'err-disabled' jusqu'à l'intervention d'un admin (shut / no shut)."),
    ("Sécurité L2", "Quelle attaque consiste à saturer la table MAC d'un switch pour le forcer à agir comme un hub ?", ["MAC Spoofing", "MAC Flooding", "ARP Poisoning", "DHCP Starvation"], 1, "Le MAC Flooding envoie des milliers de fausses MAC sources. La table s'épuise, et le switch doit faire du 'Flooding' de toutes les trames, permettant l'interception."),
    ("AAA", "Quels sont les composants du modèle AAA ?", ["Authentification, Autorisation, Audit", "Authentification, Autorisation, Accounting (Traçabilité)", "Accès, Autorisation, Administration", "Anycast, ARP, ACL"], 1, "AAA = Authentication (Qui es-tu?), Authorization (Que peux-tu faire?), Accounting (Qu'as-tu fait?)."),

    # Module 6 : Wi-Fi, SDN, Automatisation, Dépannage
    ("Wi-Fi", "Quelle est la norme IEEE pour le Wi-Fi 6 ?", ["802.11a", "802.11n", "802.11ac", "802.11ax"], 3, "802.11ax est la norme du Wi-Fi 6 (très haut débit, OFDMA). 802.11ac est le Wi-Fi 5."),
    ("Wi-Fi", "Quel est le rôle d'un WLC (Wireless LAN Controller) dans l'architecture centralisée Cisco ?", ["Servir d'antenne physique pour les clients", "Gérer et configurer tous les Lightweight APs (LAPs) de manière centralisée", "Bloquer les attaques DDoS Internet", "Fournir des IP via DHCP uniquement"], 1, "Le WLC centralise l'intelligence, la configuration, et la sécurité des points d'accès légers (LAPs) qui s'y connectent via des tunnels CAPWAP."),
    ("SDN", "Dans une architecture SDN, quel plan est centralisé sur le Contrôleur ?", ["Plan de Données (Data Plane)", "Plan de Contrôle (Control Plane)", "Plan de Gestion (Management Plane)", "Plan Physique"], 1, "Le SDN sépare le Control Plane (intelligence, routage) du Data Plane (transfert matériel). Le Control Plane est centralisé dans le contrôleur SDN (ex: DNA Center)."),
    ("API / REST", "Quelle méthode HTTP est utilisée pour mettre à jour ou modifier entièrement une ressource via une API REST ?", ["GET", "POST", "PUT", "DELETE"], 2, "PUT remplace la ressource. POST crée. GET lit. PATCH modifie partiellement. DELETE supprime."),
    ("JSON", "Quel format de données est le plus couramment utilisé avec les API REST ?", ["XML", "CSV", "JSON", "YAML"], 2, "JSON (JavaScript Object Notation) est devenu le standard de facto pour les APIs REST grâce à sa légèreté et sa lisibilité."),
    ("Automatisation", "Lequel de ces outils de gestion de configuration est 'Agentless' (sans agent) et utilise SSH par défaut ?", ["Puppet", "Chef", "Ansible", "SaltStack"], 2, "Ansible (basé sur Python) ne nécessite aucun agent préinstallé sur les routeurs/switchs. Il se connecte simplement via SSH et pousse la configuration (souvent YAML)."),
    ("SDN", "Quelle est l'interface (API) utilisée par le Contrôleur SDN pour communiquer avec le matériel réseau (Switchs/Routeurs) ?", ["Northbound API (API Nord)", "Southbound API (API Sud)", "Eastbound API", "Westbound API"], 1, "Les APIs Southbound (Sud), comme OpenFlow ou NETCONF, parlent au matériel. Les APIs Northbound (Nord), souvent REST, parlent aux applications métier."),
    ("Dépannage", "Si un PC peut pinger son adresse de Loopback (127.0.0.1) mais pas sa passerelle par défaut, que cela indique-t-il ?", ["La carte réseau (TCP/IP) fonctionne, mais il y a un problème de liaison locale (câble, VLAN, IP passerelle).", "La carte réseau est morte.", "Le DNS est en panne.", "Le routeur distant est éteint."], 0, "Le ping 127.0.0.1 prouve que la pile TCP/IP logicielle de l'OS est saine. L'échec vers la passerelle pointe vers la Couche 1/2 locale ou un mauvais paramètre IP (masque/passerelle)."),
    ("Dépannage", "Que permet d'isoler la commande 'traceroute' (tracert) ?", ["Les requêtes DNS lentes", "Les conflits d'adresses MAC", "L'équipement précis (routeur) où le paquet s'arrête ou se perd sur le chemin", "L'utilisation CPU du switch"], 2, "Traceroute montre chaque saut (Hop) vers la destination. Si ça bloque au saut 3, vous savez que le problème se situe au niveau du routeur 3."),
    ("Administration", "Quel port est utilisé par le protocole SSH pour une connexion sécurisée ?", ["TCP 23", "TCP 22", "UDP 22", "TCP 443"], 1, "SSH (Secure Shell) utilise TCP 22 pour crypter les sessions d'administration, remplaçant ainsi Telnet (TCP 23) qui est non sécurisé.")
]

# Generate HTML
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏆 Simulateur 50 Exams CCNA - Corrigés</title>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Kalam:wght@400;700&family=Patrick+Hand&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#f7f1e1; --paper-2:#fffdf6; --ink:#1f2d4d;
  --blue:#2a5db0; --red:#c0392b; --green:#1e7a4c;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Patrick Hand', cursive; background: var(--paper); color: var(--ink); padding: 15px; font-size: 1.1rem; }
.header { text-align: center; margin: 20px 0 40px; }
.header h1 { font-family: 'Caveat', cursive; font-size: 3rem; color: var(--blue); line-height:1.2; }
.header a { display: inline-block; margin-top: 15px; padding: 10px 20px; background: var(--blue); color: white; text-decoration: none; border-radius: 20px; font-family:'Kalam',cursive; font-weight:bold; box-shadow:0 4px 10px rgba(0,0,0,0.15); transition:transform 0.2s; }
.header a:hover { transform: scale(1.05); }
.exam-container { max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 20px; padding-bottom: 50px; }
.q-card { background: var(--paper-2); border: 2px solid var(--ink); border-radius: 15px; padding: 20px; box-shadow: 4px 4px 0 rgba(31,45,77,.1); }
.q-card h3 { font-family: 'Kalam', cursive; color: var(--red); margin-bottom: 12px; border-bottom: 2px dashed var(--ink); padding-bottom: 5px; }
.q-text { font-size: 1.25rem; margin-bottom: 15px; font-weight:bold; }
.options { list-style: none; margin-bottom: 15px; }
.options li { margin-bottom: 10px; padding: 10px 15px; background: rgba(0,0,0,0.03); border: 2px solid rgba(0,0,0,0.05); border-radius: 8px; cursor: pointer; transition: background 0.2s; }
.options li:hover { background: rgba(42,93,176,0.1); border-color: var(--blue); }
details { background: #eaf7ef; border: 2px solid var(--green); border-radius: 10px; padding: 12px; cursor: pointer; outline:none; }
summary { font-weight: bold; color: var(--green); outline: none; font-size: 1.1rem; list-style:none; display:flex; align-items:center; }
summary::-webkit-details-marker { display:none; }
summary::before { content:"👀 "; margin-right:8px; }
.corrige { margin-top: 12px; padding-top: 12px; border-top: 2px dashed var(--green); font-size: 1.1rem; }
.score-box { position:fixed; bottom:20px; left:50%; transform:translateX(-50%); background:var(--ink); color:white; padding:10px 20px; border-radius:30px; font-family:'Kalam',cursive; font-weight:bold; box-shadow:0 5px 15px rgba(0,0,0,0.3); z-index:100; display:none; }
</style>
</head>
<body>
  <div class="header">
    <h1>🏆 Mega Simulateur - 50 Questions CCNA</h1>
    <p>50 Questions d'examen Premium avec leurs corrigés détaillés (Niveau 200-301).</p>
    <a href="ccna_pro_complet.html">⬅ Retourner au Cours Principal</a>
  </div>
  <div class="exam-container">
"""

letters = ["A", "B", "C", "D"]

for i, (topic, q, opts, ans_idx, expl) in enumerate(q_data, start=1):
    opts_html = ""
    for j, opt in enumerate(opts):
        opts_html += f"<li><strong>{letters[j]}.</strong> {opt}</li>\n"
    
    html_content += f"""
    <div class="q-card" id="q{i}">
      <h3>Question {i} - {topic}</h3>
      <p class="q-text">{q}</p>
      <ul class="options">
        {opts_html}
      </ul>
      <details>
        <summary>Afficher le Corrigé Détaillé</summary>
        <div class="corrige">
          <p><strong>Réponse Correcte : {letters[ans_idx]}</strong></p>
          <p><em>Explication :</em> {expl}</p>
        </div>
      </details>
    </div>
"""

html_content += """
  </div>
  <script>
    // Interaction script
    document.querySelectorAll('.options li').forEach(li => {
      li.addEventListener('click', function() {
        this.parentNode.querySelectorAll('li').forEach(el => el.style.background = 'rgba(0,0,0,0.03)');
        this.style.background = '#ffe680';
        this.style.borderColor = '#d97706';
      });
    });
  </script>
</body>
</html>
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Add the button to the main file
main_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(main_path, "r", encoding="utf-8") as f:
    main_html = f.read()

btn_link = '<a href="ccna_exams.html" class="btn green" style="text-decoration:none; margin-left: 10px;">🏆 50 Exams</a>'

if "ccna_exams.html" not in main_html:
    main_html = main_html.replace('<div class="progress-wrap"', btn_link + '\n    <div class="progress-wrap"')
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(main_html)
