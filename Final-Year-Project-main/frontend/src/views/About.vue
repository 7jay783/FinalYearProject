<template>
    <div class="container">
        <div class="row border">
			<Header />
			<div class="col-lg-12 col-md-12 col-sm-12 col-12 pt-3 bg-light-green content text-center">
                <h3>About Page</h3>
				<div class="row py-5">
					<div class="col-lg-10 col-md-10 col-sm-10 col-12 my-2 py-3 mx-auto bg-light rounded">
						<h2>HUMAN FACE DETECTION AND RECOGNITION</h2>
						<h4>Final Year Project</h4>
						<h6>
							( INFORMATION TECHNOLOGY ) <br><br>
							by <br><br>
							Jay Prakash (1805213906) <br>
							Mohin Ahmad (1705213023) <br>
							Mohd Khalid (1805213908) <br><br><br>
						</h6>
						<h4>Under the guidance of <br><br></h4>
						<h5>
							Dr. Y. N. Singh <br><br>
							Ms. Sameeksha Tandon
						</h5>
					</div>
				</div>
            </div>
		</div>
    </div>
</template>

<script>


import Header from '@/components/Header.vue'

export default {
    name: 'About',
    components: {Header},
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
