import network
import time

_redes_wifi = {
    'fogel': '123456789',
    'Girón': 'pablo2121',
    'selp': '12345678jhs',
    'CLARO_eUBJxZ': 'F9B0647b51',
    'CLARO_eYvV7H': '25F8BBA54'
    
}

def agregar_red(ssid, password):
    _redes_wifi[ssid] = password
    print(f"Red '{ssid}' agregada.")

def conectar_wifi(intentos=15):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not _redes_wifi:
        print("No hay redes WiFi para conectar.")
        return False

    for ssid, password in _redes_wifi.items():
        print(f"Intentando conectar a '{ssid}'...")
        wlan.connect(ssid, password)

        for _ in range(intentos):
            if wlan.isconnected():
                print(f"✅ Conectado a {ssid}")
                print("IP:", wlan.ifconfig()[0])
                return True
            time.sleep(1)

        print(f"❌ No se pudo conectar a {ssid}")

    print("⚠️ No se pudo conectar a ninguna red.")
    return False



