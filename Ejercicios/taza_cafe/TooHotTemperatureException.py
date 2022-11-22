import temperature_exception



class TooHotTemperatureException(temperature_exception.TemperatureException):

    def __init__(self, mensaje):
        temperature_exception.TemperatureException.__init__(self, mensaje=mensaje)





