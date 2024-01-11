<template>
    <div class="backdrop" @click="close">
        <div class="modal">
            <img :src="image" v-if="this.image">
            <h1> {{ header }} </h1>
        </div>
    </div>
</template>

<script>
export default{
    data() {
        return {
            
        }
    },

    props: ['image', 'header'],

    methods: {
        close() {
            this.$emit('close')
        }
    }
}

</script>

<style scoped>
    .modal{
        width: 400px;
        padding: 20px;
        margin: 100px auto;
        background: white;
        border-radius: 10px;
        text-align: center;
    }

    img{
    width: 100%;
    height:100%
    }
    .backdrop {
        top: 0;
        position: fixed;
        background: rgba(0,0,0,0.5);
        width: 105%;
        height: 105%;
    }
</style>