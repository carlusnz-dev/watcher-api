const { spawn } = require("child_process");
const path = require("path");
const os = require("os");

const isWin = os.platform() === "win32";

const pythonPath = path.join(
  __dirname,
  "..",
  "server",
  "venv",
  isWin ? "Scripts" : "bin",
  isWin ? "python.exe" : "python"
);

const scriptPath = path.join(__dirname, "..", "server", "run.py");

console.log(`[Script] Detectado OS: ${os.platform()}`);
console.log(`[Script] Iniciando Python em: ${pythonPath}`);

const flaskProcess = spawn(pythonPath, [scriptPath], { stdio: "inherit" });

flaskProcess.on("close", (code) => {
  console.log(`Flask encerrou com código ${code}`);
});
