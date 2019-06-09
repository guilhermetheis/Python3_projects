'''
This is a simple textbased game using python
'''
__date__ = "08/06/2019"
__author__ = "Guilherme Theis"
__copyright__ = "Copyright 2019, GTheis"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Guilherme Theis"
__email__ = "guilhermetheis15@gmail.com"
__status__ = "Development"



# Imports

import time
import random
from pyfiglet import Figlet #for fancy opening

class Player: #Player clas

	def __init__(self, hitPoints, profession, level): # initialization of the player

		if (hitPoints < 0 or hitPoints > 99):#verifying if the HP is correct
			print('Your player HP is too big or to small (limits betwen 0 and 99 HP)')
		else:
			self.hitPoints = hitPoints

		if profession not in ['archer', 'warrior', 'priest, mage']:  #verifying if the profession is correct
			print('Your player needs to be one of those: archer, warrior, priest, mage')
		else:
			self.profession = profession
		
		if (level < 1 or level > 30): #verifying if the level is correct
			print('Your character needs to have a level between 1 and 30')
		else:
			self.level = level
		print('A {0} was created with {1}HP, it is level {2}'.format(self.profession, self.hitPoints, self.level))
	
	def __del__(self): #destructor
		print('Destructor')

	def getStats(self): #to return the info of the player
		print('Your player has {0}HP, it is a {1} and it is level {2}'.format(self.hitPoints, self.profession, self.level))

	def attack(self): #attack move
		a = random.randint(0,4)
		if a == 4:
			return 'crit', a*self.level # attack = random (from 0 to 5) * player level
		elif a == 0:
			return 'miss', a*self.level
		else:
			return 'normalAtt', a*self.level

	def receiveAttack(self, enemy, attackType, enemyAttack):
		self.hitPoints = self.hitPoints - enemyAttack
		if attackType == 'crit':
			print('It was a critical hit! The {0} hit you for {1}'.format(enemy, enemyAttack))
		elif attackType == 'miss':
			print('The {0} missed the attack'.format(enemy))
		else:
			print('The {0} hit you for {1}'.format(enemy, enemyAttack))
		if self.hitPoints < 0:
			print('The {0} killed you'.format(enemy))
		else:
			pass	

	def saveCharacter(self):
		wantToSave = input('Do you want to save yout character? (type yes or no) \n')
		if wantToSave == 'yes':
			fileName = input('Input your save file name (without extension) \n')
			file = open('saves/{0}.txt'.format(fileName), 'w+') #creating the character save (w+ to create the file)
			file.write(str(self.hitPoints)+'\n') #\n to jump lines
			file.write(str(self.profession)+'\n')
			file.write(str(self.level))
			file.close()
		else:
			print('Okay then big boy, see you soon')

class Monster:

	def __init__(self, playerLevel): # initialization of the monster (dependent of the player level)
		if playerLevel < 3:
			self.level = random.randint(1,3)
		else:
			self.level = random.randint(playerLevel-2, playerLevel+2) #monster level = player level +- 2
		self.hitPoints = self.level*random.randint(1,3)
		self.profession = random.choice(['Troll', 'Orc', 'Zombie', 'Giant', 'Fire Demon'])
		print('You have encountered a {0}, it is level {1} and has {2}HP'.format(self.profession, self.level, self.hitPoints))

	def attack(self): #attack move
		a = random.randint(0,3)
		if a == 3:
			return 'crit', a*self.level # attack = random (from 0 to 5) * player level
		elif a == 0:
			return 'miss', a*self.level
		else:
			return 'normalAtt', a*self.level

	def receiveAttack(self,  attackType, enemyAttack):
		self.hitPoints = self.hitPoints - enemyAttack
		if attackType == 'crit':
			print('It was a critical hit! You hit the {0} for {1}'.format(self.profession, enemyAttack))
		elif attackType == 'miss':
			print('You missed the attack'.format(self.profession))
		else:
			print('You hit for {1}'.format(self.profession, enemyAttack))
		if self.hitPoints < 0:
			print('You killed the {0}'.format(self.profession))
		else:
			pass
	

def main():
	level = 1 #initial conditions player
	hitPoints = 10
	profession = 'archer'
	f = Figlet(font='slant')
	print(f.renderText('Welcome to\n simpleGame'))
	print('Version {0}'.format(__version__))
	print('{0}. Maintained by {1}, email: {2}'.format(__copyright__, __maintainer__, __email__))
	while True: #first loop to verify if wants to play again
		myArcher = Player(hitPoints, profession, level)
		monster = Monster(myArcher.level)
		while True: #second loop for the game itself
			if (monster.hitPoints <= 0 or myArcher.hitPoints <= 0):
				break
			else:
				archerAttackType, archerAttack = myArcher.attack()
				monsterAttackType, monsterAttack = monster.attack()
				monster.receiveAttack(archerAttackType, archerAttack)
				if monster.hitPoints <= 0:
					break
				else:
					time.sleep(2)
					myArcher.receiveAttack(monster.profession, monsterAttackType, monsterAttack)
					time.sleep(2)

			#testing init limits
			#myFakeHPArcher = Player(100, 'archer', 1)
			#myFakeLevelArcher = Player(10, 'archer', 31)
			#myFakeProf = Player(10, 'paladin', 1)
		myArcher.getStats()	
		playAgain = input('Do you want to play again (type yes or no)\n')
		if playAgain == 'yes':
			if myArcher.hitPoints > 0:
				hitPoints +=2 #add 3 HP if won
				level +=1 #add a level if won
			else:
				pass
		else:
			break
	myArcher.saveCharacter()
			

if __name__ == "__main__":
	main()