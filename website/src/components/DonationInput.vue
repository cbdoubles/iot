<template>
  <div>
    <PopupBox ref="popupBox" />

    <form id="donationForm" @submit.prevent="console.log(form)">
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="title" />

      <label for="description">Description:</label>
      <textarea id="description" v-model="description"></textarea>

      <button @click="submitForm">Submit</button>

      <div class="hello">
        <picture-input ref="pictureInput" width="600" height="600" margin="16" accept="image/jpeg, image/jpg" size="10"
          button-class="btn" :custom-strings="{
            upload: '<h1>Your device does not support file uploading.</h1>',
            drag: 'Drag an image or <br>click here to select a file'
          }" @change="onChange">
        </picture-input>
      </div>
    </form>
  </div>
</template>
  
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
      defaultImg: require('@/assets/No-image.jpeg')
    };
  },
  mixins: [dblib],

  methods: {
    async submitForm() {
      try {

        const formData = new FormData()
        console.log("making form")
        console.log(this.get_image)
        formData.append('box_uid', this.box_id)
        formData.append('title', this.title)
        formData.append('description', this.description)
        if (this.$refs.pictureInput.file == null) {
          formData.append('image',
            await fetch(this.defaultImg)
              .then(response => response.blob())
              .then(blob => new File([blob], "default.jpeg"))
          )
        } else {
          formData.append('image', this.$refs.pictureInput.file)
        }

        console.log(formData)
        axios.post('http://127.0.0.1:8000/api/v1/create-product/', formData)
          .then(
          await this.sendBoxNumber(this.box_number),
          await this.showPopup(`Go to Box ${this.box_number} to donate your item. Thank you!`))
        // await this.createProduct({
        //   box_uid: this.box_id,
        //   title: this.title,
        //   description: this.description,
        //   get_image: this.$refs.pictureInput.file,
        // });
        this.$router.push({ path: `/login` });

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
        console.log('Picture loaded.');
        this.get_image = this.$refs.pictureInput.file;

        console.log(this.$refs.pictureInput.file);
        // console.log(this.getBase64Image(this.$refs.pictureInput.file))
      } else {
        console.log('FileReader API not supported: use the <form>, Luke!')
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
  