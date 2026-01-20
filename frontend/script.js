async function analyzeMood() {
  const mood = document.getElementById("moodInput").value;
  const output = document.getElementById("output");

  if (mood.trim().length < 5) {
    output.innerText = "Please describe your feelings in a bit more detail.";
    return;
  }

  output.innerText = "Analyzing your mood...";

  try {
    const response = await fetch("https://YOUR_BACKEND_URL/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: mood })
    });

    const data = await response.json();

    output.innerText =
      `Emotion: ${data.emotion}\n\n` +
      `Summary: ${data.summary}\n\n` +
      `Advice: ${data.advice}`;

  } catch (err) {
    output.innerText = "Unable to connect to the server. Please try again later.";
  }
}
