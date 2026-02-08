#!/usr/bin/env python3
"""Generate Super Bowl Bingo PDFs with seeded random for consistency."""

from weasyprint import HTML, CSS
import random

# Set seed for consistent cards
random.seed(2026)

# Position template: True = HIGH, False = MEDIUM, None = FREE
POSITION_TEMPLATE = [
    [True,  False, True,  False, True ],
    [True,  False, False, False, True ],
    [True,  True,  None,  False, False],
    [False, True,  True,  True,  False],
    [False, True,  False, True,  False]
]

ADULT_HIGH = [
    "Golden Gate Bridge shown on screen",
    "Malcolm Butler interception referenced",
    "Holding penalty called",
    "A catch reviewed for completion",
    "Both teams' 14-3 records mentioned",
    "Announcers compare Maye to young Brady",
    "Shot of Bay Area or SF skyline",
    "Drake Maye scrambles from pocket",
    "Jaxon Smith-Njigba 20+ yard catch",
    "Field goal is kicked",
    "Darnold's 'redemption story' mentioned",
    "A quarterback sack occurs",
    "Budweiser Clydesdale horse in ad",
    "Mike Vrabel shown on sideline",
    "Shane Gillis in Bud Light ad",
    "Bad Bunny performs 'Tití Me Preguntó'",
    "Bad Bunny performs 'Baile Inolvidable'",
    "Someone at party spills a drink",
    "Gatorade shower on winning coach",
    "Green Day shown during pregame",
    "Kenneth Walker III rushing attempt",
    "Aerial/drone shot of Levi's Stadium",
    "Touchdown celebration dance",
    "Split screen of both coaches",
    "Patriots dynasty era mentioned",
    "First down measurement shown",
    "Crowd shot with face paint",
    "Announcers explain a rule to viewers",
    "Slow-motion replay of a big hit",
    "Ref makes dramatic hand signal",
    "Tom Brady shown at the game",
    "Post Malone in Bud Light ad",
    "Cardi B shown cheering for Diggs",
    "Player does 'first down' point",
    "Commercial uses a classic rock song"
]

ADULT_MEDIUM = [
    "A turnover (INT or fumble)",
    "Sam Darnold throws an interception",
    "Drake Maye runs for a first down",
    "A trick play is called",
    "Score tied at halftime",
    "Blocked punt or field goal",
    "Emma Stone in a commercial",
    "Sabrina Carpenter in a commercial",
    "'He Gets Us' religious ad airs",
    "Matthew McConaughey in a commercial",
    "Coin toss is TAILS",
    "A commercial makes you emotional",
    "Kelce brothers (Travis or Jason) spotted",
    "Tech CEO spotted in crowd",
    "Taylor Swift appears on screen",
    "Bad Bunny brings surprise guest",
    "4th down conversion attempt",
    "Player helped off field (injury)",
    "Scoring play overturned by review",
    "Someone at party yells at TV",
    "Someone at party checks phone",
    "Someone says 'Great commercial!'",
    "Dog appears in a commercial",
    "Stefon Diggs spectacular catch",
    "Christian Gonzalez pass breakup",
    "Vrabel's Patriots playing days mentioned",
    "Car or truck commercial airs",
    "Scarlett Johansson in a commercial",
    "George Clooney in a commercial",
    "Peyton Manning in Bud Light ad",
    "Chris Hemsworth in a commercial",
    "Charlie Puth holds 'brave' 3+ seconds",
    "Player or coach cries during anthem",
    "Coach throws or slams headset",
    "First score is a field goal",
    "Coin toss is HEADS",
    "Bad Bunny wears sunglasses at start",
    "Commercial makes fun of AI",
    "Two-point conversion attempted"
]

KID_HIGH = [
    "TOUCHDOWN!",
    "Player catches ball",
    "Cheerleaders!",
    "Yellow flag thrown",
    "Touchdown dance!",
    "FIREWORKS!",
    "Horse in a commercial",
    "Ball gets kicked",
    "Coach looks mad",
    "Replay shown",
    "Crowd goes WILD",
    "Players high-five",
    "Halftime singing",
    "Halftime dancing",
    "Car in commercial",
    "Team huddle",
    "Funny commercial!",
    "Player runs FAST",
    "Big catch!",
    "Big tackle!"
]

KID_MEDIUM = [
    "Dog in commercial",
    "Cat in commercial",
    "Baby in commercial",
    "Someone falls down",
    "Super long throw",
    "Helmet bonk!",
    "Player slides",
    "Player waves to camera",
    "Famous person!",
    "Kids in commercial",
    "Food in commercial",
    "Player points to sky",
    "Superhero in ad",
    "Robot in commercial",
    "Mascot dancing",
    "Big jump!",
    "Score is TIED",
    "Confetti falls!",
    "Ball spike!",
    "Someone does a flip"
]

