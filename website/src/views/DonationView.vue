<template>
    <div>
      <h1>Donation Page</h1>
      <TextInput @form-submitted="handleFormSubmitted" />
    </div>
  </template>
  
  <script>
  import TextInput from '@/components/DonationInput.vue';
  
  export default {
    components: {
      TextInput,
    },
    methods: {
      handleFormSubmitted(data) {
        console.log('Form submitted in DonationInput component!');
        console.log('Title:', data.title);
        console.log('Description:', data.description);
        // Perform any additional actions with the submitted data
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add styling if needed */
  </style>  