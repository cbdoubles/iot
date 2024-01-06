

<template>
    <template v-if="isLoading">
        <img :src=loadingImage style="max-width: 40%;">
    </template>

    <template v-else>
        <div class="grid-container">
            <div v-for="(item) in products" :key="item.box_id">
                <ProductCard 
                :pid="item.box_id"
                :box_num="item.box_num"
                :product="item.title"
                :description="item.description"
                :image="item.get_image"
                :thumbnail="item.get_thumbnail"
                @viewItem="viewProduct(item)" />
            </div>
        </div>
    </template>
</template>


    

<script>
import ProductCard from '@/components/ProductCard.vue'
import dblib from '@/dblib'

export default {
    name: 'ShopView',
    components: {
        ProductCard
    },

    data() {
        return {
            isLoading: false,
            products:[],
        }
    },
    mixins: [dblib],

    methods: {
        viewProduct(item) {
            console.log('print in shopview');
            console.log(item.box_id);
            this.$router.push({path: `/item/${item.box_id}`, query: {pid: item.box_id}})
        }
    },
    computed: {
        loadingImage() {
            return require('@/assets/loading.gif')
        }
    },

    async created() {
    // Call getItems when the component is created
        this.getItems();
  }

    
}
</script>
    
<style scoped>
.grid-container {
    display: grid;
    margin-left: 5%;
    gap: 40px;
    grid-template-columns: repeat(auto-fill, 208px);
}
</style>