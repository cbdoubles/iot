<template>
  <div class="flex">

    <router-link to="/donate" class="button"> Donate</router-link>

    <div class="button" @click="login">
      Login
    </div>
    <router-link to="/browse" class="button"> Browse (used for dev, delete when using login)</router-link>


  </div>
</template>

<script>
import dblib from '../dblib'

export default {

  methods: {
    
    invalidUser() {
      console.log("Invalid")
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
  padding-left: 25%;
  padding-bottom: 35%;
}
</style>../dblib