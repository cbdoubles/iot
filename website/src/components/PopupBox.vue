<template>
    <div class="popup-box" v-if="isVisible">
      <div class="popup-content">
        <!-- Your content here -->
        <p>{{ message }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isVisible: false,
        message: "",
      };
    },
    methods: {
      showPopup(message) {
        return new Promise((resolve) => {
          this.message = message;
          this.isVisible = true;
          console.log(this.isVisible);

          setTimeout(() => {
            this.hidePopup();
            resolve(); // Resolve the promise after the timeout
          }, 1000); // Hide after 4 seconds
        });
      },
      hidePopup() {
        this.isVisible = false;
      },
    },
  };
  </script>
  
  <style scoped>
  .popup-box {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    border: 1px solid #ccc;
    padding: 20px;
    width: 50%;
    max-width: 400px; /* Adjust as needed */
    z-index: 9999;
  }
  
  .popup-content {
    text-align: center;
  }
  </style>
  