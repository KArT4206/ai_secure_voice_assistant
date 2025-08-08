<template>
  <div class="report-viewer">
    <h2>📊 Report Viewer</h2>
    <form @submit.prevent="fetchReport">
      <label for="type">Report Type:</label>
      <select v-model="reportType" required>
        <option disabled value="">Select one</option>
        <option value="transcription">Transcription</option>
        <option value="sentiment">Sentiment</option>
        <option value="intent">Intent</option>
      </select>

      <label for="input">Input Text (if needed):</label>
      <textarea v-model="userInput" placeholder="Enter text if report type needs it..."></textarea>

      <button type="submit">Get Report</button>
    </form>

    <div v-if="reportResult" class="result-box">
      <h3>📋 Result</h3>
      <p>{{ reportResult }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      reportType: "",
      userInput: "",
      reportResult: ""
    };
  },
  methods: {
    async fetchReport() {
      let endpoint = "";
      let formData = new FormData();

      if (this.reportType === "sentiment") {
        endpoint = "nlp/sentiment/";
        formData.append("text", this.userInput);
      } else if (this.reportType === "intent") {
        endpoint = "ai/intent/";
        formData.append("text", this.userInput);
      } else {
        this.reportResult = "Please use the voice recorder for transcription reports.";
        return;
      }

      try {
        const res = await fetch(`http://127.0.0.1:8000/${endpoint}`, {
          method: "POST",
          body: formData
        });
        const data = await res.json();
        this.reportResult = JSON.stringify(data, null, 2);
      } catch (err) {
        this.reportResult = "Error fetching report.";
        console.error(err);
      }
    }
  }
};
</script>

<style scoped>
.report-viewer {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 12px;
  box-shadow: 2px 2px 10px #eee;
}
textarea, select, input {
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #aaa;
}
button {
  padding: 10px 20px;
  font-weight: bold;
  cursor: pointer;
}
.result-box {
  margin-top: 20px;
  padding: 15px;
  background: #f9f9f9;
  border-left: 5px solid #4caf50;
}
</style>
