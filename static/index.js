const buttons_ip = document.getElementById("ip-button");
const buttons_conector = document.getElementById("conector-button");

async function ip() {
  const scanner = await fetch("http://127.0.0.1:8000/scanner/ip");
  const data = await scanner.json();
  console.log(data);
}

async function wifi() {
  const scanner = await fetch("http://127.0.0.1:8000/scanner/wifi");
  const data = await scanner.json();
  console.log(data);
}

buttons_ip.addEventListener("click", ip);

buttons_conector.addEventListener("click", wifi);
