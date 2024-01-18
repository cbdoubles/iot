<template>
  <div class="flex">

    <ModalItem header="Scan RFID" :image="loadingImage" v-if="isLoading" @close="this.abort()"> </ModalItem>

    <router-link to="/donate" class="button"> Donate</router-link>

    <!-- <div class="button" @click="this.login(), this.isLoading = true">
      Login
    </div> -->
    <div class="button" @click="this.login(this.controller), this.isLoading = true">
      Login
    </div>


  </div>
</template>

<script>
import dblib from '../dblib'
import ModalItem from '@/components/ModalItem.vue'

export default {

  data() {
    return {
      isLoading: false,
      request: null,
    }
  },

  methods: {
    invalidUser() {
      console.log("Invalid")
    },
    async abort() {
      this.controller.abort()
      this.$router.go()
    },
  },

  components: {
    ModalItem
  },
  computed: {
    loadingImage() {
      return require('@/assets/loading.gif')
    },
    controller() {
      return new AbortController();
    }
  },
  mixins: [dblib]


}

</script>



<style scoped>
.flex {
  display: flex;
  justify-content: center;
}

.flex-item+.flex-item,
.button {
  margin-left: 10px;
}

.button {
  margin-top: 15px;
  background-color: #0066FF;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  padding-left: 35%;
  padding-bottom: 60%;
}
</style>../dblib