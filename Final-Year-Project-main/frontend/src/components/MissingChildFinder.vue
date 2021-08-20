<template>
	<div class="tab-pane fade show active" id="nav-missing-child" role="tabpanel" aria-labelledby="nav-missing-child-tab">
		<ImagesUploader :api="api" :allowed_types="images_upload.types" :upload_url="images_upload.url" @upload-response="get_uploader_response" />
		<div class="row" v-if="images_upload.response!==null">
			<div class="col-lg-12 col-md-12 col-sm-12 col-12 py-2 my-2 border border-warning text-center rounded">
				<button @click="search_for_matches('in_unknowns')" class="btn btn-md" :class="search.processing ? 'btn-warning' : 'btn-success'" :disabled="search.processing">
					{{search.processing ? '...Matching...' : 'Search For Matches'}}
				</button>
			</div>
		</div>
		<SearchResultViewer :search_results="search.results" v-if="search.results!==null" />
		<div class="row my-2 rounded border border-info" v-if="search.results!==null"> <!--  v-if="search.results!==null" -->
			<div class="col-lg-12 col-md-12 col-sm-12 col-12 py-2 my-2 mx-auto text-center">
				<form class="row form" @submit.prevent="save_for_processing($event.target, 'known')">
					<h4>Doesn't Find Appropriate Match?</h4>
					<h6>Save Images For Future Processing</h6>
					<div class="col-lg-6 col-md-8 col-sm-10 col-12 mx-auto">
						<input type="text" class="form-control my-3" name="name" minlength="3" placeholder="child name">
						<input type="text" class="form-control my-3" name="address" minlength="10" placeholder="child address">
						<input type="email" class="form-control my-3" name="contact_email" placeholder="contact person email">
						<input type="tel" class="form-control my-3" name="contact_mobile" placeholder="contact person mobile ex. +919234567890" pattern="(\+\d{1,3})?\d{10}">
						<button type="submit" class="btn btn-md btn-success" :disabled="saving">{{saving ? 'submitting' : 'submit now'}}</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>

import ImagesUploader from '@/components/ImagesUploader.vue'
import SearchResultViewer from '@/components/SearchResultViewer.vue'

export default {
	name: 'MissingChildFinder',
	components: {ImagesUploader, SearchResultViewer},
	props: ['api','allowes_images_type'],
	data(){
		return {
			images_upload: {
                types:  ['image/png', 'image/jpg', 'image/jpeg'],
                url: '/upload-images',
                response: null
            },
            search: {
                processing: false,
                results: null
            },
            saving: false
		}
	},
	methods: {
        get_uploader_response(res){
            this.images_upload.response = res
            this.search.results = null
        },
        search_for_matches(mode){
            if(this.images_upload.response.upload_id)
            {
                this.search.processing = true
                this.api.get(`/search-results/${this.images_upload.response.upload_id}/${mode}`).then(res => {
                    this.search.results = res.data
                    console.log(res.data)
                }).catch(err => {
                    console.log(err)
                }).finally(() => {
                    this.search.processing = false
                })
            }
        },
        save_for_processing(form, type){
            if(this.images_upload.response !== null)
            {
                this.saving = true
                let formjson = Object.fromEntries((new FormData(form)).entries())
                this.api.post(`/save-images/${this.images_upload.response.upload_id}/${type}`, formjson).then(res => {
                    if(res.data.success)
                    {
                        alert('saved successfully')
                    }
                }).catch(err => {
                    console.log(err)
                }).finally(() => {
                    this.saving = false
                })
            }
            else{
                alert('upload image first')
            }
        },
        test(){
            console.log(this.API_BASE_URL)
        }
    }
}
</script>