def generate_card(high_pool, medium_pool):
    """Generate a single bingo card grid."""
    high_positions = []
    medium_positions = []

    for row in range(5):
        for col in range(5):
            if POSITION_TEMPLATE[row][col] is True:
                high_positions.append((row, col))
            elif POSITION_TEMPLATE[row][col] is False:
                medium_positions.append((row, col))

    shuffled_high = random.sample(high_pool, 12)
    shuffled_medium = random.sample(medium_pool, 12)

    grid = [["" for _ in range(5)] for _ in range(5)]

    for i, (row, col) in enumerate(high_positions):
        grid[row][col] = shuffled_high[i]

    for i, (row, col) in enumerate(medium_positions):
        grid[row][col] = shuffled_medium[i]

    grid[2][2] = "FREE"

    return grid

def render_card_html(grid, card_id, is_kid):
    """Render a single card as HTML."""
    card_class = "kid-card" if is_kid else "adult-card"
    card_type = "KID CARD" if is_kid else "ADULT CARD"

    cells_html = ""
    for row in range(5):
        for col in range(5):
            content = grid[row][col]
            if content == "FREE":
                cells_html += '<div class="cell free">★<br>FREE<br>★</div>'
            else:
                cells_html += f'<div class="cell">{content}</div>'

    return f'''
    <div class="card {card_class}">
        <div class="header">
            <h1>BINGO</h1>
            <div class="matchup">SEAHAWKS vs PATRIOTS</div>
            <div class="details">Super Bowl LX • February 8, 2026</div>
            <div class="card-type">{card_type}</div>
        </div>
        <div class="grid">{cells_html}</div>
        <div class="footer">Card {card_id} • Mark 5 in a row to win!</div>
    </div>
    '''

def generate_all_cards():
    """Generate all 17 cards."""
    cards_html = ""

    # 10 adult cards
    for i in range(1, 11):
        grid = generate_card(ADULT_HIGH, ADULT_MEDIUM)
        cards_html += render_card_html(grid, f"A{i}", False)

    # 7 kid cards
    for i in range(1, 8):
        grid = generate_card(KID_HIGH, KID_MEDIUM)
        cards_html += render_card_html(grid, f"K{i}", True)

    return cards_html

CSS_STYLES = '''
@page {
    size: letter portrait;
    margin: 0.4in;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
    width: 7.2in;
    height: 9.2in;
    padding: 0.3in;
    background: white;
    page-break-after: always;
    page-break-inside: avoid;
}

.card:last-child {
    page-break-after: avoid;
}

.header {
    text-align: center;
    margin-bottom: 0.2in;
}

.header h1 {
    font-size: 36pt;
    font-weight: 800;
    letter-spacing: 3px;
    color: #002244;
}

.matchup {
    font-size: 14pt;
    font-weight: 600;
    color: #4a4a4a;
    margin: 5px 0;
}

.details {
    font-size: 10pt;
    color: #888;
}

.card-type {
    display: inline-block;
    font-size: 11pt;
    font-weight: bold;
    padding: 4px 16px;
    border-radius: 20px;
    margin-top: 8px;
}

.adult-card .card-type {
    background: #002244;
    color: white;
}

.kid-card .card-type {
    background: #69be28;
    color: white;
}

.kid-card .header h1 {
    color: #69be28;
}

.grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 2px;
    border: 4px solid #002244;
    background: #002244;
}

.kid-card .grid {
    border-color: #69be28;
    background: #69be28;
}

.cell {
    background: white;
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 4px;
    font-size: 9pt;
    line-height: 1.15;
    font-weight: 500;
}

.kid-card .cell {
    font-size: 11pt;
    font-weight: 600;
}

.cell.free {
    background: linear-gradient(135deg, #002244 0%, #69be28 100%);
    color: white;
    font-weight: 800;
    font-size: 14pt;
}

.kid-card .cell.free {
    background: linear-gradient(135deg, #69be28 0%, #002244 100%);
}

.footer {
    text-align: center;
    margin-top: 0.15in;
    font-size: 9pt;
    color: #666;
}
'''

def main():
    print("Generating Super Bowl LX Bingo Cards...")

    cards_html = generate_all_cards()

    full_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Super Bowl LX Bingo Cards</title>
</head>
<body>
{cards_html}
</body>
</html>'''

    # Generate PDF
    html = HTML(string=full_html)
    css = CSS(string=CSS_STYLES)
    html.write_pdf('superbowl-bingo-cards.pdf', stylesheets=[css])

    print("Generated: superbowl-bingo-cards.pdf")
    print("17 cards total (10 adult + 7 kid)")

if __name__ == "__main__":
    main()
