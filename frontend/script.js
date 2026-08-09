const API = "http://127.0.0.1:8000";

const table = document.querySelector("#device-table");
const errorBox = document.querySelector("#error");
const apiStatus = document.querySelector("#api-status");
const statusDot = document.querySelector("#status-dot");

function statusClass(status) {
  return status.toLowerCase();
}

async function loadDevices() {
  try {
    errorBox.classList.add("hidden");
    apiStatus.textContent = "API online";
    statusDot.style.background = "#72e2ba";

    const response = await fetch(`${API}/devices`);

    if (!response.ok) {
      throw new Error(`API returned ${response.status}`);
    }

    const devices = await response.json();

    table.innerHTML = devices.map(device => `
      <tr>
        <td>${device.id}</td>
        <td><strong>${device.name}</strong></td>
        <td>${device.type}</td>
        <td>
          <span class="status ${statusClass(device.status)}">
            ${device.status}
          </span>
        </td>
        <td>${device.battery}%</td>
      </tr>
    `).join("");

    document.querySelector("#total").textContent = devices.length;

    document.querySelector("#online").textContent =
      devices.filter(device => device.status === "Online").length;

    document.querySelector("#offline").textContent =
      devices.filter(device => device.status === "Offline").length;

    const average = devices.length
      ? Math.round(
          devices.reduce((sum, device) => sum + device.battery, 0) /
          devices.length
        )
      : 0;

    document.querySelector("#battery").textContent = `${average}%`;

  } catch (error) {
    apiStatus.textContent = "API offline";
    statusDot.style.background = "#ff8c8c";

    errorBox.textContent =
      "Could not connect to the FastAPI backend. Start the API on port 8000.";

    errorBox.classList.remove("hidden");
  }
}

document.querySelector("#refresh").addEventListener("click", loadDevices);

loadDevices();
