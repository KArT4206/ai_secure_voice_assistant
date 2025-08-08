<template>
  <div class="language-selector">
    <h2>🌐 Select Your Language</h2>
    <select v-model="selectedLang" @change="setLanguage">
      <option disabled value="">Select a language</option>
      <option value="en">English</option>
      <option value="hi">Hindi</option>
      <option value="es">Spanish</option>
      <option value="fr">French</option>
      <option value="ta">Tamil</option>
    </select>

    <p v-if="confirmation">✅ Language set to: {{ languageName }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedLang: "",
      confirmation: false
    };
  },
  computed: {
    languageName() {
      const map = {
        en: "English",
        hi: "Hindi",
        es: "Spanish",
        fr: "French",
        ta: "Tamil"
      };
      return map[this.selectedLang] || "";
    }
  },
  methods: {
    async setLanguage() {
      const formData = new FormData();
      formData.append("lang_code", this.selectedLang);

      try {
        const res = await fetch("http://127.0.0.1:8000/set_language/", {
          method: "POST",
          body: formData
        });

        const data = await res.json();
        if (data.status === "success") {
          this.confirmation = true;
        } else {
          this.confirmation = false;
        }
      } catch (err) {
        console.error("Language setting failed:", err);
        this.confirmation = false;
      }
    }
  }
};
</script>

<style scoped>
.language-selector {
  text-align: center;
  margin-top: 40px;
}
select {
  padding: 10px;
  font-size: 16px;
  margin-top: 10px;
}
</style>
