<template>
    <div class="row border border-info rounded">
        <div class="col-lg-12 col-md-12 col-sm-12 col-12 my-2 text-center">
            <h3 class="my-3">{{Object.keys(search_results).length ? 'Available Matches' : 'No Matches Found'}} </h3>
        </div>
        <div v-for="(result,i) in search_results" :key="i" class="col-lg-12 col-md-12 col-sm-12 col-12 py-2 my-2 mx-auto text-center">
			<div class="card">
				<div class="card-header">
					Match Number {{i+1}}
				</div>
				<div class="card-body">
					<div class="row my-2">
                        <div class="col-lg-6 col-md-8 col-sm-10 col-12 mx-auto">
                            <table class="table table-responsive table-bordered">
                                <thead>
                                    <tr>
                                        <th colspan="2">Child Information</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <th>type</th> <td>{{result.type}}</td>
                                    </tr>
                                    <tr v-if="result.info.name">
                                        <th>name</th><td>{{result.info.name}}</td>
                                    </tr>
                                    <tr>
                                        <th>{{result.type=='known' ? 'address': 'last location'}}</th><td>{{result.info.address}}</td>
                                    </tr>
                                    <tr>
                                        <th>Contact Person Email</th><td>{{result.info.contact_email}}</td>
                                    </tr>
                                    <tr>
                                        <th>Contact Person Phone</th><td>{{result.info.contact_mobile}}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="row my-2">
                        <h5 class="card-title">Other Available Images</h5>
                        <div class="col-lg-2 col-md-3 col-sm-4 col-6" v-for="(img,i) in result.images" :key="i">
                            <img class="similar-img my-1" :src="`${API_BASE_URL}/img/children/${result._id}/${img}`" :alt="img" height="100">
                        </div>
                    </div>
				</div>
			</div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'SearchResultViewer',
    props: ['search_results'],
    components: {},
    data(){
        return {
            processing: false
        }
    },
    methods: {

    }
}
</script>

<style scoped>
    .similar-img{
        max-height: 150px;
    }
</style>