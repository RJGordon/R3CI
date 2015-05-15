class ScribBot:

	def __init__(name, com):
		self.robot = myro.makeRobot(name, com)
		self.controller = R3Controller.R3Controller()

	def forward(self, distance):
		angle = self.robot.getAngle()
		self.controller.getForwardCoords(angle, distance)
		
	def turnToFace(self, UID):
		curAngle = self.robot.getAngle()
		turnAngle = self.controller.getAngleToRobot(UID)
		self.robot.turnBy(turnAngle)