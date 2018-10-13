#################     To Do List    #####################
#                                                       #
# 1. Auto Join PT                                       #
# 2. Auto Change Channel                                #
# 3. Auto Join Dungeon                                  #
# 4. Properly define the list of keys                   #
# 5. Solve key conflict issues when casting buff + skill#
# 6. ???                                                #
#                                                       #
#########################################################

from keypress import keyPress, keyPresswithDur
import time
import threading
import random
# Movement related vars
movementDirection = 1
movementDistMin = 0.1
movementDistMax = 0.8
movementDuration = 0.0
movementCountMin = 6
movementCountMax = 12
movementCount = random.choice(range(movementCountMin,movementCountMax,1))

directions = 1
noOfSkillsSet = 1 # The number of set of skills your character has. 

def skillCast():
	global directions
	rand = [1, 2, 3, 4, 5]
	duration = 1
	# Cast your main skill for N times 
	# This is to prevent consistent behaviours on your player which might trigger the BOT detectors.
	for x in range(random.choice(rand)):
		keyPress('q')
	# Press direction key twice to change direction
	directions = not directions

# Modify this accordingly based on your skill key bindings
def buffCast():
	# Cast buffs every N mins
	# This is to prevent consistent behaviours on your player which might trigger the BOT detectors.
	global noOfSkillsSet
	rand = random.sample(range(12, 30), 8)
	print("'" + str(rand) + "'" + " seconds until next castBuff()")
	threading.Timer(random.choice(rand), buffCast).start()
	buffKeys = ['1', '2', '3', '4']
	switchKey = 'f1'
	for x in range(noOfSkillsSet): # 3 Sets of skill key bindings
		for keyValue in buffKeys:
			keyPress(keyValue)
		if (noOfSkillsSet != 1):
			keyPress(switchKey)

def charMove():
	global movementDirection, movementDuration, movementCount
	duration = random.uniform(movementDistMin,movementDistMax)
	if movementDirection:
		movementDuration += duration
		keyPresswithDur('d', duration)
	else:
		movementDuration -= duration
		keyPresswithDur('a', duration)

	if movementCount <= 0:
		if movementDuration > 0:
			keyPresswithDur('a', movementDuration)
		else:
			keyPresswithDur('d', movementDuration * -1)

		print ("Zero-ing character to starting point")
		movementCount = random.choice(range(movementCountMin,movementCountMax,1))
		movementDuration = 0.0

	movementDirection = not movementDirection
	movementCount -= 1

	
