import temperature_exception



class TooColdTemperatureException(temperature_exception.TemperatureException):

    def __init__(self, mensaje):
        temperature_exception.TemperatureException.__init__(self, mensaje=mensaje)
