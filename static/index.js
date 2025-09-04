const buttons_ip = document.getElementById("ip-button");
const buttons_conector = document.getElementById("conector-button");
const container = document.getElementById("container");

async function ip() {
  const scanner = await fetch("http://127.0.0.1:8000/scanner/ip");
  const data = await scanner.json();
  console.log(data);
}

// block button wifi 
async function wifi() {
  const scanner = await fetch("http://127.0.0.1:8000/scanner/wifi");
  const data = await scanner.json();
  const ul = document.createElement("ul");

  data.forEach((element) => {
    const devices = document.createElement("li");

    devices.textContent = element;
    ul.appendChild(devices);
  });

  container.appendChild(ul);
}

buttons_ip.addEventListener("click", ip);

buttons_conector.addEventListener("click", wifi);
