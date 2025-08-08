document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("uploadForm");
  const fileInput = document.getElementById("audioFile");
  const resultDiv = document.getElementById("result");
  const errorDiv = document.getElementById("error");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const file = fileInput.files[0];
    if (!file) return alert("Please select an audio file.");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/transcribe/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      resultDiv.textContent = "🗣️ Transcription: " + data.transcription;
      errorDiv.textContent = "";
    } catch (err) {
      errorDiv.textContent = "❌ Transcription failed: " + err.message;
      resultDiv.textContent = "";
    }
  });
});

async function keystrokeAuth() {
  const username = document.getElementById("username").value;
  const pattern = document.getElementById("pattern").value;

  const formData = new URLSearchParams();
  formData.append("username", username);
  formData.append("pattern", pattern);

  try {
    const response = await fetch("http://127.0.0.1:8000/auth/keystroke/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    document.getElementById("result").textContent = "🔐 Auth Result: " + data.auth_result;
  } catch (err) {
    document.getElementById("error").textContent = "❌ Keystroke auth failed.";
  }
}

async function analyzeSentiment() {
  const text = document.getElementById("sentimentText").value;

  const formData = new URLSearchParams();
  formData.append("text", text);

  try {
    const response = await fetch("http://127.0.0.1:8000/nlp/sentiment/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    document.getElementById("result").textContent = "😊 Sentiment: " + data.sentiment;
  } catch (err) {
    document.getElementById("error").textContent = "❌ Sentiment analysis failed.";
  }
}

async function classifyIntent() {
  const text = document.getElementById("intentText").value;

  const formData = new URLSearchParams();
  formData.append("text", text);

  try {
    const response = await fetch("http://127.0.0.1:8000/ai/intent/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    document.getElementById("result").textContent = "🎯 Intent: " + data.intent;
  } catch (err) {
    document.getElementById("error").textContent = "❌ Intent classification failed.";
  }
}

async function summarizeText() {
  const text = document.getElementById("summaryText").value;

  const formData = new URLSearchParams();
  formData.append("text", text);

  try {
    const response = await fetch("http://127.0.0.1:8000/nlp/summarize/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    document.getElementById("result").textContent = "📝 Summary: " + data.summary;
  } catch (err) {
    document.getElementById("error").textContent = "❌ Summarization failed.";
  }
}

async function setLanguage() {
  const lang = document.getElementById("langCode").value;

  const formData = new URLSearchParams();
  formData.append("lang_code", lang);

  try {
    const response = await fetch("http://127.0.0.1:8000/set_language/", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    document.getElementById("result").textContent = "🌍 Language set to: " + lang;
  } catch (err) {
    document.getElementById("error").textContent = "❌ Setting language failed.";
  }
}
a