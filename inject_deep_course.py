import os
import re

html_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Subnetting Deep Dive (Module 2, p03)
subnetting_html = """
    <img src="subnetting_math.jpg" alt="Explication du Subnetting et Adresses IP" class="course-img" style="border-radius:12px; border:2px solid var(--ink); margin: 20px 0;">
    <div class="expert-details" style="margin-top: 20px; padding: 20px; border-left: 5px solid var(--blue); background: #eaf2f8; border-radius: 8px;">
      <h3 style="color: var(--blue); margin-top: 0; font-family:'Caveat',cursive; font-size:1.8rem;">🧮 Méthode de Calcul Subnetting (VLSM)</h3>
      <p>Pour le CCNA, vous devez calculer de tête rapidement. Voici la méthode infaillible pour une adresse comme <strong>192.168.10.68 /26</strong> :</p>
      <ol style="margin-left: 20px; margin-bottom: 15px;">
        <li><strong>Trouver le Pas (Magic Number) :</strong> Le /26 signifie qu'on a emprunté 2 bits dans le dernier octet. Le nouveau masque est 255.255.255.192. Le "Pas" = 256 - 192 = <strong>64</strong>.</li>
        <li><strong>Trouver les réseaux (Network ID) :</strong> Les réseaux vont de 64 en 64 (0, 64, 128, 192). L'IP 68 se trouve entre 64 et 128. L'adresse réseau est donc <strong>192.168.10.64</strong>.</li>
        <li><strong>Trouver l'adresse de diffusion (Broadcast) :</strong> C'est l'adresse juste avant le réseau suivant (128 - 1). Le Broadcast est <strong>192.168.10.127</strong>.</li>
        <li><strong>Trouver la plage utilisable (Hosts) :</strong> Du réseau +1 au broadcast -1. Soit de <strong>192.168.10.65</strong> à <strong>192.168.10.126</strong>.</li>
      </ol>
      <p>💡 <em>Astuce Packet Tracer :</em> N'assignez jamais l'adresse réseau (.64) ou broadcast (.127) à un PC, sinon Packet Tracer affichera l'erreur <code>Invalid IP address</code>.</p>
    </div>
"""

if "Méthode de Calcul Subnetting" not in html:
    html = html.replace('<li>Classes A, B, C, D, E</li>', '<li>Classes A, B, C, D, E</li>\n' + subnetting_html)


# 2. OSPF and Mermaid Topology (Module 4, p09)
ospf_lab_html = """
    <div class="expert-details" style="margin-top: 20px; padding: 20px; border-left: 5px solid var(--orange); background: #fdf3e3; border-radius: 8px;">
      <h3 style="color: var(--orange); margin-top: 0; font-family:'Caveat',cursive; font-size:1.8rem;">⚙️ Schéma et Lab OSPFv2 (Cisco Packet Tracer)</h3>
      <div class="mermaid" style="text-align: center; margin: 15px 0;">
        graph TD
        R1((Router R1<br>10.1.1.1/30)) ---|Serial0/0/0| R2((Router R2<br>10.1.1.2/30))
        R1 ---|Gig0/0| SW1[Switch LAN 1<br>192.168.10.0/24]
        R2 ---|Gig0/0| SW2[Switch LAN 2<br>192.168.20.0/24]
        style R1 fill:#f9f,stroke:#333,stroke-width:2px
        style R2 fill:#f9f,stroke:#333,stroke-width:2px
      </div>
      <p><strong>Commandes à taper dans R1 pour activer OSPF dans la zone 0 (Area 0) :</strong></p>
      <pre><code>R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 10.1.1.0 0.0.0.3 area 0
R1(config-router)# network 192.168.10.0 0.0.0.255 area 0
R1(config-router)# passive-interface Gig0/0</code></pre>
      <p><em>Explication :</em> La commande <code>passive-interface</code> empêche R1 d'envoyer des messages Hello OSPF vers le réseau local (LAN), ce qui sécurise le réseau et économise de la bande passante.</p>
    </div>
"""

