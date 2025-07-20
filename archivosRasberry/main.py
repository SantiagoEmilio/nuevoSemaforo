from wifi import conectar_wifi
from firebase import Firebase
from archivosRasberry.semaforo import Semaforo

def main():
    if conectar_wifi():
        sem = Semaforo()
        fb = Firebase("https://semaforooo-3314e-default-rtdb.firebaseio.com")
        print("Iniciando ciclo del semáforo...")
        while True:
            sem.ciclo(firebase=fb)
    else:
        print("No se pudo conectar a WiFi. Terminando programa.")

if __name__ == "__main__":
    main()

