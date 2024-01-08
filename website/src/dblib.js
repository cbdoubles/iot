import axios from 'axios'
const dblib = {

  data() {
    return {
      isLoading: false,
      rfid: -1,
      arduino: 'http://192.168.178.157',
      database: 'http://127.0.0.1:8000',
      // database: 'localhost:####',
      products: [],
    }
  },

  methods: {
    async login() {
      this.isLoading = true
      this.rfid = -1
      console.log('getting RFID')
      this.scanRFID()
      console.log('checking uuid')
      this.verifyLogin()
      this.isLoading = false
    },


    // Waits for the arduino to send a uuid.
    // currently it will not time out or anything.
    async scanRFID() {
      axios.get(this.arduino + '/rfid')
        .then(response => { this.rfid = response })
        .catch(error => {
          this.isLoading = false
          console.log(error)
        })
    },

    // Checks the uuid gotten from the arduino against database.
    // if valid user, go to the browse page.
    async verifyLogin() {
      axios.get(this.database + '/api/v1/verify-login/', {nfc_id: this.rfid})
        .then(response => {
          if (response.data) {
            this.$router.push('/browse')
          } else {
            console.log('invalid uuid.')
            // pop
            this.$router.push('/login')
          }
        })
        .catch(error => {
          this.isLoading = false
          console.log(error)
        })
    },

  // Get items from the database, store them in products.
    async getItems() {
      this.isLoading = true;
    
      try {
        const response = await axios.get(this.database + '/api/v1/latest-products/');
        this.products = response.data;
      } catch (error) {
        console.error('Error fetching items:', error);
      } finally {
        this.isLoading = false;
      }
    },
  
    // get a singular product from the database
    async getProduct(pid) {
      try {
        this.isLoading = true;
    
        const response = await axios.get(`${this.database}/api/v1/boxes/product/${pid}`);
        this.product = response.data;
    
        return response.data;  // Return the data received from the endpoint
      } catch (error) {
        console.error('Error fetching product:', error);
        // return {pid: 1, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description that is way too'};
      } finally {
        this.isLoading = false;
      }
    },

    async getFreeBox() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${this.database}/api/v1/check-free-box/`);
        this.box = response.data;
        return response.data;  // Return the data received from the endpoint
      } catch (error) {
        console.error('Error fetching product:', error);
        // return {pid: 1, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description that is way too'};
      } finally {
        this.isLoading = false;
      }
    },

    async createProduct(product) {
      // const productId = product.pid;  // Assuming you have an 'id' property in your product data
      try {
        // Make an API request to submit the data
        const response = await axios.post(`${this.database}/api/v1/create-product/`, {
          box_uid: product.box_uid,
          title: product.title, 
          description: product.description,
          get_image: product.get_image,
        });
        console.log(response.data.message);  // Log the server response
          // Optionally, you can perform additional actions based on the response
      } catch (error) {
          console.error('Error deleting product:', error);
          // Optionally, you can handle the error, show a message, etc.
      }
    },
    
    async deleteProduct(product) {
      // const productId = product.pid;  // Assuming you have an 'id' property in your product data
      try {
        const response = await axios.post(`${this.database}/api/v1/delete-product/`, { box_id: product.box_id });
        console.log(response.data.message);  // Log the server response
          // Optionally, you can perform additional actions based on the response
      } catch (error) {
          console.error('Error deleting product:', error);
          // Optionally, you can handle the error, show a message, etc.
      }
    },

  },
}

export default dblib