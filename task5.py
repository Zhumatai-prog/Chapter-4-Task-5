
class Soldier():
	def __init__(self, name, gun):
		self.name = name
		self.gun = gun


	def fire(self):
		print("tigi-tigitish")


class Guns():
	def __init__(self):
		Soldier.__init__(self)

	def fire_bullets(self):
		print(f"{self.name} is shooting with {self.gun}")
		self.bullets = 30
		while self.bullets >= 0:
			self.fire()
			self.bullets -= 1

			if self.bullets == -1:
				self.reload()
				
	def reload(self):
		self.choice = input("Would you like to reload: y/n ")
		if self.choice == 'y':
			self.fire_bullets()
		else:
			pass

class Act_of_Shooting(Soldier, Guns):
	def __init__(self, name, gun):
		Soldier.__init__(self, name, gun)

Ryan = Act_of_Shooting('Ryan', 'AK47')
Ryan.fire_bullets()