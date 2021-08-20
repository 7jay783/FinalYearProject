<template>
    <div class="container">
        <div class="row border">
			<Header />
			<div class="col-lg-12 col-md-12 col-sm-12 col-12 pt-3 bg-light-green content text-center">
                <h3>Admin Page</h3>
				<div class="row py-5">
					<div class="col-lg-4 col-md-4 col-sm-5 col-12 py-3 border bg-light rounded mx-auto">
						<h5>Unknown Childern</h5> 
						<h3>{{counts.unknown}}</h3>
					</div>
					<div class="col-lg-4 col-md-4 col-sm-5 col-12 py-3 border bg-light rounded mx-auto">
						<h5>Known Childern</h5> 
						<h3>{{counts.known}}</h3>
					</div>
					<div class="col-lg-10 col-md-10 col-sm-10 col-12 my-5 mx-auto bg-light rounded">
						<h5 class="my-4">Select Training Mode</h5>
						<input class="form-check-input" value="unknown" type="radio" id="uc" v-model="t_mode">&nbsp;
						<label class="form-check-label" for="uc">Unknown Children</label> &nbsp; &nbsp;
						<input class="form-check-input" value="known" type="radio" id="kc" v-model="t_mode">&nbsp;
						<label class="form-check-label" for="kc">Known Children</label>
						<div class="my-4">
							<button class="btn btn-md btn-primary px-5 py-2" @click="train" :disabled="training">{{training ? '..Training..' : 'Train Model'}}</button>
						</div>
					</div>
				</div>
            </div>
		</div>
    </div>
</template>

<script>

import axios from 'axios'
import 'bootstrap'

import Header from '@/components/Header.vue'

export default {
    name: 'Admin',
    components: {Header},
    data(){
        return {
            api: axios.create({baseURL: this.API_BASE_URL}),
			counts: {},
			training: false,
			t_mode: 'unknown'
        }
    },
    methods: {
        get_counts(){
			this.api.get('/children-counts').then(res => {
				this.counts = res.data
			}).catch(err => {
				console.log(err)
				this.get_counts()
			})
		},
		train(){
			this.training = true
			this.api.post(`/train/${this.t_mode}`).then(res => {
				alert(res.data.msg)
			}).catch(err => {
				alert(err)
			}).finally(() => {
				this.training = false
			})
		}
    },
	created(){
		this.get_counts()
	}
}
</script>

<style scoped>
	/* div.tile{
		min-height: 8rem;
	} */
    div.content{
        min-height: 33rem;
    }
</style>
