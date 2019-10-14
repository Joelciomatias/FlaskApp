/* eslint-disable */
<template>
  <div class="hello">
<h2>Test python results</h2>
<span>Número de tarefas na fila: {{ reserved }} </span><br/>
  <span>Número de tarefas executanto: {{ item }} </span><br/>

  <span>Tarefa mais antiga iniciada à {{ first }} segundos </span><br/>
  <span>Tarefa mais recente iniciada à {{ last }} segundos </span>
  <br>
  <button id="add" v-on:click="clickButton">Adicionar Tarefa</button>
  <input type="number" id="iterations" value="1" max="100"/>
  <div>
      <b-table striped hover :items="items"></b-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import io from 'socket.io-client';

export default {
  name: 'HelloWorld',
  sockets: {
        connect: function () {
          console.log('socket connected')
          var that = this
          this.sockets.subscribe('active', (data) => {
            //console.log('active',data['active'])
            //console.log('reserved',data['reserved'])
              //  console.log('registered',data['registered'])
            //this.getValue(data['active'].length)
            that.item = data['active'].length
            that.reserved = data['reserved'].length
            data['active'] = data['active'].sort((a, b) => (a.time_start > b.time_start) ? 1 : -1)
            if( data['active'].length>0){
              let first = new Date(data['active'][0].time_start * 1000)
              let last =  new Date(data['active'][data['active'].length -1].time_start * 1000)
              let now = new Date()
              this.first = parseInt((now.getTime() - first.getTime()) / 1000);
              this.last = parseInt((now.getTime() - last.getTime()) / 1000);
            } else {
              this.last = 0
              this.first =0
            }
          });
        },
        customEmit: function (data) {
            console.log('this method was fired by the socket server. eg: io.emit("customEmit", data)')
        }
    },
  data() {
      return {
        items: [],
        item:0,
        reserved:0,
        first:0,
        last:0
      }
  },
  beforeMount(){
    this.getData()
 },
 mounted(){
   this.$socket.emit('create',{})

   this.$socket.on('join_room',()=>{
     console.log('received join room')
   })
 },
 methods:{
  getValue: function(value){  
      return  value
  },
 clickButton: function (data) {
        let random =  Math.floor(Math.random() * 10); 
        random = random < 1 ? 1 : random
         let value = document.querySelector("input[id=iterations]").value
        document.querySelector("input[id=iterations]").value = random
         console.log(value,random)
          axios.get(`http://localhost:5000/test-python/${value}`)
          .then(response => {
          })
          .catch(e => {
            this.errors.push(e)
          })
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
