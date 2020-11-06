<template>
  <div id="app">
    <h1>Welcome to our prototype!</h1>
    <form action='http://localhost:4000/?name=' method='get' id='searchFor'>
      <label for="name">Restaurant Name</label><br>
      <input type="text" id="name" name="name" v-model="name"><br>
      <button type="button" v-on:click="submit">Search</button>
    </form>
    <table style="width:100%">
      <tr>
        <th>Ranking</th>
        <th>Business Name</th>
        <th>Location</th>
        <th>Rating</th>
        <th>Phone Number</th>
      </tr>
      <tr>
        <th id='ranking1'></th>
        <th id='name1'></th>
        <th id='location1'></th>
        <th id='rating1'></th>
        <th id='phonenumber1'></th>
      </tr>
      <tr>
        <th id='ranking2'></th>
        <th id='name2'></th>
        <th id='location2'></th>
        <th id='rating2'></th>
        <th id='phonenumber2'></th>
      </tr>
      <tr>
        <th id='ranking3'></th>
        <th id='name3'></th>
        <th id='location3'></th>
        <th id='rating3'></th>
        <th id='phonenumber3'></th>
      </tr>
    </table>
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data(){return{name:''}},
  methods: {submit:function(){
    // console.log(this.name)
    axios.get('http://localhost:4000/', { params: { name: this.name } }).then(response=>{
      console.log(response)
      for (let i=0; i<response.data.businesses.length; i++){
        if (i==3) {
          break
        }
        document.getElementById('ranking'+(i+1)).innerHTML=i+1
        document.getElementById('name'+(i+1)).innerHTML=response.data.businesses[i]['name']
        document.getElementById('location'+(i+1)).innerHTML=response.data.businesses[i]['location']["address1"]
        document.getElementById('rating'+(i+1)).innerHTML=response.data.businesses[i]['rating']
        document.getElementById('phonenumber'+(i+1)).innerHTML=response.data.businesses[i]['phone']
        
      }
    })
  }}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
