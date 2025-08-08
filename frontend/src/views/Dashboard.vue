<template>
  <div class="dashboard">
    <h1>🎛 AI Secure Voice Assistant Dashboard</h1>

    <div class="card-grid">
      <div class="card" @click="goTo('voice')">
        🎤 Voice Recorder
      </div>
      <div class="card" @click="goTo('auth')">
        🔐 Keystroke Auth
      </div>
      <div class="card" @click="goTo('report')">
        📊 Reports
      </div>
      <div class="card" @click="goTo('language')">
        🌐 Language Selector
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goTo(route) {
      this.$router.push(`/${route}`);
    }
  }
};
</script>

<style scoped>
.dashboard {
  padding: 40px;
  text-align: center;
}
.card-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
  margin-top: 40px;
}
.card {
  background: #f0f0f0;
  border-radius: 12px;
  padding: 20px 30px;
  cursor: pointer;
  font-size: 18px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  transition: 0.2s ease;
}
.card:hover {
  background: #e0e0e0;
  transform: scale(1.05);
}
</style>
