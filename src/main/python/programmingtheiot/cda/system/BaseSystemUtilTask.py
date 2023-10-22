#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import programmingtheiot.common.ConfigConst as ConfigConst

class BaseSystemUtilTask():
	"""
	Shell implementation representation of class for student implementation.
	
	"""
	
	"def __init__(self, name = ConfigConst.NOT_SET, typeID = ConfigConst.DEFAULT_SENSOR_TYPE):"
	def __init__(self, name: str = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE):
		"pass"
		self.name = name
		self.typeID = typeID
	
	def getName(self) -> str:
		"pass"
		return self.name
	
	def getTypeID(self) -> int:
		"pass"
		return self.typeID
	
	def getTelemetryValue(self) -> float:
		pass
	