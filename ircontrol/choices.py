###################################################
### INPUT TYPES
###################################################
NEGATIVE = 0
NEUTRAL = 1
POSITIVE = 2

INPUT_TYPES = (
	(NEGATIVE, 'Negative'),
	(NEUTRAL, 'Neutral'),
	(POSITIVE, 'Positive')
)


###################################################
### POWER CHOICES
###################################################
TV = 1
STEREO = 2
AIR_CONDITIONER = 3
OTHER = 4

DEVICE_TYPES = (
	(TV, 'TV'),
	(STEREO, 'STEREO'),
	(AIR_CONDITIONER, 'AIR CONDITIONER'),
	(OTHER, 'OTHER')
)


###################################################
### DEVICE LOCATIONS
###################################################
LIVING_ROOM = 1
DINNING_ROOM = 2
BEDROOM = 3
BATHROOM = 4
OTHER = 5

DEVICE_LOCATIONS = (
	(LIVING_ROOM, 'LIVING ROOM'),
	(DINNING_ROOM, 'DINNING ROOM'),
	(BEDROOM, 'BEDROOM'),
	(BATHROOM, 'BATHROOM'),
	(OTHER, 'OTHER')
)


###################################################
### BUTTON STYLES
###################################################
LIGHTBLUE_BUTTON = 'btn-info'
BLUE_BUTTON = 'btn-primary'
YELLOW_BUTTON = 'btn-warning'
GREEN_BUTTON = 'btn-success'
RED_BUTTON = 'btn-danger'

RC_BUTTONS = (
	(LIGHTBLUE_BUTTON, 'LIGHT BLUE'),
	(BLUE_BUTTON, 'BLUE'),
	(YELLOW_BUTTON, 'YELLOW'),
	(GREEN_BUTTON, 'GREEN'),
	(RED_BUTTON, 'RED')
)


