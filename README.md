![Pygame GIthub](https://user-images.githubusercontent.com/64391274/229285417-80d68655-4282-4a33-87a2-20723c8dfcb0.png)



# Project Name
ESCAPE!!

The program is a simple Pygame game in which the player character must avoid enemy characters to stay alive. The game window displays a score and the number of lives remaining.

The player character is represented as a rectangle that can be moved horizontally and vertically using the arrow keys or WASD keys. The enemies are also represented as rectangles that move across the screen at a constant speed.

The game loop updates the positions of the player character and the enemies on the screen and checks for collisions between them. If the player character collides with an enemy, the player loses a life and the character's position is reset to the center of the screen.

The game ends when the player loses all their lives. When the game ends, a "Game Over" message is displayed on the screen for 5 seconds before quitting the game.

The program uses Pygame to handle the game loop, graphics, and user input. The game score and lives are displayed on the screen using text objects. The program also uses sound effects to indicate when the player loses a life or collides with an enemy.
## Team members
1. Vishal Unni [https://github.com/VISHALUNNI]
2. Adithya S Prabhu [https://github.com/TectonicSteak]
3. Alaka A J [https://github.com/alaka03aj]
## Link to product walkthrough
[Walkthrough](https://www.loom.com/share/1ad1cd92a5aa4cabbf18b4cecf05ad79)
## How it Works ?
1. The blob has the ability to move left and right. The goal is to not get in contact with the spikes that has the power to reduce it's health. The blob has 3 lives. The game stops when it runs out of life. It has a total of 5 levels and the game ends when you hit a score of 30 (ie, you survived till the end!).
2. [Walkthrough](https://www.loom.com/share/1ad1cd92a5aa4cabbf18b4cecf05ad79)
## Libraries used
pygame - 2.3.0
## How to configure
Instructions for setting up project
1. Fork the repository
2. Clone the repository
```
git clone [forked-repo-link]
```
3. Run the program
```
py main.py
```
Note: Python and pygame must be installed to run this game!

## How to Run
```
py main.py
```
## Resources
1. https://canberragpn.github.io/static/doc/PygameCheatSheet.pdf
2. https://realpython.com/pygame-a-primer/
