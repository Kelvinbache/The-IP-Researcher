const buttons_ip = document.getElementById("ip-button");
const buttons_connector = document.getElementById("connector-button");
const container = document.getElementById("container_content");
let content = "";
const ul = document.createElement("ul");
const li = document.createElement("li");

ul.appendChild(li);
ul.className = "list";
container.appendChild(ul);

// block buttons
function loading() {
  buttons_ip.disabled = true;
  buttons_ip.textContent = "Loading...";
  buttons_ip.className = "button loading";

  buttons_connector.disabled = true;
  buttons_connector.textContent = "Loading...";
  buttons_connector.className = "button loading";
}

// unblock buttons
function completeLoading() {
  buttons_ip.disabled = false;
  buttons_ip.textContent = "IP";
  buttons_ip.className = "button button-ip";

  buttons_connector.disabled = false;
  buttons_connector.textContent = "Connector";
  buttons_connector.className = "button button-connector";
}

async function ip() {
  loading();

  try {
    const scanner = await fetch("http://127.0.0.1:8000/scanner/ip");
    const data = await scanner.json();
    content = JSON.stringify(data).replace(/[{}"]/g, "").replace(/,/g, "\n") + "\n";
    li.textContent = content;

  } catch (error) {
    console.error("Error fetching IP data:", error);
  } finally {
    completeLoading();
  }
}

// block button wifi
async function wifi() {
  loading();

  try {
    const scanner = await fetch("http://127.0.0.1:8000/scanner/wifi");
    const data = await scanner.json();

    content = JSON.stringify(data).replace(/[{}"]/g, "").replace(/,/g, "\n");
    li.textContent = content;

  } catch (error) {
    console.error("Error fetching WiFi data:", error);
  } finally {
    completeLoading();
  }
}

buttons_ip.addEventListener("click", ip);

buttons_connector.addEventListener("click", wifi);
