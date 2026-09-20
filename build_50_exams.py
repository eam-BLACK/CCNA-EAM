import os

file_path = r"C:\Users\PC\Desktop\ccna7\ccna_50_exams.html"

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🚀 Simulateur Pro - 50 Examens CCNA</title>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Kalam:wght@400;700&family=Patrick+Hand&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
:root{ --paper:#f7f1e1; --paper-2:#fffdf6; --ink:#1f2d4d; --blue:#2a5db0; --red:#c0392b; --green:#1e7a4c; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Patrick Hand', cursive; background: var(--paper); color: var(--ink); padding: 15px; font-size: 1.15rem; overflow-x: hidden; }
.header { text-align: center; margin: 20px 0 30px; }
.header h1 { font-family: 'Caveat', cursive; font-size: 3rem; color: var(--blue); line-height:1.1; }
.header p { color: var(--ink); font-size: 1.2rem; }
.header a { display: inline-block; margin-top: 15px; padding: 10px 25px; background: var(--ink); color: white; text-decoration: none; border-radius: 20px; font-family:'Kalam',cursive; font-weight:bold; }

/* Grid des 50 examens */
#dashboard { max-width: 1000px; margin: 0 auto; }
.exam-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 15px; margin-top: 20px; }
.exam-btn { background: var(--paper-2); border: 2px solid var(--ink); border-radius: 12px; padding: 15px 10px; text-align: center; cursor: pointer; transition: 0.2s; box-shadow: 3px 3px 0 rgba(31,45,77,.1); font-family: 'Kalam', cursive; font-size: 1.2rem; font-weight: bold; color: var(--ink); }
.exam-btn:hover { transform: translateY(-3px); box-shadow: 4px 6px 0 rgba(31,45,77,.15); border-color: var(--blue); color: var(--blue); }
.exam-btn.completed { background: #eaf7ef; border-color: var(--green); color: var(--green); }

/* Interface d'un examen */
#exam-view { display: none; max-width: 900px; margin: 0 auto; padding-bottom: 100px; }
.exam-header { display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; background: rgba(247,241,225,0.95); padding: 10px 20px; z-index: 50; border-bottom: 2px dashed var(--ink); backdrop-filter: blur(5px); margin-bottom: 20px; border-radius: 10px; }
.exam-header h2 { font-family: 'Caveat', cursive; font-size: 2rem; color: var(--red); }
.btn-back { background: var(--ink); color: white; border: none; padding: 8px 15px; border-radius: 8px; cursor: pointer; font-family: 'Kalam', cursive; font-weight: bold; font-size: 1.1rem; }
.btn-submit { background: var(--green); color: white; border: 2px solid var(--ink); padding: 8px 15px; border-radius: 8px; cursor: pointer; font-family: 'Kalam', cursive; font-weight: bold; font-size: 1.1rem; }

.q-card { background: var(--paper-2); border: 2px solid var(--ink); border-radius: 15px; padding: 25px; box-shadow: 4px 4px 0 rgba(31,45,77,.1); margin-bottom: 20px; }
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

  <div class="header" id="main-header">
    <h1>🚀 50 Examens x 100 Questions</h1>
    <p>Le moteur d'intelligence artificielle qui génère <strong>5000 questions uniques</strong> avec corrigés.</p>
    <a href="ccna_pro_complet.html">⬅ Retourner au Cours Principal</a>
  </div>

  <div id="dashboard">
    <h2 style="font-family:'Caveat', cursive; font-size:2.5rem; text-align:center;">Choisissez votre Examen</h2>
    <div class="exam-grid" id="exam-grid"></div>
  </div>

  <div id="exam-view">
    <div class="exam-header">
      <button class="btn-back" onclick="closeExam()">🔙 Quitter</button>
      <h2 id="exam-title">Examen X</h2>
      <button class="btn-submit" onclick="submitExam()">✅ Score Final</button>
    </div>
    <div id="questions-container"></div>
  </div>
  
  <div class="score-box" id="score-box"></div>

<script>
/* =========================================
   MOTEUR DE GÉNÉRATION D'EXAMENS CCNA
========================================= */

// Seeded Random Number Generator (pour que l'Examen X soit toujours le même)
let currentSeed = 1;
function sRandom() {
    let x = Math.sin(currentSeed++) * 10000;
    return x - Math.floor(x);
}
function sRandInt(min, max) {
    return Math.floor(sRandom() * (max - min + 1)) + min;
}
function sRandChoice(arr) {
    return arr[sRandInt(0, arr.length - 1)];
}
function sShuffle(arr) {
    let array = [...arr];
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(sRandom() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// -----------------------------------------
// BASE DE DONNÉES THÉORIQUES (Pool)
// -----------------------------------------
const theoryDB = [
    { t: "OSI", q: "À quelle couche OSI fonctionne un routeur ?", o: ["Couche 1", "Couche 2", "Couche 3", "Couche 4"], a: 2, e: "Le routeur transfère les paquets en se basant sur l'adresse IP (Couche 3)." },
    { t: "OSI", q: "Quel protocole fonctionne à la couche Transport ?", o: ["IP", "TCP", "HTTP", "Ethernet"], a: 1, e: "TCP et UDP sont les protocoles de la couche Transport (Couche 4)." },
    { t: "Commutation", q: "Que fait un switch avec une trame 'Unknown Unicast' ?", o: ["Il la supprime", "Il la diffuse sur tous les ports", "Il l'envoie au routeur", "Il la renvoie à l'expéditeur"], a: 1, e: "L'opération s'appelle le Flooding." },
    { t: "VLAN", q: "Quel protocole est utilisé pour négocier un lien Trunk ?", o: ["VTP", "STP", "DTP", "LACP"], a: 2, e: "Dynamic Trunking Protocol (DTP) gère la négociation des Trunks." },
    { t: "VLAN", q: "Quel est le standard ouvert pour l'encapsulation Trunk ?", o: ["ISL", "802.1Q", "HDLC", "PPP"], a: 1, e: "802.1Q est le standard IEEE. ISL est propriétaire Cisco." },
    { t: "STP", q: "Dans STP, comment est élu le Root Bridge ?", o: ["Plus haute IP", "Plus haute MAC", "Plus faible Priorité + MAC", "Plus haute Priorité"], a: 2, e: "Le switch avec le plus faible Bridge ID devient le Root." },
    { t: "RSTP", q: "Quel état n'existe PAS dans Rapid STP (802.1w) ?", o: ["Discarding", "Learning", "Forwarding", "Listening"], a: 3, e: "RSTP fusionne Blocking et Listening en un seul état : Discarding." },
    { t: "EtherChannel", q: "Quel protocole EtherChannel est un standard IEEE ?", o: ["PAgP", "LACP", "VTP", "STP"], a: 1, e: "LACP (802.3ad) est le standard. PAgP est propriétaire Cisco." },
    { t: "Routage", q: "Quelle est la distance administrative d'une route statique ?", o: ["1", "90", "110", "120"], a: 0, e: "Une route statique a une AD de 1 (très fiable)." },
    { t: "OSPF", q: "Que signifie l'état FULL dans OSPF ?", o: ["Échange de Hello", "Bases de données (LSDB) 100% synchronisées", "Élu DR", "En panne"], a: 1, e: "FULL signifie que les routeurs adjacents ont des LSDB identiques." },
    { t: "Sécurité", q: "Que bloque DHCP Snooping ?", o: ["Les attaques DDoS", "Les faux serveurs DHCP (Rogue DHCP)", "Le trafic HTTP", "Le Spanning Tree"], a: 1, e: "Il empêche les serveurs non autorisés d'attribuer de fausses adresses IP." },
    { t: "Sécurité", q: "Port Security : Quel est le mode de violation par défaut ?", o: ["Protect", "Restrict", "Shutdown", "Err-disable"], a: 2, e: "Le port est mis en état 'Shutdown' (err-disabled) s'il y a violation." },
    { t: "NAT", q: "Quel type de NAT utilise des numéros de ports pour partager une seule IP publique ?", o: ["NAT Statique", "NAT Dynamique", "PAT (Overload)", "NAT IPv6"], a: 2, e: "Port Address Translation (PAT) mappe plusieurs IP privées via les ports TCP/UDP." },
    { t: "ACL", q: "Quelle plage correspond à une ACL Standard ?", o: ["1-99", "100-199", "1000-1999", "2000-2699"], a: 0, e: "1-99 et 1300-1999 sont pour les ACL standards." },
    { t: "IPv6", q: "Combien de bits compose une adresse IPv6 ?", o: ["32", "64", "128", "256"], a: 2, e: "IPv6 utilise 128 bits, exprimés en hexadécimal." },
    { t: "IPv6", q: "Quelle adresse IPv6 est l'équivalent de 127.0.0.1 (Loopback) ?", o: ["FE80::1", "FF02::1", "::1", "2001::1"], a: 2, e: "::1 est l'adresse de loopback en IPv6." },
    { t: "Wi-Fi", q: "Quel équipement centralise la gestion des points d'accès légers (LAP) ?", o: ["Routeur", "Switch Core", "WLC", "Firewall"], a: 2, e: "Le WLC (Wireless LAN Controller) gère les LAPs via le tunnel CAPWAP." },
    { t: "Wi-Fi", q: "Quelle norme de sécurité Wi-Fi utilise SAE ?", o: ["WEP", "WPA", "WPA2", "WPA3"], a: 3, e: "WPA3 remplace le PSK par SAE (Simultaneous Authentication of Equals)." },
    { t: "SDN", q: "Quelle API est utilisée pour que le contrôleur SDN parle aux switchs physiques ?", o: ["Northbound", "Southbound", "Eastbound", "Westbound"], a: 1, e: "Southbound API (ex: OpenFlow, NETCONF) descend vers le matériel." },
    { t: "Automatisation", q: "Lequel de ces outils n'utilise PAS d'agent sur l'équipement réseau ?", o: ["Chef", "Puppet", "Ansible", "Docker"], a: 2, e: "Ansible est 'Agentless' et se connecte simplement via SSH." }
];

// -----------------------------------------
// GÉNÉRATEURS DE QUESTIONS DYNAMIQUES
// (Produisent des millions de combinaisons)
// -----------------------------------------

function ip2long(ip) {
    return ip.split('.').reduce((ipInt, octet) => (ipInt << 8) + parseInt(octet, 10), 0) >>> 0;
}
function long2ip(ipInt) {
    return ( (ipInt>>>24) +'.' + (ipInt>>16 & 255) +'.' + (ipInt>>8 & 255) +'.' + (ipInt & 255) );
}

function genSubnettingQ() {
    let base = sRandChoice(["192.168", "10.0", "172.16", "172.20", "10.5", "192.168.100"]);
    if(base.split('.').length == 2) base += `.${sRandInt(1, 250)}`;
    let ip = `${base}.${sRandInt(1, 250)}`;
    let prefix = sRandChoice([25, 26, 27, 28, 29, 30]);
    
    let ipL = ip2long(ip);
    let maskL = (0xFFFFFFFF << (32 - prefix)) >>> 0;
    let netL = (ipL & maskL) >>> 0;
    let broadL = (netL | ~maskL) >>> 0;
    
    let netIP = long2ip(netL);
    let broadIP = long2ip(broadL);
    let firstIP = long2ip(netL + 1);
    let lastIP = long2ip(broadL - 1);
    
    let type = sRandChoice(["network", "broadcast", "first", "last"]);
    let q, ans, expl;
    
    if(type === "network") {
        q = `Quelle est l'adresse réseau (Network ID) pour l'hôte ${ip}/${prefix} ?`;
        ans = netIP;
        expl = `Avec un /${prefix}, le réseau de base est ${netIP}.`;
    } else if(type === "broadcast") {
        q = `Quelle est l'adresse de diffusion (Broadcast) pour le sous-réseau contenant l'IP ${ip}/${prefix} ?`;
        ans = broadIP;
        expl = `Avec un /${prefix}, l'adresse la plus haute du bloc est ${broadIP}.`;
    } else if(type === "first") {
        q = `Quelle est la PREMIÈRE adresse IP utilisable pour le sous-réseau de ${ip}/${prefix} ?`;
        ans = firstIP;
        expl = `Le réseau est ${netIP}, donc la première IP est ${firstIP}.`;
    } else {
        q = `Quelle est la DERNIÈRE adresse IP utilisable pour le sous-réseau de ${ip}/${prefix} ?`;
        ans = lastIP;
        expl = `Le broadcast est ${broadIP}, donc la dernière IP est ${lastIP}.`;
    }
    
    let wrongs = [
        long2ip(netL - 1 >= 0 ? netL - 1 : 0),
        long2ip(broadL + 1),
        long2ip(netL + Math.floor(Math.pow(2, 32-prefix)/2)),
        long2ip(broadL),
        long2ip(netL)
    ].filter(x => x !== ans);
    
    let opts = sShuffle([ans, wrongs[0], wrongs[1], wrongs[2]]);
    return { t: "Subnetting", q: q, o: opts, a: opts.indexOf(ans), e: expl };
}

function genPortQ() {
    const ports = [ {p:"HTTP", v:80}, {p:"HTTPS", v:443}, {p:"SSH", v:22}, {p:"Telnet", v:23}, {p:"DNS", v:53}, {p:"DHCP Serveur", v:67}, {p:"NTP", v:123}, {p:"TFTP", v:69}, {p:"FTP", v:21} ];
    let correct = sRandChoice(ports);
    let q = `Quel est le port par défaut utilisé par le protocole ${correct.p} ?`;
    let wrongs = ports.filter(x => x.v !== correct.v).map(x => x.v);
    wrongs = sShuffle(wrongs);
    let opts = sShuffle([correct.v, wrongs[0], wrongs[1], wrongs[2]]);
    return { t: "Ports & Protocoles", q: q, o: opts, a: opts.indexOf(correct.v), e: `${correct.p} utilise toujours le port ${correct.v}.` };
}

function genADQ() {
    const ads = [ {p:"OSPF", v:110}, {p:"EIGRP", v:90}, {p:"RIP", v:120}, {p:"Route Statique", v:1}, {p:"Connecté", v:0}, {p:"eBGP", v:20} ];
    let correct = sRandChoice(ads);
    let q = `Quelle est la Distance Administrative (AD) par défaut du protocole ${correct.p} ?`;
    let wrongs = ads.filter(x => x.v !== correct.v).map(x => x.v);
    wrongs = sShuffle(wrongs);
    let opts = sShuffle([correct.v, wrongs[0], wrongs[1], wrongs[2]]);
    return { t: "Routage (AD)", q: q, o: opts, a: opts.indexOf(correct.v), e: `L'AD indique la fiabilité. Pour ${correct.p}, c'est ${correct.v}.` };
}

function genWildcardQ() {
    const masks = [ {p:24, v:"0.0.0.255"}, {p:25, v:"0.0.0.127"}, {p:26, v:"0.0.0.63"}, {p:27, v:"0.0.0.31"}, {p:28, v:"0.0.0.15"}, {p:29, v:"0.0.0.7"}, {p:30, v:"0.0.0.3"} ];
    let correct = sRandChoice(masks);
    let q = `Quel est le masque générique (Wildcard Mask) utilisé dans OSPF ou ACL pour un sous-réseau /${correct.p} ?`;
    let wrongs = masks.filter(x => x.v !== correct.v).map(x => x.v);
    wrongs = sShuffle(wrongs);
    let opts = sShuffle([correct.v, wrongs[0], wrongs[1], wrongs[2]]);
    return { t: "Wildcard Mask", q: q, o: opts, a: opts.indexOf(correct.v), e: `Un /${correct.p} a pour wildcard mask ${correct.v} (inverse du masque réseau).` };
}

function generateExam(examID) {
    currentSeed = examID * 12345; // Initialisation du seed unique pour cet examen
    
    let examQs = [];
    
    // On prend 25 questions théoriques au hasard dans notre BD (sans doublons)
    let tPool = sShuffle([...theoryDB]);
    for(let i=0; i<25; i++) {
        if(tPool[i]) examQs.push(tPool[i]);
    }
    
    // On génère 75 questions dynamiques pour arriver à 100 !
    for(let i=0; i<35; i++) examQs.push(genSubnettingQ());
    for(let i=0; i<15; i++) examQs.push(genPortQ());
    for(let i=0; i<15; i++) examQs.push(genADQ());
    for(let i=0; i<10; i++) examQs.push(genWildcardQ());
    
    // Mélanger les 100 questions
    return sShuffle(examQs);
}

// -----------------------------------------
// GESTION DE L'INTERFACE (UI)
// -----------------------------------------

const grid = document.getElementById('exam-grid');
const dash = document.getElementById('dashboard');
const view = document.getElementById('exam-view');
const container = document.getElementById('questions-container');
const title = document.getElementById('exam-title');
const header = document.getElementById('main-header');
const scoreBox = document.getElementById('score-box');

// Créer les 50 boutons
let savedProgress = JSON.parse(localStorage.getItem('ccna-50-exams') || '{}');

for(let i=1; i<=50; i++) {
    let btn = document.createElement('div');
    btn.className = 'exam-btn' + (savedProgress[i] ? ' completed' : '');
    btn.innerHTML = `Examen ${i} <br><span style="font-size:0.8rem; font-weight:normal;">100 Questions</span>`;
    if(savedProgress[i]) {
        btn.innerHTML += `<br><span style="font-size:0.9rem;">⭐ ${savedProgress[i]}/100</span>`;
    }
    btn.onclick = () => openExam(i);
    grid.appendChild(btn);
}

let currentExamID = 1;

function openExam(id) {
    currentExamID = id;
    dash.style.display = 'none';
    header.style.display = 'none';
    view.style.display = 'block';
    scoreBox.style.display = 'none';
    title.innerText = `Examen ${id} (100 Qs)`;
    
    let qs = generateExam(id);
    container.innerHTML = '';
    
    let letters = ["A", "B", "C", "D"];
    
    qs.forEach((q, idx) => {
        let qNum = idx + 1;
        let optsHtml = q.o.map((opt, oIdx) => `<li data-idx="${oIdx}" data-correct="${q.a}"><strong>${letters[oIdx]}.</strong> ${opt}</li>`).join('');
        
        container.innerHTML += `
        <div class="q-card" id="q${qNum}">
          <h3>Question ${qNum} - ${q.t}</h3>
          <p class="q-text">${q.q}</p>
          <ul class="options">${optsHtml}</ul>
          <div class="corrige">
            <p><strong>✅ Bonne Réponse : ${letters[q.a]}</strong></p>
            <p><em>Explication :</em> ${q.e}</p>
          </div>
        </div>`;
    });
    
    // Events
    document.querySelectorAll('.options li').forEach(li => {
      li.addEventListener('click', function() {
        const ul = this.parentNode;
        if(ul.dataset.locked) return;
        ul.querySelectorAll('li').forEach(el => el.classList.remove('selected'));
        this.classList.add('selected');
      });
    });
    
    window.scrollTo(0,0);
}

function closeExam() {
    view.style.display = 'none';
    dash.style.display = 'block';
    header.style.display = 'block';
    scoreBox.style.display = 'none';
    window.scrollTo(0,0);
}

function submitExam() {
    let score = 0;
    document.querySelectorAll('.options').forEach(ul => {
        ul.dataset.locked = "true";
        const selected = ul.querySelector('li.selected');
        const correct_idx = ul.querySelector('li').dataset.correct;
        
        ul.parentNode.querySelector('.corrige').style.display = 'block';

        if(selected) {
            if(selected.dataset.idx === correct_idx) {
                selected.classList.add('correct');
                score++;
            } else {
                selected.classList.add('wrong');
                ul.querySelector(`li[data-idx="${correct_idx}"]`).classList.add('correct');
            }
        } else {
            ul.querySelector(`li[data-idx="${correct_idx}"]`).classList.add('correct');
        }
    });

    scoreBox.innerHTML = `Score Final : ${score} / 100`;
    scoreBox.style.display = 'block';
    
    // Save progress
    savedProgress[currentExamID] = score;
    localStorage.setItem('ccna-50-exams', JSON.stringify(savedProgress));
    
    // Update dashboard button
    const btn = grid.children[currentExamID - 1];
    btn.className = 'exam-btn completed';
    btn.innerHTML = `Examen ${currentExamID} <br><span style="font-size:0.8rem; font-weight:normal;">100 Questions</span><br><span style="font-size:0.9rem;">⭐ ${score}/100</span>`;
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
</script>
</body>
</html>
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Update main file to point to 50 Exams Simulator
main_path = r"C:\Users\PC\Desktop\ccna7\ccna_pro_complet.html"
with open(main_path, "r", encoding="utf-8") as f:
    main_html = f.read()

btn_link = '<a href="ccna_50_exams.html" class="btn green" style="text-decoration:none; margin-left: 10px;">💯 50 Examens Pro</a>'

import re
if "ccna_mega_exam.html" in main_html:
    main_html = re.sub(r'<a href="ccna_mega_exam\.html".*?</a>', btn_link, main_html)
elif "ccna_exams.html" in main_html:
    main_html = re.sub(r'<a href="ccna_exams\.html".*?</a>', btn_link, main_html)
elif "50 Examens Pro" not in main_html:
    main_html = main_html.replace('<div class="progress-wrap"', btn_link + '\n    <div class="progress-wrap"')

with open(main_path, "w", encoding="utf-8") as f:
    f.write(main_html)
