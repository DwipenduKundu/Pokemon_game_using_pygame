# Pokemon Game

A two-player Pygame where **Pikachu** and **Meowth** compete to collect Pokeballs. First to reach 20 points wins!

## 🎮 Gameplay

- **Player 1 (Pikachu)**:
  - Controls: Arrow Keys **(← ↑ ↓ →)**

- **Player 2 (Meowth)**:
  - Controls: **W A S D**

- Collect the Pokéball that appears at random positions on the screen.
- First player to collect **20 Pokeballs** wins.

## Files:

Make sure you have the following assets in the correct directory:
```
project/
├── game.py
├── player_pics/
│ ├── pikachu.png
│ ├── avatar.png (Meowth)
│ └── POKEBALL.png
└── music/
└── pokemon_go.mp3

```

Update the image and music file paths in the code if necessary.

## ▶️ How to Run

#### 1. Clone the repository


```bash
git clone git@github.com:DwipenduKundu/Pokemon_game_using_pygame.git
cd company-master-data_analysis
```

#### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
#linux
source venv/bin/activate     
# On Windows: venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```


#### 4. Run the script

```bash
pip install pygame
python 2_player_game.py.py
```
------------------

### Features
- Smooth movement and real-time collision detection
- Background music
- Real-time score display
- Victory message with delay before exit

### Winner Logic
- The game ends when any player collects 20 Pokéballs.
- A victory message is displayed for 3 seconds before closing.

**Enjoy the Pokemon action!** # Pokemon_game_using_pygame
