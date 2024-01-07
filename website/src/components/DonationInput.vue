<template>
    <div>
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="title" />
  
      <label for="description">Description:</label>
      <textarea id="description" v-model="description"></textarea>
  
      <button @click="submitForm">Submit</button>
      <PopupBox ref="popupBox" />
    </div>
  </template>
  
  <script>
  import dblib from '@/dblib';
  import PopupBox from '@/components/PopupBox.vue';
  
  export default {
    components: {
        PopupBox,
    },

    data() {
      return {
        title: '',
        description: '',
        box: '',
        box_id: '',
        box_number: 0,
        get_image: '',
      };
    },
    mixins: [dblib],

    methods: {
      async submitForm() {
        try {
          await this.showPopup(`Go to Box ${this.box_number} to donate your item. Thank you!`);
          await this.createProduct({
            box_uid: this.box_id,
            title: this.title, 
            description: this.description,
            get_image: this.get_image,
          });
          this.$router.push({path: `/login`});
  
          // Optionally, you can handle the response - uncomment
          // console.log('Server Response:', response.data);
  
          // Emit an event to notify the parent component
          this.$emit('form-submitted', { 
            box_id: this.box_id,
            box_number: this.box_number,
            title: this.title, 
            description: this.description,
            get_image: this.get_image,
          });
  
        } catch (error) {
          console.error('Error submitting form:', error);
          // Optionally, you can handle errors and show a message to the user
        }
      },

      async showPopup(message) {
            // Access the showPopup method of the PopupBox component
            await this.$refs.popupBox.showPopup(message);
        },
    },

    async created() {
    // Call getItems when the component is created
        try {
            this.isLoading = true;
            this.box = await this.getFreeBox();
            console.log("Box_num: ", this.box.box_num);
            if(this.box.box_num == -1) {
              await this.showPopup(`There are no available boxes :((`);
              this.$router.push({path: `/login`});
            } else {
              this.box_id = this.box.unique_ID;
              this.box_number = this.box.box_num;
              console.log("Box_id: ", this.box_id);
              console.log("Box_num: ", this.box_number);
            }
        } catch (error) {
            console.error('Error fetching product:', error);
        } finally {
            this.isLoading = false;
        }
    }
  };
  </script>
  
  <style scoped>
  /* Add styling if needed */
  </style>
  