import time
import random
import os

# Étapes logiques du faux système scolaire
etapes = [
    "Initialisation du système scolaire...",
    "Connexion au réseau pédagogique...",
    "Chargement du module : Professeur Emanuel...",
    "Analyse du discours en cours...",
    "Tentative de compréhension du contenu...",
    "Évaluation de l'attention des élèves...",
    "Recherche de motivation...",
    "Exécution de la commande : 'Rester éveillé'...",
    "Compilation des informations utiles...",
    "Détection de signaux de vie dans la classe...",
    "Simulation d'intérêt en cours...",
    "Préparation du mini-jeu de survie...",
]

messages_par_etape = [
    "Système scolaire détecté : ClasseOS v1.3",
    "Connexion au cerveau... [Timeout]",
    "Chargement de la voix d’Emanuel... [Volume : 120%, Clarté : 3%]",
    "Analyse du discours d’Emanuel... [Trop de mots détectés]",
    "Tentative de compréhension... [Erreur 404 : logique non trouvée]",
    "Synchronisation avec l’attention de la classe... [Déconnexion automatique]",
    "Chargement de la motivation... [Échec critique - fichier corrompu]",
    "Exécution de la commande : 'Faire semblant d’écouter'... [Succès partiel, yeux ouverts]",
    "Compression du contenu utile... [0.0001% extrait]",
    "Recherche de signes vitaux... [Un soupir détecté au fond de la classe]",
    "Affichage du sourire poli... [Processus bloqué]",
    "Chargement du mini-jeu : 'Survivre à Emanuel.exe'",
]

bonus_messages = [
    "Téléchargement de la pause... [Interdite jusqu'à nouvel ordre]",
    "Activation du mode survie... [Café non détecté]",
    "Tentative de fuite mentale... [Mur de briques]",
    "Lancement de l'application 'Regarder l'horloge'... [Temps ralenti]",
    "Connexion à l'univers parallèle... [Refusée par le système scolaire]",
    "Mise à jour du prof... [Version 1997 toujours active]",
    "Détection de bug : Trop de syllabes dans une seule phrase",
    "Erreur critique : Emanuel a commencé une digression dans une digression",
]

# Mini-jeu 1 : quiz absurde
def mini_jeu_survie():
    print("\n=== Mini-jeu : Survivre à Emanuel.exe ===")
    questions = [
        {
            "question": "Emanuel commence une phrase par 'Donc, en résumé...' Que fais-tu ?",
            "options": ["A. Tu prends des notes", "B. Tu t’endors", "C. Tu cries intérieurement", "D. Tu redémarres ton cerveau"],
            "answer": "C"
        },
        {
            "question": "Combien de temps faut-il à Emanuel pour expliquer un mot simple ?",
            "options": ["A. 10 secondes", "B. 1 minute", "C. 3 heures", "D. Le reste de ta vie"],
            "answer": "D"
        },
        {
            "question": "Quel est le meilleur camouflage pour ne pas être interrogé ?",
            "options": ["A. Regarder le tableau", "B. Faire semblant d’écrire", "C. Fusionner avec ta chaise", "D. Disparaître dans une autre dimension"],
            "answer": "C"
        }
    ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        reponse = input("Ta réponse (A/B/C/D) : ").strip().upper()
        if reponse == q["answer"]:
            print("✔ Bonne réponse !")
            score += 1
        else:
            print("✘ Mauvaise réponse... mais qui aurait survécu de toute façon ?")

    print(f"\n>>> Résultat : {score}/3 bonnes réponses.")
    if score == 3:
        print("🎉 Tu as survécu à Emanuel ! Félicitations, héros de la classe.")
    else:
        print("💤 Tu t’es évanoui d’ennui. Redémarrage en cours...")

# Mini-jeu 2 : devine ce que veut dire Emanuel
def mini_jeu_traduction():
    print("\n=== Mini-jeu bonus : Traduction Emanuel → Français ===")
    phrase = "« Si on fait un if ici ... »"
    print(f"\nEmanuel dit : {phrase}")
    input("Appuie sur Entrée pour tenter une traduction...")
    print("Traduction : « On va parler d’un truc simple, mais je vais le rendre incompréhensible. »")
    print("✔ Traduction approximative réussie !")

# Fonction principale
def fake_class_system():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== 🎬 Démarrage de ClasseOS v1.3 - Mode Emanuel Activé ===\n")
    print("⚠️ Attention : ce système peut provoquer des effets secondaires tels que bâillements, perte de volonté et fuites mentales.\n")
    time.sleep(2)

    for etape, message in zip(etapes, messages_par_etape):
        print(f"> {etape}")
        time.sleep(0.8)
        print(f"  {message}\n")
        time.sleep(1)

    # Messages bonus
    print("=== Messages système additionnels ===\n")
    for _ in range(4):
        print(f"> {random.choice(bonus_messages)}")
        time.sleep(1)

    # Mini-jeux
    mini_jeu_survie()
    mini_jeu_traduction()

    # Écran bleu final
    print("\n💻 === ERREUR FATALE ===")
    print("Code : 0xE-M-A-N-U-E-L")
    print("Description : Trop de discours détecté. Le système a cessé de répondre.")
    print("Solution : Fermer les yeux et espérer que la cloche sonne.")
    print("\n🔁 Redémarrage en mode coma scolaire...\n")

# Lancer le programme
fake_class_system()