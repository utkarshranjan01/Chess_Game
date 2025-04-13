# Chess Royale: A Python Chess Game with Online and Offline Play

Chess Royale is a sophisticated Python-based chess game built with the Pygame library that offers both offline and online multiplayer experiences. The game features an intuitive drag-and-drop interface, comprehensive chess rules implementation, and a resilient networking system that delivers smooth gameplay even with limited bandwidth.

---

![Front Screen](Screenshots/Screenshot%202024-03-01%20at%205.54.57%20PM.jpg)  
![Game Demo](Screenshots/demo.mp4)

---

## Key Features

- Offline Mode:
  Challenge a friend locally on the same computer with full chess functionality.

- Online Multiplayer:
  Connect with players worldwide through a robust TCP-based networking system featuring connection reliability mechanisms.

- Intuitive Chess Interface:
  Enjoy familiar click and drag-and-drop controls reminiscent of popular chess platforms.

- Complete Chess Rules Implementation:
  - Legal move validation with piece-specific movement patterns
  - Special moves including castling and en passant
  - Pawn promotion to queen, rook, bishop, or knight
  - Draw conditions including 50-move rule and threefold repetition
  - Check and checkmate detection
  - Stalemate recognition



## Technical Architecture

 - **Frontend**: Pygame provides responsive graphics rendering and user interaction handling
 - **Game Logic**: Comprehensive chess rule engine with move validation and game state management
 - **Networking**: Custom-built client-server architecture using Python's socket library
 - **Performance**: Multi-threaded design ensures smooth gameplay while handling network communications
 - **Reliability**: Heartbeat protocol maintains connection integrity and gracefully handles disconnections

## Technologies Used

- **Python**: Core programming language
- **Pygame**: Graphics rendering, animation, and input processing
- **Socket** Programming: Real-time network communication between clients and server
- **Threading**: Asynchronous I/O management to prevent UI freezing during network operations
- **Design Patterns**: State pattern for game phases, Observer pattern for event handling

## Installation

Clone the repository and install the dependencies:

```bash
git clone <your-repository-url>
cd <your-project-directory>
pip install pygame socket
```

## Launch the game

Starting the Game: Run python main.py to launch Chess Royale
Game Mode Selection: Choose between offline or online play from the main menu
Online Play: Host a game or join an existing session (change IP address from constants.py file)
Controls: Click a piece to select, then click a destination square or simply drag and drop


## License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments