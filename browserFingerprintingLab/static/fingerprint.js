(() => {
  const rows = [
    ["language", navigator.language],
    ["languages", (navigator.languages || []).join(", ")],
    ["userAgent", navigator.userAgent],
    ["screenSize", `${screen.width} x ${screen.height}`],
    ["colorDepth", screen.colorDepth],
    ["hardwareConcurrency", navigator.hardwareConcurrency ?? "Unavailable"],
    ["deviceMemory", navigator.deviceMemory ?? "Unavailable"],
    ["windowSize", `${window.innerWidth} x ${window.innerHeight}`],
    ["devicePixelRatio", window.devicePixelRatio],
    ["timeZone", Intl.DateTimeFormat().resolvedOptions().timeZone],
    ["documentReferrer", document.referrer || "Empty"],
  ];
  const body = document.querySelector("#feature-table tbody");
  for (const [name, value] of rows) {
    const tr = document.createElement("tr");
    const th = document.createElement("th");
    const td = document.createElement("td");
    th.textContent = name;
    td.textContent = String(value);
    tr.append(th, td);
    body.append(tr);
  }
  const features = Object.fromEntries(rows);
  document.getElementById("send-features").addEventListener("click", async () => {
    const status = document.getElementById("feature-status");
    try {
      const response = await fetch("/collect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: "active-features", ...features }),
      });
      const result = await response.json();
      status.textContent = `${result.status} (HTTP ${response.status})`;
    } catch (error) {
      status.textContent = `Send failed: ${error.message}`;
    }
  });
  window.fingerprintFeatures = features;
})();
