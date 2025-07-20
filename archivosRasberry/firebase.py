import urequests
import json
import time
import gc

class Firebase:
    def __init__(self, url_base):
        self.url_base = url_base.rstrip('/')

    def enviar_estado(self, estado, duracion, activo=False):
        timestamp = int(time.time() * 1000)
        data = {
            "estado": estado,
            "duracion": duracion,
            "activo": activo,
            "timestamp": timestamp
        }

        try:
            headers = {'Content-Type': 'application/json'}
            data_json = json.dumps(data)

            # ✅ Actualizar estado actual
            response1 = urequests.patch(f"{self.url_base}/semaforo/estado_actual.json", data=data_json, headers=headers)
            response1.close()

            # ✅ Guardar en historial
            response2 = urequests.post(f"{self.url_base}/semaforo/historial.json", data=data_json, headers=headers)
            response2.close()

            print("✅ Estado enviado con éxito:", data)

        except Exception as e:
            print("❌ Error al enviar datos a Firebase:", e)

        # ✅ Forzar liberación de memoria
        gc.collect()

