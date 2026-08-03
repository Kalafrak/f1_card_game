# Apex Legacy

A Top Trumps-inspired card battling game featuring Formula 1 drivers.

## About

Pit your driver's strongest attribute against your opponent's over 10 rounds
and try to stay ahead in the race for the championship. Each round, draw a
driver card and choose a stat — talent, longevity, aggression, moxie,
humour, or scrupulousness — to battle against the CPU's card. Whoever has
the higher value wins the round. Highest score after 10 rounds takes the
championship!

## How to Play

1. Run the game (see below).
2. Follow the prompts to confirm you're ready to race.
3. Each round, you'll see your driver's card and stats.
4. Choose which stat to compare against the CPU's card using the
   two-letter shorthand (ta/lo/ag/mo/hu/sc).
5. See the result, and track the running score.
6. After 10 rounds, the player with the highest score wins the
   championship!
7. Type 'quit' at any time to exit early.

## Requirements

- Python 3.x

## Installation and Setup

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Kalafrak/apex-legacy.git
   cd f1_card_game
   \`\`\`

2. Create and activate a virtual environment:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Running the Game

\`\`\`bash
python main.py
\`\`\`

## Running Tests

\`\`\`bash
pytest
\`\`\`

## Project Structure

- \`main.py\` — entry point, sets up the deck and starts the game
- \`game_loop.py\` — core game logic and round loop
- \`display.py\` — handles all printed output and pacing
- \`deck.py\` — the Deck class (shuffling, drawing cards)
- \`driver_class.py\` — the Driver class and JSON loading logic
- \`drivers.json\` — driver data (name and stats)
- \`test_*.py\` — unit tests for game logic