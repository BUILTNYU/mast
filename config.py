OUTPUT_REQUEST = "output_request.csv"
OUTPUT_NODE = "output_node.csv"
OUTPUT_BUS = "output_bus.csv"
OUTPUT_COST = "output_cost.csv"

R_LENGTH = 5 # ride length(miles)
R_TIME = 30 # ride time(mins)
MAX_DEV = .5 # max y deviation. grid is R_LENGTH x (2*MAX_DEV)
MAX_R = 0 # max walking radius from 3 main checkpoints? (unclear)
MIN_DIST = 0.25

BUS_SPEED = 20 # bus speed (mph)
W_SPEED = 5 # walk speed (mph)

N_RIDES = 3 # number of buses that will come through
HEADWAY = 15 # headway (mins)
N_INT_POINTS = 2 # number of intermediate checkpoints
WAITING_TIME = 10 # bus waiting time to allow load / unload (secs)

N_CUSTOMERS_PER_HR = 25
PD_PCT = .1
PRD_PCT = .4
RPD_PCT = .4
RPRD_PCT = .1
#PD_PCT = 0
#PRD_PCT = 1
#RPD_PCT = 0
#RPRD_PCT = 0

PTYPE_WEIGHTS = [PD_PCT, PRD_PCT, RPD_PCT, RPRD_PCT]
assert (PD_PCT + PRD_PCT + RPD_PCT + RPRD_PCT - 1) < .000001

ADVANCE_DEMAND = 20 # MINUTES of customer demand in advance of first ride

WEIGHT_EXTRAMILES = .25 #0.25
WEIGHT_EXTRA_PSGM = 0
WEIGHT_EXTRA_PSGRT = .25   #0.25
WEIGHT_EXTRA_PSGWT = .5     #0.5
WEIGHT_EXTRA_PSGDLY = 0
assert (WEIGHT_EXTRAMILES + WEIGHT_EXTRA_PSGM + WEIGHT_EXTRA_PSGRT + WEIGHT_EXTRA_PSGWT + WEIGHT_EXTRA_PSGDLY - 1) < .000001

MIN_INIT_SLACK = .5 # b/w 0 and 1, pi in the paper
MAX_BACK = 1 # max backtracking (miles)

ALLOW_STEPS = False

T_STEP = 1 # time step (seconds)

ALLOW_MERGE = True
ALLOW_WALKING = True
WALK_MULTIPLIER = 1.0
MAX_WALK_TIME = 20 #max walking time (minutes)
MAX_MERGE_TIME = 2 #max walking time (minutes)

COST_RT = 0.0
COST_WT = 0.0
COST_D = 1.0