if "Schéma et Lab OSPFv2" not in html:
    html = html.replace('<li>Types de LSA</li>', '<li>Types de LSA</li>\n' + ospf_lab_html)


# 3. VLANs Diagram & Engineer Image (Module 3, p07)
vlan_html = """
    <img src="ccna_engineer.jpg" alt="Ingénieur réseau configurant des équipements Cisco" class="course-img" style="border-radius:12px; border:2px solid var(--ink); margin: 20px 0;">
    <div class="expert-details" style="margin-top: 20px; padding: 20px; border-left: 5px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.8rem;">🏢 Schéma de Segmentation VLANs & Trunk</h3>
      <div class="mermaid" style="text-align: center; margin: 15px 0;">
        graph LR
        SW1[Switch Core] ===|Lien TRUNK 802.1Q| SW2[Switch Access]
        SW2 ---|Port Access<br>VLAN 10| PC1((PC Compta))
        SW2 ---|Port Access<br>VLAN 20| PC2((PC RH))
        style SW1 fill:#bbf,stroke:#333,stroke-width:2px
        style SW2 fill:#bbf,stroke:#333,stroke-width:2px
      </div>
      <p><strong>Comment configurer le Trunking (Packet Tracer) :</strong></p>
      <pre><code>SW1(config)# interface GigabitEthernet 0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20</code></pre>
    </div>
"""

if "Schéma de Segmentation VLANs" not in html:
    html = html.replace('<li>DTP (Dynamic Trunking Protocol)</li>', '<li>DTP (Dynamic Trunking Protocol)</li>\n' + vlan_html)


# 4. Ultimate Lab Guide (Module 6, p17 Labs pratiques)
packet_tracer_html = """
    <img src="packet_tracer_lab.jpg" alt="Interface Cisco Packet Tracer avec topologie réseau" class="course-img" style="border-radius:12px; border:2px solid var(--ink); margin: 20px 0;">
    <div class="expert-details" style="margin-top: 20px; padding: 20px; border-left: 5px solid var(--green); background: #eaf7ef; border-radius: 8px;">
      <h3 style="color: var(--green); margin-top: 0; font-family:'Caveat',cursive; font-size:1.8rem;">💻 Comment maîtriser Cisco Packet Tracer</h3>
      <p>Packet Tracer est l'outil officiel de simulation Cisco. Pour réussir le CCNA, vous devez pratiquer. Voici comment aborder chaque laboratoire (Lab) :</p>
      <ol style="margin-left: 20px; margin-bottom: 15px;">
        <li><strong>Placez les équipements :</strong> Ajoutez les Routeurs (série 4331), les Switchs (série 2960) et les PCs depuis le menu inférieur.</li>
        <li><strong>Câblez :</strong> Utilisez l'éclair noir (Câble droit) pour relier PC ➔ Switch ou Switch ➔ Routeur. Utilisez le câble croisé (pointillés) pour Routeur ➔ Routeur.</li>
        <li><strong>Le grand classique "Router-On-A-Stick" (ROAS) :</strong> C'est l'exercice numéro 1 au CCNA pour faire communiquer des VLANs différents.</li>
      </ol>
      <h4>Lab ROAS étape par étape (Routeur) :</h4>
      <pre><code>Router(config)# interface gigabitethernet 0/0/0
Router(config-if)# no shutdown
Router(config-if)# exit

Router(config)# interface gigabitethernet 0/0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0

Router(config)# interface gigabitethernet 0/0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0</code></pre>
      <p>⚠️ N'oubliez pas d'assigner l'IP <code>192.168.10.1</code> comme "Default Gateway" (Passerelle) dans la configuration du PC0 !</p>
    </div>
"""

if "Comment maîtriser Cisco Packet Tracer" not in html:
    # Inject before the table in p17
    html = html.replace('<h3>10 labs progressifs 🔥</h3>', '<h3>10 labs progressifs 🔥</h3>\n' + packet_tracer_html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
