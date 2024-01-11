<template>
  <div class="product-card">

    <!-- <div class="badge">Hot</div> -->
    <div class="product-tumb" @click="$emit('viewItem')">
      <img :src="this.image" alt="">
    </div>
    <div class="product-details">
      <!-- Categories -->
      <!-- <span class="product-catagory">Women,bag</span> -->
      <h4><a @click="$emit('viewItem')"> {{ this.product }} </a></h4>
      <p>{{ this.description }}</p>
      <div class="product-bottom-details">
        <!-- Price part of product card, can be used when implementing credits. -->
        <!-- <small>$96.00</small> to put a discount -->
        <!-- <div class="product-price">{{ this.price }}</div> -->
        <div class="product-links">
          <div class="row">
            <!-- Replace with hearth icon if we decide to implement favourites -->
            <!-- <router-link to="/item" class="column">
              <img src="../assets/shopping-cart-svgrepo-com.svg" alt="Shopping cart" class="icon"/>
            </router-link> -->
            <div @click="$emit('viewItem')" class="column">
              <img src="../assets/shopping-cart-svgrepo-com.svg" alt="Shopping cart" class="icon" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- <div class="Card">
    <div>
      <img :src="this.image" class="image">
      <h1> {{ product }}</h1>
    </div>
  </div> -->
</template>





<script>

export default {
  name: 'ProductCard',


  props: ['pid', 'product', 'image', 'description'],

}
</script>


<style scoped>

.row {
  display: flex;
  margin-left: 100px;
}

/* Create three equal columns that sits next to each other */
.column {
  flex: 100%;
}

@import url('https://fonts.googleapis.com/css?family=Roboto:400,500,700');

* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}


body {
  font-family: 'Roboto', sans-serif;
}

a {
  text-decoration: none;
}

.product-card {
  width: 100%;
  position: relative;
  box-shadow: 0 2px 7px #a0a0a0;
  margin: 10px auto;
  background: #eeeeee;
  border-radius: 5%;
}

.badge {
  position: absolute;
  left: 0;
  top: 20px;
  text-transform: uppercase;
  font-size: 13px;
  font-weight: 700;
  background: red;
  color: #fff;
  padding: 3px 10px;
}

.icon {
  max-width: 100%;
  max-height: 100%;
}

.product-tumb {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 225px;
  background: #f0f0f0;
  border-radius: 2%;
  cursor: pointer;
}

.product-tumb img {
  max-width: 100%;
  max-height: 100%;
  border-radius: 5%;
}

.product-details {
  padding: 30px;
}

.product-catagory {
  display: block;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  color: #ccc;
  margin-bottom: 18px;
}

.product-details h4 a {
  font-weight: 500;
  display: block;
  margin-bottom: 18px;
  text-transform: uppercase;
  color: #363636;
  text-decoration: none;
  transition: 0.3s;
}

.product-details h4 a:hover {
  color: #fbb72c;
}

.product-details p {
  font-size: 15px;
  line-height: 22px;
  margin-bottom: 18px;
  color: #999;
  overflow: hidden;
}

.product-bottom-details {
  overflow: hidden;
  border-top: 1px solid #b4b3b3;
  padding-top: 20px;
}

.product-bottom-details div {
  float: left;
  width: 50%;
}

.product-price {
  font-size: 18px;
  color: #fbb72c;
  font-weight: 600;
}

.product-price small {
  font-size: 80%;
  font-weight: 400;
  text-decoration: line-through;
  display: inline-block;
  margin-right: 5px;
}

.product-links {
  text-align: right;
}

.product-links router-link {
  display: inline-block;
  margin-left: 5px;
  color: #e1e1e1;
  transition: 0.3s;
  font-size: 17px;
}

.product-links a:hover {
  color: #fbb72c;
}
</style>