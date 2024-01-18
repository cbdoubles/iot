// vue.config.js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    client: {
      overlay: {
        warnings: false,
        errors: false,
        runtimeErrors: false
      },

      // or
      overlay: false,
    }
  }
})