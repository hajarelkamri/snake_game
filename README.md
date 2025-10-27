# Reinforcement Learning Maze Solver

Ce projet implémente deux algorithmes d'apprentissage par renforcement - **Q-learning** et **SARSA** - pour résoudre un problème de navigation dans un labyrinthe. L'agent apprend à atteindre un objectif tout en évitant les obstacles grâce à l'exploration et l'exploitation de l'environnement.

##  Fonctionnalités

- **Implémentation de Q-learning** : Apprentissage hors politique (off-policy)
- **Implémentation de SARSA** : Apprentissage sur politique (on-policy) 
- **Environnement graphique interactif** : Visualisation en temps réel de l'apprentissage
- **Table Q dynamique** : Génération automatique des états
- **Métriques de performance** : Visualisation des steps et coûts par épisode
- **Comparaison d'algorithmes** : Possibilité de comparer les performances entre Q-learning et SARSA

# Utilisation
 # Exécuter Q-learning: 
  python main_Q-learning.py
 # Exécuter SARSA :
  python main.py
# Algorithmes Implémentés
  # Q-learning
  Type : Off-policy
  
  Mise à jour : Utilise la meilleure action future possible
  
  Formule : Q(s,a) = Q(s,a) + α[r + γmaxQ(s',a') - Q(s,a)]
  
  # SARSA
  Type : On-policy
  
  Mise à jour : Utilise l'action réellement choisie
  
  Formule : Q(s,a) = Q(s,a) + α[r + γQ(s',a') - Q(s,a)]

# Résultats et Visualisation
  Le projet génère plusieurs graphiques pour analyser les performances :
  
  Épisodes vs Steps : Nombre de steps nécessaires pour atteindre l'objectif
  
  Épisodes vs Coût : Coût cumulé pendant l'apprentissage
  
  Table Q finale : Valeurs apprises pour les états optimaux

 # Paramètres Configurables
  # Paramètres d'apprentissage
    learning_rate (α) : Taux d'apprentissage (0.01-1.0)
    
    reward_decay (γ) : Facteur d'atténuation (0.9)
    
    e_greedy (ε) : Probabilité d'exploration (0.9)

 # Paramètres d'exécution
  episodes : Nombre d'épisodes d'entraînement
  
  actions : Actions disponibles dans l'environnement

  # Analyse des Performances
  Q-learning : Converge généralement plus vite vers une politique optimale
  
  SARSA : Plus prudent, évite les zones dangereuses lors de l'exploration
  
  Comparaison : Les deux algorithmes montrent des performances similaires mais avec des caractéristiques d'exploration différentes
