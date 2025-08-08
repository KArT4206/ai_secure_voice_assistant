<template>
  <div class="auth-modal">
    <h2>🔐 Keystroke Authentication</h2>
    <form @submit.prevent="authenticateUser">
      <label for="username">Username:</label>
      <input v-model="username" type="text" id="username" required />

      <label for="keystrokes">Type this phrase:</label>
      <input
        v-model="typedPattern"
        type="text"
        id="keystrokes"
        placeholder="the quick brown fox"
        @keydown="recordTiming"
        @keyup="saveTiming"
        required
      />

      <button type="submit">Verify</button>
    </form>
    <p v-if="result">{{ result }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      typedPattern: "",
      keyTimings: [],
      lastKeyTime: null,
      result: ""
    };
  },
  methods: {
    recordTiming() {
      this.lastKeyTime = performance.now();
    },
    saveTiming() {
      if (this.lastKeyTime !== null) {
        const duration = performance.now() - this.lastKeyTime;
        this.keyTimings.push(duration.toFixed(3));
        this.lastKeyTime = null;
      }
    },
    async authenticateUser() {
      const formData = new FormData();
      formData.append("username", this.username);
      formData.append("pattern", this.keyTimings.join(","));

      try {
        const response = await fetch("http://127.0.0.1:8000/auth/keystroke/", {
          method: "POST",
          body: formData
        });

        const data = await response.json();
        this.result = `Auth Status: ${data.auth_result}`;
      } catch (error) {
        this.result = "Error during authentication.";
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
.auth-modal {
  max-width: 400px;
  margin: 30px auto;
  padding: 20px;
  border: 1px solid #aaa;
  border-radius: 10px;
  box-shadow: 2px 2px 10px #ddd;
}
label, input, button {
  display: block;
  width: 100%;
  margin: 10px 0;
}
button {
  padding: 10px;
  font-weight: bold;
}
</style>
