<template>
  <div class="voice-recorder">
    <button @click="toggleRecording">
      {{ isRecording ? 'Stop Recording' : 'Start Recording' }}
    </button>
    <p v-if="transcript">📝 Transcript: {{ transcript }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isRecording: false,
      mediaRecorder: null,
      audioChunks: [],
      transcript: ""
    };
  },
  methods: {
    async toggleRecording() {
      if (!this.isRecording) {
        this.audioChunks = [];
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.mediaRecorder = new MediaRecorder(stream);

        this.mediaRecorder.ondataavailable = event => {
          if (event.data.size > 0) {
            this.audioChunks.push(event.data);
          }
        };

        this.mediaRecorder.onstop = this.sendAudio;
        this.mediaRecorder.start();
        this.isRecording = true;
      } else {
        this.mediaRecorder.stop();
        this.isRecording = false;
      }
    },

    async sendAudio() {
      const audioBlob = new Blob(this.audioChunks, { type: 'audio/webm' });
      const formData = new FormData();
      formData.append('file', audioBlob, 'audio.webm');

      try {
        const response = await fetch("http://127.0.0.1:8000/transcribe/", {
          method: "POST",
          body: formData
        });
        const result = await response.json();
        this.transcript = result.transcription;
      } catch (error) {
        this.transcript = "Error during transcription.";
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
.voice-recorder {
  text-align: center;
  margin-top: 20px;
}
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
