<template>
  <div>

    
    <form id="donationForm" @submit.prevent="console.log(form)">
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="title" />

      <label for="description">Description:</label>
      <textarea id="description" v-model="description"></textarea>

      <button @click="submitForm">Submit</button>
      <PopupBox ref="popupBox" />

      <div class="hello">
        <picture-input ref="pictureInput" width="600" height="600" margin="16" accept="image/jpeg,image/png" size="10"
          button-class="btn" :custom-strings="{
            upload: '<h1>Bummer!</h1>',
            drag: 'Drag a 😺 GIF or GTFO'
          }" @change="onChange">
        </picture-input>
      </div>
    </form>
</div></template>
  
<script>
import dblib from '@/dblib';
import PopupBox from '@/components/PopupBox.vue';
import PictureInput from 'vue-picture-input'
import axios from 'axios';


export default {
  components: {
    PopupBox,
    PictureInput
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

        
        const formData = new FormData()
        formData.append('box_uid', this.box_id)
        formData.append('title', this.title)
        formData.append('description', this.description)
        formData.append('image', this.$refs.pictureInput.file)
        console.log(formData)
        axios.post('http://127.0.0.1:8000/api/v1/create-product/', formData, {headers: {'Sec-Fetch-Site': 'same-origin'}})
        // await this.createProduct({
        //   box_uid: this.box_id,
        //   title: this.title,
        //   description: this.description,
        //   get_image: this.$refs.pictureInput.file,
        // });
        // this.$router.push({ path: `/login` });

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

    onChange(image) {
      console.log('New picture selected!')
      if (image) {
        console.log('Picture loaded.')

        console.log(this.$refs.pictureInput.file)
        // console.log(this.getBase64Image(this.$refs.pictureInput.file))
      } else {
        console.log('FileReader API not supported: use the <form>, Luke!')
      }
    },
    async showPopup(message) {
      // Access the showPopup method of the PopupBox component
      await this.$refs.popupBox.showPopup(message);
    },

    getBase64Image(img) {
      // Create an empty canvas element
      var canvas = document.createElement("canvas");
      canvas.width = img.width;
      canvas.height = img.height;

      // Copy the image contents to the canvas
      var ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0);

      // Get the data-URL formatted image
      // Firefox supports PNG and JPEG. You could check img.src to
      // guess the original format, but be aware the using "image/jpg"
      // will re-encode the image.
      var dataURL = canvas.toDataURL("image/png");

      return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
    }
  },

  async created() {
    // Call getItems when the component is created
    try {
      this.isLoading = true;
      this.box = await this.getFreeBox();
      console.log("Box_num: ", this.box.box_num);
      if (this.box.box_num == -1) {
        await this.showPopup(`There are no available boxes :((`);
        this.$router.push({ path: `/login` });
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
  