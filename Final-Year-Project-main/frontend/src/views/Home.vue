<template>
    <div class="container">
        <div class="row border">
            <Header />
            <div class="col-lg-12 col-md-12 col-sm-12 col-12 pt-5 bg-light-green">
                <nav class="nav nav-pills nav-justified nav-fill my-2">
                    <a class="nav-link me-1 border border-warning border-3 active" id="nav-missing-child-tab" data-bs-toggle="tab" href="#nav-missing-child" role="tab" aria-controls="nav-missing-child" aria-selected="true">
                        Looking For A Missing Child ?
                    </a>
                    <a class="nav-link ms-1 border border-warning border-3" id="nav-unknow-child-tab" data-bs-toggle="tab" href="#nav-unknow-child" role="tab" aria-controls="nav-unknow-child" aria-selected="false">
                        Have An Unknown Child ?
                    </a>
                </nav>
                <div class="tab-content my-2 p-3 border border-primary rounded">
                    <MissingChildFinder :api="api" :allowes_images_type="allowes_images_type" />
                    <UnknownChildFinder :api="api" :allowes_images_type="allowes_images_type" />
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>

import axios from 'axios'
import 'bootstrap'

import Header from '@/components/Header.vue'

import MissingChildFinder from '@/components/MissingChildFinder.vue'
import UnknownChildFinder from '@/components/UnknownChildFinder.vue'


export default {
    name: 'Home',
    components: {Header, MissingChildFinder,UnknownChildFinder},
    data(){
        return {
            api: axios.create({baseURL: this.API_BASE_URL}),
            allowes_images_type: ['image/png', 'image/jpg', 'image/jpeg']
        }
    },
    methods: {
        
    }
}
</script>

<style>
    .bg-light-green{
        background: #4dff7d;
    }
</style>

<style scoped>
    a.nav-link{
        color: black;
        font-size: 1rem;
        font-weight: 500;
    }
    div.tab-content{
        min-height: 50rem;
    }
</style>
