// 🎨 Semáforo sincronizado con Firebase y Raspberry
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-app.js";
import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-database.js";

// Configuración Firebase
const firebaseConfig = {
  apiKey: "AIzaSyDZTRFG7yBzizPSJJImWddGwbyQiWQKGH8",
  authDomain: "raspberry-pi-pico-w-5635e.firebaseapp.com",
  databaseURL: "https://raspberry-pi-pico-w-5635e-default-rtdb.firebaseio.com",
  projectId: "raspberry-pi-pico-w-5635e",
  storageBucket: "raspberry-pi-pico-w-5635e.appspot.com",
  messagingSenderId: "5310962444",
  appId: "1:5310962444:web:ac110a2284b6e138694729"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const semaforoRef = ref(db, 'semaforo');

const luces = {
  rojo: document.getElementById("rojo"),
  amarillo: document.getElementById("amarillo"),
  verde: document.getElementById("verde")
};

const label = document.getElementById("estado-label");

function actualizarVista(estado) {
  Object.keys(luces).forEach(color => {
    luces[color].classList.remove("activo");
  });
  if (luces[estado]) {
    luces[estado].classList.add("activo");
    label.textContent = `Luz activa: ${estado.toUpperCase()}`;
  } else {
    label.textContent = "Esperando datos de la Raspberry...";
  }
}

onValue(semaforoRef, (snapshot) => {
  const data = snapshot.val();
  if (data && data.estado) {
    actualizarVista(data.estado);
  } else {
    label.textContent = "Esperando conexión con Firebase...";
  }
});
