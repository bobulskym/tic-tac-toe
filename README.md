# Tic-Tac-Toe AI 🎮🤖

This project implements a Tic-Tac-Toe game with an AI opponent using **Reinforcement Learning (Q-Learning)**. The game is visualized using **Pygame**, allowing a human player to compete against a trained AI.

## 📌 Features
- AI learns using **Q-Learning** and gets better over time.
- The game is displayed in a **Pygame window** for an interactive experience.
- **Randomized starting player**: Each time you play, either you or the AI will move first.
- Two separate game modes:
  - `player_starts.py`: The human player moves first.
  - `ai_starts.py`: The AI makes the first move.
- `main.py` randomly selects one of the two modes.

---

## 🛠 Installation & Setup

### 1️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required dependencies:

```bash
pip install pygame
```

### 2️⃣ Run the Game
To play, simply run:

```bash
python main.py
```

The script will randomly decide whether **you or the AI will move first**.

---

## 🏆 How It Works
### 1. **AI Training**
- The AI learns optimal moves using **Q-Learning**.
- It updates a **Q-table** that stores the best actions for each game state.
- Over **100,000+ training games**, the AI improves its strategy.

### 2. **Game Logic**
- The **human player (O)** plays against the **AI (X)**.
- The game board updates in real-time using Pygame.
- If the game ends (win, lose, or draw), the winner is displayed on the screen.

---

## 🎮 Controls
- Click on a square to make your move.
- The AI will play automatically after your turn.
- The game will show the winner when it ends.

---

## 📂 File Structure
```
📂 TicTacToe-AI
│── main.py          # Randomly chooses player_starts.py or ai_starts.py
│── player_starts.py # Human starts first
│── ai_starts.py     # AI starts first
│── README.txt       # Project description
```

---

## ⚡ Future Improvements
- Add **sound effects** when making a move.
- Implement a **restart button** instead of exiting after a game ends.
- Enhance AI with **Deep Q-Learning** for smarter gameplay.

---

## 🤝 Contributing
Feel free to **fork** this project and submit pull requests with improvements!

---

## 📜 License
This project is open-source and free to use. 🚀
