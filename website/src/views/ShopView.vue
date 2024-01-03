

<template>
    <template v-if="isLoading">
        <img :src=loadingImage style="max-width: 40%;">
    </template>

    <template v-else>
        <div class="grid-container">
            <div v-for="(item) in products" :key="item.pid">
                <ProductCard 
                :product="item.product"
                :image="item.image"
                :description="item.description"
                :pid="item.pid"
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
            products: [ 
            {pid: 1, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description that is way too looooooooooooooooooooooooooooooooooooooooooong!'},
            {pid: 2, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 3, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 4, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 5, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 6, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 7, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'}, 
            {pid: 8, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 9, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 10, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 11, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
            {pid: 12, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description!'},
        ],
        }
    },
    mixins: [dblib],

    methods: {
        viewProduct(item) {
            this.$router.push({path: '/item', query: {pid: item.pid}})
        }
    },
    computed: {
        loadingImage() {
            return require('@/assets/loading.gif')
        }
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