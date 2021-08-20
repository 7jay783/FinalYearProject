const fs = require('fs')
const path = require('path')

module.exports = {
    devServer: {
        // Fixing issue with WDS disconnected and sockjs network error on vm
        host: '0.0.0.0',
        port: 7150,
        public: 'linux.vm:7150',
        disableHostCheck: true,
        // End of fix
        //if hot reload not working
        // watchOptions: {
        //     poll: true
        // },
        //end
        // https - remove if you don't have certificates
        https: {
            key: fs.readFileSync(`${process.env.HOME}/.certs/linux.vm/key.pem`),
            cert: fs.readFileSync(`${process.env.HOME}/.certs/linux.vm/cert.pem`),
            ca: fs.readFileSync(`${process.env.HOME}/.certs/linux.vm/ca.pem`),
        }, //end
    },
    productionSourceMap: false,
    outputDir: path.resolve(__dirname, '../app/www'),
    // pwa setup
    pwa: {
        name: 'Face Recognizer',
        workboxOptions: {
            exclude: [/\.map$/],
        }
    }, //end
    
    
}