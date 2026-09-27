# 🌌 Spacy - 2D Space Arcade Game

A fast-paced, interactive 2D arcade game built entirely in Python using the PyGame framework. Dodge chaotic asteroid fields, navigate past scrolling deep-space planetary bodies, and survive as long as you can to rack up your score!

This project was built from scratch as part of a coding milestone to track engineering hours for the **Stardance** competition.

---

## 🚀 Project Tracking Metrics
* **Total Tracked Hours:** 14 Hours, 56 Minutes
* **Time Tracker Tool:** VS Code HackTime Extension
* **Target Objective:** MacBook Air 13" Achievement Bracket

---

## 🛸 Game Features
* **Dynamic Physics Engine:** Implements multi-entity bounding box collision routines to handle bouncing physics between multiple moving asteroids.
* **Procedural Environments:** Features a parallax background layer alongside automated random scaling and placement loops for solar system planets (Earth, Mars, Jupiter, Venus, etc.).
* **Advanced Game Loop:** Runs a stable frame-rate clock cycle separating user input event registers from screen asset rendering pipelines.
* **Sci-Fi Audio Design:** Integrated audio mixing boards to handle concurrent background space soundtracks and tactical impact sound effects.

---

## 📁 Repository Structure
```text
Spacy/
│
├── Spacy.py              # Core Python game executable script
├── README.md             # Project documentation & layout manual
│
├── Spacy/images/         # Graphic assets (Spaceship, asteroid textures)
└── Spacy/sounds/         # Audio assets (Background score, impact FX)
```

---

## 🛠️ Installation & Local Setup

To play the game locally on your computer, ensure you have Python 3 installed, then follow these simple steps:

1. **Clone or Download the Repository:**
   Download this project directory to your local drive.

2. **Install the Required Libraries:**
   Open your terminal/command prompt inside the folder and install PyGame:
   ```bash
   pip install pygame
   ```

3. **Launch the Game:**
   Run the primary script file via Python:
   ```bash
   python Spacy.py
   ```

---

## 🧠 Core Engineering Principles Learned
* Managing complex nested state evaluation cycles inside infinite structural program loops.
* Implementing vector velocity calculations (`vx`, `vy`) to translate screen coordinates dynamically over time.
* Reading and troubleshooting comprehensive Python traceback errors to isolate system environment bottlenecks.
