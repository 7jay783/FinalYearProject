<template>
  <router-view/>
</template>

<script>
export default {
  watch: {
    '$route' (to) {
      document.title = to.meta.title || 'Face Recognizer' //default title
    }
  }
}
</script>


<style>

</style>
