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
VERY_LOW = 1
LOW = 2
MEDIUM = 3
HIGH = 4
VERY_HIGH = 5

POWER_CHOICES = (
	(VERY_LOW, 'Very Low'),
	(LOW, 'Low'),
	(MEDIUM, 'Medium'),
	(HIGH, 'High'),
	(VERY_HIGH, 'Very High'),
)


###################################################
### RESOURCE TYPE CHOICES
###################################################
AUDIO = 'sounds'
PICS = 'pics'
SMILEYS = 'smileys'
DOCUMENTS = 'documents'

RESOURCE_TYPE_CHOICES = (
	(AUDIO, 'Audio File'),
	(PICS, 'Picture'),
	(SMILEYS, 'Smiley Picture'),
	(DOCUMENTS, 'Documents, GIFs, ANY FILE')
)
