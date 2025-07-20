from machine import Pin
import time

class Semaforo:
    def __init__(self):
        self.led_rojo = Pin(10, Pin.OUT)
        self.led_amarillo = Pin(11, Pin.OUT)
        self.led_verde = Pin(12, Pin.OUT)

    def apagar_todos(self):
        self.led_rojo.value(0)
        self.led_amarillo.value(0)
        self.led_verde.value(0)

    def ciclo(self, firebase=None):
        # 🔴 Rojo
        self.apagar_todos()
        self.led_rojo.value(1)
        if firebase:
            firebase.enviar_estado("rojo", 10, activo=True)
        time.sleep(10)

        # 🟡 Amarillo
        self.apagar_todos()
        self.led_amarillo.value(1)
        if firebase:
            firebase.enviar_estado("amarillo", 5)
        time.sleep(5)

        # 🟢 Verde
        self.apagar_todos()
        self.led_verde.value(1)
        if firebase:
            firebase.enviar_estado("verde", 4)
        time.sleep(4)

