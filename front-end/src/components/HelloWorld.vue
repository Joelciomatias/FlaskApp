/* eslint-disable */
<template>
  <div class="hello">
<h2>Test python results</h2>
  <div>
      <b-table striped hover :items="items"></b-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data() {
      return {
        items: []       
      }
  },
  beforeMount(){
    this.getData()
 },
 methods:{

   getData() {
     axios.get(`http://localhost:5000/finished`)
    .then(response => {
      // JSON responses are automatically parsed.
      let result = []
      response.data.result.forEach(element => {
        result.push({
          'Id':element.id,
          'Interations':element.iterations,
          'Sum':element.sum,
          'Start':element.start,
          'End':element.end,
        })
      });
      this.items = result
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
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
