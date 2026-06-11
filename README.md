# ML Studio 🤖

> Didacticiel interactif d'apprentissage supervisé — Importez vos données, explorez, nettoyez, entraînez et évaluez vos modèles ML en quelques clics.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![React](https://img.shields.io/badge/React-18+-61DAFB)
![Licence](https://img.shields.io/badge/licence-MIT-orange)

---

## Aperçu

ML Studio est une application web pédagogique qui guide l'utilisateur à travers toutes les étapes d'un projet de machine learning supervisé :

1. **Import du dataset** — Upload CSV avec détection automatique des types
2. **EDA** — Statistiques descriptives, distributions, corrélations
3. **Data Cleaning & Feature Selection** — Gestion des NaN, encodage, normalisation
4. **Entraînement** — Plusieurs modèles, hyperparamètres configurables
5. **Évaluation** — Métriques, matrice de confusion, comparaison des modèles

---

## Stack technique

| Couche | Technologie |
|--------|-------------|
| Frontend | React 18, Recharts, Tailwind CSS |
| Backend | Python 3.10+, FastAPI, Uvicorn |
| ML | scikit-learn, pandas, numpy |
| Communication | REST API (JSON) |

---

## Prérequis

- Python 3.10 ou supérieur
- Node.js 18 ou supérieur (LTS recommandé)
- npm 9+

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-username/ml-studio.git
cd ml-studio
```

### 2. Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

pip install fastapi uvicorn pandas scikit-learn python-multipart numpy
```

### 3. Frontend

```bash
cd ../frontend
npm install
```

---

## Lancement

### Backend (port 8000)

```bash
cd backend
venv\Scripts\activate   # Windows
uvicorn main:app --reload
```

API disponible sur : http://localhost:8000
Documentation interactive : http://localhost:8000/docs

### Frontend (port 5173)

```bash
cd frontend
npm run dev
```

Application disponible sur : http://localhost:5173

---

## Structure du projet

```
ml-studio/
├── backend/
│   ├── main.py               # Point d'entrée FastAPI
│   ├── routers/
│   │   └── dataset.py        # Endpoints upload & analyse
│   └── services/
│       └── analyzer.py       # Logique d'analyse des données
│
├── frontend/
│   ├── src/
│   │   ├── components/       # Composants réutilisables
│   │   ├── pages/            # Pages de l'application
│   │   └── api/              # Appels vers le backend
│   └── public/
│
└── README.md
```

---

## Endpoints API

| Méthode | Route | Description |
|---------|-------|-------------|
| `GET` | `/` | Statut de l'API |
| `GET` | `/dataset/ping` | Health check |
| `POST` | `/dataset/upload` | Upload et analyse d'un CSV |

---

## Fonctionnalités v1.0

- [x] Upload CSV (détection auto du séparateur `,` ou `;`)
- [x] Analyse automatique des types de colonnes
- [x] Statistiques descriptives par colonne
- [x] Histogrammes et distribution des variables
- [x] Détection des valeurs manquantes
- [ ] EDA avancée (corrélation, boxplots)
- [ ] Data Cleaning interactif
- [ ] Entraînement multi-modèles
- [ ] Évaluation et comparaison des modèles

---

## Roadmap v2.0

- Support JSON et Excel en import
- Export du modèle entraîné (.pkl)
- Rapport PDF automatique de l'analyse
- Mode régression et classification détectés automatiquement
- Déploiement Docker

---

## Contribuer

Les contributions sont les bienvenues !

1. Fork le projet
2. Crée une branche (`git checkout -b feature/ma-fonctionnalite`)
3. Commit tes changements (`git commit -m 'Ajout de ma fonctionnalité'`)
4. Push la branche (`git push origin feature/ma-fonctionnalite`)
5. Ouvre une Pull Request

---

## Auteur

**Franklin** — [GitHub](https://github.com/franklinlemaire) · [LinkedIn](https://www.linkedin.com/in/franklin-le-maire-kassan-nga-438a132b8)

---

## Licence

Distribué sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
