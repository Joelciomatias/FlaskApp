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

import io from 'socket.io-client';


this.$socket.subscribe('join_room', (data) => {
    this.msg = data.message;
});

export default {
  name: 'HelloWorld',
  sockets: {
        connect: function () {
            console.log('socket connected')
        },
        customEmit: function (data) {
            console.log('this method was fired by the socket server. eg: io.emit("customEmit", data)')
        }
    },
  data() {
      return {
        items: []       
      }
  },
  beforeMount(){
    this.getData()
 },
 mounted(){
   this.$socket.emit('create', {})
 },
 methods:{
 clickButton: function (data) {
            // $socket is socket.io-client instance
            this.$socket.emit('emit_method', data)
        },
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
