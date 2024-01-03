import axios from 'axios'
const dblib = {

  data() {
    return {
      isLoading: false,
      rfid: -1,
      arduino: 'http://192.168.178.157',
      database: 'localhost:####',
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
      axios.get(this.database + '/users?' + this.rfid)
        .then(response => {
          if (response.data) {
            this.$router.push('/browse')
          } else {
            console.log('invalid uuid.')
          }
        })
        .catch(error => {
          this.isLoading = false
          console.log(error)
        })
    },
  },

  // Get items from the database, store them in
  // products.
  async getItems() {
    this.isLoading = true
    axios.get(this.database + '/items')
      .then(response => response.json())
      .then(json => {
        this.products = json
      })
      .catch(error => {
        console.log(error)
      })
    this.isLoading = false
  },

  // get a singular product from the database
  async getProduct(pid) {
    this.isLoading = true
    axios.get(this.database + '/items?' + pid)
      .then(response => response.json())
      .then(json => this.product = json.data)
      .catch(error => {
        console.log(error)
      })
      this.isLoading = false
      return {pid: 1, product: 'tshirt', image: 'https://picsum.photos/200', description: 'This is a description that is way too'}
  }
}

export default dblib