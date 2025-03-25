const express = require("express");
const path = require("path");
const { spawn } = require("child_process");

const app = express();
const PORT = 3000;

// Serve everything in the "public" folder (including index.html)
app.use(express.static(path.join(__dirname, "public")));

// Also serve static files from "static" (for graph.png)
app.use("/static", express.static(path.join(__dirname, "static")));

/**
 * GET /generate-graph?book_id=12345
 * Spawns the Python script with the given book_id.
 */
app.get("/generate-graph", (req, res) => {
  const bookId = req.query.book_id || "12345";

  // Spawn Python script
  const pythonProcess = spawn("python", [
    path.join(__dirname, "python", "main.py"),
    bookId
  ]);

  // Optional: log Python's stdout and stderr
  pythonProcess.stdout.on("data", (data) => {
    console.log("Python stdout:", data.toString());
  });
  pythonProcess.stderr.on("data", (data) => {
    console.error("Python stderr:", data.toString());
  });

  // When the script finishes, respond to the client
  pythonProcess.on("close", (code) => {
    console.log(`Python script exited with code ${code}`);
    // The graph is now saved as static/graph.png
    // Send a plain text response or JSON
    res.send("Graph generation complete");
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
