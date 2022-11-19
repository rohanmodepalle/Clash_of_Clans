# Village Layout
BG = "  "
SIDE_WALL = "| "
TOP_WALL = "- "
TOP_RIGHT_CORNER = "┐"
TOP_LEFT_CORNER = "┌ "
BOTTOM_RIGHT_CORNER = "┘"
BOTTOM_LEFT_CORNER = "└ "
ROWS = 50
COLS = 50

# ---------------------------------------------------------------------------------------------------------------------#

# Buildings

## Town Hall
MAX_TOWN_HALL_HEALTH = 200
TOWN_HALL_SYMBOL = 'T '

## Hut
MAX_HUT_HEALTH = 100
HUT_SYMBOL = 'H '

## Cannon
MAX_CANNON_HEALTH = 100
CANNON_SYMBOL = 'C '
CANNON_RANGE = 7
CANNON_DAMAGE = 10

## Wizard Tower
MAX_WT_HEALTH = 200
WT_SYMBOL = 'W '
WT_RANGE = CANNON_RANGE
WT_DAMAGE = CANNON_DAMAGE

## Wall
MAX_WALL_HEALTH = 75
WALL_SYMBOL = '. '



# ---------------------------------------------------------------------------------------------------------------------#

# Characters

## Barbarian
MAX_BARB_HEALTH = 100
BARB_DAMAGE = 10
BARB_SPEED = 1
BARB_SYMBOL = 'B '
MAX_BARBARIANS = 6

## King
MAX_KING_HEALTH = 150
KING_DAMAGE = 20
KING_SPEED = 2
KING_SYMBOL = 'K '

## Queen
MAX_QUEEN_HEALTH = 150
QUEEN_DAMAGE = 15
QUEEN_SPEED = 2
QUEEN_RANGE = 8
QUEEN_SYMBOL = 'Q '

## Archer
MAX_ARCHER_HEALTH = MAX_BARB_HEALTH // 2
ARCHER_DAMAGE = BARB_DAMAGE // 2
ARCHER_SPEED = BARB_SPEED * 2
ARCHER_SYMBOL = 'A '
ARCHER_RANGE = 4
MAX_ARCHERS = 6

## Balloon
MAX_BALLOON_HEALTH = MAX_BARB_HEALTH
BALLOON_DAMAGE = BARB_DAMAGE * 2
BALLOON_SPEED = BARB_SPEED * 2
BALLOON_SYMBOL = 'O '
MAX_BALLOONS = 3


