import re
import sys

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

deep_content = {
    "p1": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Architecture et Redondance :</strong> Dans les réseaux d'entreprise (WAN), on utilise des topologies <strong>Maillées (Full Mesh)</strong> pour assurer une tolérance aux pannes maximale. Le nombre total de liens se calcule via <code>N(N-1)/2</code>.</p>
      <p><strong>Équipement Central :</strong> Le <strong>Switch (Commutateur L2)</strong> est au cœur de la topologie Étoile. Si ce switch tombe en panne, tout le réseau local (domaine de diffusion) est coupé (Single Point of Failure).</p>
    </div>
    """,
    "p2": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Couche 2 vs Couche 3 :</strong> La transmission à la Couche 2 (Trame) est <em>strictement locale</em> au LAN. Pour traverser des routeurs et aller sur Internet, la donnée doit être encapsulée dans la Couche 3 (Paquet) avec une IP logique routable.</p>
      <p><strong>Inspection et TCP :</strong> Un pare-feu qui bloque HTTP (port 80) doit inspecter l'en-tête de la <strong>Couche 4 (Transport)</strong>. En analysant le réseau avec Wireshark, l'établissement d'une session TCP se fait via un mécanisme appelé <strong>Three-Way Handshake</strong> : <code>SYN</code>, puis <code>SYN-ACK</code>, et enfin <code>ACK</code>.</p>
    </div>
    """,
    "p3": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>VLSM (Variable Length Subnet Mask) :</strong> Le VLSM permet d'emprunter des bits hôtes pour créer des sous-réseaux de tailles différentes, évitant le gaspillage. Pour calculer les hôtes, on utilise <code>2^h - 2</code>. Pour les sous-réseaux, c'est <code>2^s</code>. Lors d'un design, <strong>commencez toujours par le sous-réseau exigeant le plus grand nombre d'hôtes</strong>.</p>
      <p><strong>Cas Pratique :</strong> Si deux routeurs ont les adresses 192.168.1.5/30 et 192.168.1.9/30 reliées directement, le ping échouera. Pourquoi ? Le masque /30 donne des sous-réseaux par incréments de 4 (.0, .4, .8, .12). L'IP .5 est dans le réseau .4, tandis que l'IP .9 est dans le réseau .8. Ils ne sont pas dans le même réseau de Couche 3 !</p>
    </div>
    """,
    "p4": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>EUI-64 et Adressage Automatique :</strong> Pour générer automatiquement la partie Hôte (Interface ID, 64 bits), on prend l'adresse MAC (48 bits), on la coupe en deux, on insère <strong>FFFE</strong> au milieu, et on inverse le <strong>7ème bit</strong> (Universal/Local bit) du premier octet.</p>
      <p><strong>SLAAC et ICMPv6 :</strong> IPv6 n'utilise plus de Broadcast (pas d'ARP). Il utilise le Neighbor Discovery Protocol (NDP). Pour s'auto-configurer, le PC écoute les messages <strong>Router Advertisement (RA)</strong> envoyés en multicast (FF02::2) contenant le préfixe réseau, après avoir sollicité le réseau via un <strong>Router Solicitation (RS)</strong>.</p>
    </div>
    """,
    "p5": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Séquence de Démarrage (Boot Process) :</strong> 1. La ROM exécute le POST et lance le Bootstrap. 2. Le Bootstrap charge l'image Cisco IOS depuis la <strong>Mémoire Flash</strong> vers la RAM. 3. L'IOS charge le fichier <code>startup-config</code> depuis la <strong>NVRAM</strong> vers la <strong>RAM</strong>.</p>
      <p><strong>Récupération de Mot de Passe :</strong> Si le mot de passe est perdu, on redémarre le routeur et on interrompt le processus pour entrer en mode <strong>ROMMON</strong>. On modifie ensuite le <strong>Configuration Register</strong> à <code>0x2142</code> pour forcer le routeur à ignorer la NVRAM au prochain démarrage.</p>
    </div>
    """,
    "p6": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>STP (Spanning Tree Protocol) & Élection :</strong> L'élection du Root Bridge L2 se base sur le <strong>Bridge ID (BID)</strong> qui combine la Priorité et l'adresse MAC. La règle d'or : <em>La valeur la plus basse l'emporte</em> (L'adresse IP n'a aucun rôle ici). STP empêche les boucles (Broadcast Storms).</p>
      <p><strong>RSTP et Sécurité :</strong> RSTP (802.1w) accélère la convergence. Les 3 états des ports sont : <strong>Discarding, Learning, Forwarding</strong>. Pour sécuriser un port vers un PC et supprimer le délai d'écoute de 30s, on active <code>spanning-tree portfast</code> combiné à <code>bpduguard enable</code>. Si une trame BPDU est reçue sur un tel port, il passe en erreur <strong>err-disable</strong> immédiatement.</p>
    </div>
    """,
    "p7": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Trunking et 802.1Q :</strong> Pour faire passer plusieurs VLANs sur un câble, on crée un Lien Trunk L2. Le standard <strong>802.1Q</strong> insère un tag de 4 octets dans l'en-tête Ethernet. Le VLAN Natif (Native VLAN) est le seul à circuler <em>sans tag</em>.</p>
      <p><strong>Routage Inter-VLAN (ROAS) :</strong> Si les PC du VLAN 10 ne joignent pas la passerelle G0/0.10, les causes fréquentes sont : le port du switch n'est pas en mode <code>trunk</code>, ou la commande <code>encapsulation dot1Q 10</code> manque sur le routeur. Côté EtherChannel (Agrégation), les modes LACP sont <strong>Active/Passive</strong> tandis que DTP (négociation Trunk) utilise <strong>Dynamic Desirable/Auto</strong>. Si deux switchs sont en mode 'auto', le Trunk ne montera jamais.</p>
    </div>
    """,
    "p8": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Logique de Routage :</strong> Le routeur choisit le meilleur chemin en regardant d'abord la correspondance la plus précise (<strong>Longest Prefix Match</strong>). En cas d'égalité, il choisit la <strong>Distance Administrative (AD)</strong> la plus basse (Static=1, OSPF=110). Enfin, il regarde la <strong>Métrique</strong>.</p>
      <p><strong>Floating Static Route :</strong> C'est une route de secours. Si OSPF (AD 110) est actif, on peut configurer une route statique avec une AD de 115 : <code>ip route 0.0.0.0 0.0.0.0 10.0.0.1 115</code>. Tant qu'OSPF fonctionne, cette route statique reste masquée. Elle ne s'activera qu'en cas de panne de l'OSPF.</p>
    </div>
    """,
    "p9": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Mécanique de OSPFv2 (Link-State) :</strong> OSPF ne partage pas juste des routes, il construit une base de données topologique L3 (<strong>LSDB</strong>) via des paquets <strong>LSA</strong> (Link State Advertisements). Chaque routeur calcule ensuite son arbre grâce à l'algorithme <strong>SPF de Dijkstra</strong>.</p>
      <p><strong>Élection DR/BDR :</strong> Sur les réseaux partagés (Ethernet), les routeurs élisent un DR (Designated Router) pour centraliser les LSAs. L'élection se base sur la priorité la plus haute, puis sur le <strong>Router-ID</strong> le plus élevé (l'adresse loopback configurée, ou l'IP active la plus haute).</p>
    </div>
    """,
    "p10": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>ACL et Masque Générique (Wildcard) :</strong> L'ACL filtre le trafic L3 et L4. Le Wildcard Mask est l'inverse du sous-réseau : les '0' exigent une correspondance exacte, les '1' ignorent la vérification. L'ACL possède toujours un <strong>Implicit Deny Any Any</strong> invisible à la fin : si aucune ligne ne correspond, le paquet est détruit.</p>
      <p><strong>Placement Stratégique :</strong> Règle Cisco : l'ACL <strong>Étendue</strong> (qui filtre Source, Destination, et Port) se place le plus <em>proche possible de la source</em> pour bloquer le trafic indésirable rapidement. L'ACL <strong>Standard</strong> (qui ne filtre que la source) se place le plus <em>proche de la destination</em>.</p>
    </div>
    """,
    "p11": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Vocabulaire NAT Cisco :</strong> <em>Inside Local</em> = Votre IP privée (192.168.x.x). <em>Inside Global</em> = L'IP publique de votre box internet. <em>Outside Global</em> = L'IP du serveur distant (ex: Google) telle qu'elle est sur le web.</p>
      <p><strong>PAT (Port Address Translation) :</strong> Aussi appelé NAT Overload. C'est le type de NAT utilisé dans 99% des cas (Box maison/entreprise). Il permet à des milliers de PC privés de partager <strong>une seule IP publique</strong> en modifiant dynamiquement le <strong>Numéro de Port Source (L4)</strong> pour distinguer les sessions.</p>
    </div>
    """,
    "p12": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Le processus DORA :</strong> <code>Discover (Broadcast) -> Offer (Unicast) -> Request (Broadcast) -> Acknowledge (Unicast)</code>. Si le serveur DHCP L3 n'est pas sur le même LAN que le client L2, les routeurs bloquent le broadcast. Il faut configurer un relais avec la commande <code>ip helper-address</code> sur l'interface du routeur !</p>
      <p><strong>Enregistrements DNS L7 :</strong> Type <strong>A</strong> = Mappe un nom à une adresse IPv4. Type <strong>AAAA</strong> = Mappe vers une IPv6. Type <strong>CNAME</strong> = Alias (surnom) vers un autre nom d'hôte. Type <strong>MX</strong> = Indique l'adresse du serveur d'échange d'Emails.</p>
    </div>
    """,
    "p13": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Sécurité L2 et DHCP Snooping :</strong> Pour contrer les Rogue DHCP et le MAC Flooding, le switch L2 utilise DHCP Snooping (bloque les réponses DHCP sauf sur les ports dits "Trusteds") et <strong>Port-Security</strong> (mode <em>Restrict</em> : bloque le trafic pirate, laisse passer les légitimes, incrémente un compteur de violation).</p>
      <p><strong>Sécurité des Mots de Passe & AAA :</strong> Utilisez <code>enable secret</code> qui chiffre nativement en <strong>MD5 / SHA-256 (Type 5 ou 8)</strong>, et non <code>service password-encryption</code> (Type 7 faible). Pour authentifier les admins via un serveur centralisé, le protocole <strong>TACACS+</strong> chiffre l'ensemble du paquet (idéal pour l'admin), tandis que <strong>RADIUS</strong> ne chiffre que le mot de passe (idéal pour le 802.1X).</p>
    </div>
    """,
    "p14": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Collision Avoidance (CSMA/CA) :</strong> Le réseau Wi-Fi est un média partagé Half-Duplex. Il utilise l'évitement (Avoidance) de collision via des accusés (ACK). WPA3 modernise la sécurité et empêche le brute-force hors ligne grâce au protocole d'authentification <strong>SAE (Simultaneous Authentication of Equals)</strong>.</p>
      <p><strong>WLC et Mode FlexConnect :</strong> Dans un réseau d'entreprise, les bornes (AP) montent des tunnels <strong>CAPWAP</strong> (Contrôle UDP 5246, Data UDP 5247) vers le Contrôleur WLC. Si le lien WAN coupe, un AP en mode <strong>FlexConnect</strong> reste opérationnel (Standalone) et commute localement les trames de données au niveau L2 sur le switch distant.</p>
    </div>
    """,
    "p15": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Architecture SDN :</strong> Le SDN sépare le <strong>Data Plane</strong> (sur les switchs pour forwarder le trafic via ASICs L1/L2) et le <strong>Control Plane</strong> (la "matière grise", le cerveau, centralisé dans un contrôleur comme Cisco DNA Center L7).</p>
      <p><strong>Outils et API :</strong> Les scripts communiquent avec les équipements via les méthodes REST API (GET, PUT, POST) et le format de données standard <strong>JSON</strong>. Pour déployer des configurations en masse <em>sans</em> installer de logiciel agent sur les vieux routeurs Cisco, on privilégie <strong>Ansible</strong> (basé sur Python, agentless via SSH) plutôt que Puppet ou Chef (qui requièrent des agents).</p>
    </div>
    """,
    "p16": r"""
    <div class="expert-details" style="margin-top: 20px; padding: 15px; border-left: 4px solid var(--purple); background: #f3ecfd; border-radius: 8px;">
      <h3 style="color: var(--purple); margin-top: 0; font-family:'Caveat',cursive; font-size:1.6rem;">🔬 Détails Techniques (Niveau CCNA)</h3>
      <p><strong>Découverte du Réseau L2 :</strong> Pour connaître les voisins L2 directement connectés sans avoir de carte réseau, on utilise le protocole propriétaire <strong>CDP (Cisco Discovery Protocol)</strong> ou le standard ouvert <strong>LLDP (Link Layer Discovery Protocol)</strong>.</p>
      <p><strong>Trace de Chemin L3 :</strong> La commande <code>traceroute</code> (ou tracert sous Windows) identifie les sauts de routeurs en manipulant intelligemment le champ <strong>TTL (Time To Live)</strong> de l'en-tête IPv4. Il envoie un TTL=1 pour obtenir un message d'erreur ICMP du premier routeur, puis TTL=2 pour le second, et ainsi de suite.</p>
    </div>
    """
}

# Inject the deep_content string immediately before <section class="exercices">
for pid, content in deep_content.items():
    pattern = rf'(<article class="poster" id="{pid}".*?>.*?(?=<section class="exercices">))'
    html = re.sub(pattern, rf'\g<1>{content}\n    ', html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
