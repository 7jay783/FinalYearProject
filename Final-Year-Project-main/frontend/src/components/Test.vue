<template>
  <div class="hello">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>{{ msg }}</h1>
    <p>
      <a href="https://cli.vuejs.org" target="_blank">vue-cli documentation</a>
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li>babel</li>
      <li>pwa</li>
      <li>router</li>
      <li>eslint</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Test',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
