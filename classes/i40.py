class Room():
    temperatureSetpoint = 21
    humiditySetpoint = 30
    def __init__(self,temp,humidity,humSet):
        self.temperature = temp
        self.humidity = humidity
        self.humiditySetpoint = humSet

    def setHumiditySetpoint(self,newhumSet)
        self.humiditySetpoint = newhumSet



e208 = Room(24,40,30)
e223 = Room(22,55,30)
e223.setHumiditySetpoint(35)

e223.humiditySetpoint = 35