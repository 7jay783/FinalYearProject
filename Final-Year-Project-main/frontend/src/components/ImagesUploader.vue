<template>
    <div class="row border border-info rounded">
        <div class="col-lg-12 col-md-12 col-sm-12 col-12 py-2 my-2 text-center">
            <h3 class="my-3">Upload Images</h3>
            <input type="file" class="btn btn-dark px-1" multiple="true" accept=".jpg,.jpeg,.png" @change="images_loader($event.target.files)" v-if="images_content.length===0">
            <button class="btn btn-sm px-3 border border-dark float-end" @click="clear_images" v-else>X</button> <br>
            <img v-for="(img,i) in images_content" :src="img" alt="" :key="i" height="150" class="m-2">
        </div>
        <div class="col-lg-12 col-md-12 col-sm-12 col-12 my-2 py-2 text-center" v-if="images_content.length!==0">
            <button class="btn btn-md btn-primary" @click="upload_images" :disabled="upload_response!==null || processing">{{processing ? 'uploading' : (upload_response!==null) ? 'uploaded' : 'upload'}}</button>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ImagesUploader',
    props: ['api', 'allowed_types', 'upload_url'],
    emits: ['uploadResponse'],
    components: {},
    data(){
        return {
            processing: false,
            images: new FormData,
            images_content: [],
            upload_response: null
        }
    },
    methods: {
        clear_images(){
            this.delete_images()
            this.images = new FormData
            this.images_content = []
            this.upload_response = null
        },
        images_loader(files){
            this.clear_images()
            files.forEach(async (file) => {
                if(this.allowed_types.includes(file.type))
                {
                    this.images.append('images', file)
                    const reader = new FileReader()
                    reader.onload = () => {this.images_content.push(reader.result)}
                    reader.readAsDataURL(file)
                }
            })
        },
        upload_images(){
            this.processing = true
            this.api.post(this.upload_url, this.images).then(res => {
                this.upload_response = res.data
            }).catch(err => {
                console.log(err)
            }).finally(() => {
                this.processing = false
            })
        },
        delete_images(){
            if(this.upload_response!==null)
            {
                this.processing = true
                this.api.get(`/delete-uploaded-images/${this.upload_response.upload_id}`).then(res => {
                    console.log(res.data)
                }).catch(err => {
                    console.log(err)
                }).finally(() => {
                    this.processing = false
                })
            }   
        }
    },
    watch: {
        upload_response(response){
            this.$emit('uploadResponse', response)
            // console.log(response)
        }
    }
}
</script>

