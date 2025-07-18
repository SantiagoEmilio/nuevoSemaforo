const luces = {
  rojo: document.getElementById("rojo"),
  amarillo: document.getElementById("amarillo"),
  verde: document.getElementById("verde")
};

const label = document.getElementById("estado-label");

function actualizarVista(estado) {
  Object.keys(luces).forEach(color => {
    luces[color].classList.toggle("activo", estado === color);
  });
  label.textContent = `Luz activa: ${estado.toUpperCase()}`;
}

function esperar(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function cicloSemaforo() {
  while (true) {
    // 🔴 Rojo
    actualizarVista("rojo");
    await esperar(6000); // 6 segundos

    // 🟡 Amarillo
    actualizarVista("amarillo");
    await esperar(3000); // 3 segundos

    // 🟢 Verde
    actualizarVista("verde");
    await esperar(2000); // 2 segundos
  }
}

cicloSemaforo();
