<template>
    <div class="body">


          
         
     

       

       



              
            <div>
             <h1 v-if="parseInt(BPM_data)<100" style="color:green">Heart rate data: {{BPM_data}} beats per minute</h1> 
             <h1 v-else style="color:red">Heart rate data: {{BPM_data}} beats per minute</h1> 
             <button v-on:click="BPM">Aquire BPM data</button>
            </div>   

            <div>
             <h1 >Blood pressure data: {{blood_pressure_data}}/{{blood_pressure_data}} mmHg</h1> 
             <button v-on:click="blood_pressure">Aquire blood pressure data</button>
            </div>   

    

            <div>
             <button @click="stopfunc">Stop</button>
            </div>   
                   
      

          
                 
      
    

                        

       










   

 

    
        <!-- <h2>{{$nuxt.$fire.auth.currentUser.email}}</h2> -->

    </div>
</template>

<script>

// import Vue from 'vue'
// import BackToTop from 'vue-backtotop'

// Vue.use(BackToTop)

    export default {
 
      data() {
    return {
      scrollTop: null,
      isVisible: false,
      visibleDistance: 200,
      showHeader: true,
      lastScrollPosition: 0,
      BPM_data:"0",
      blood_pressure_data:"0",
      connection:null,
      stop:false,
      aa:false,
      bb:false

    }
  },      
    


  mounted(){

    this.connectionBPM = new WebSocket("ws://localhost:8000/bpm");
    this.connectionBPM.onopen = () => console.log("connectionBPM established");
  },

  methods: {


    BPM(){
      // this.connectionBPM = new WebSocket("ws://localhost:8000/bpm");
      // this.connectionBPM.onopen = () => console.log("connectionBPM established");
      // this.connectionBPM.send(JSON.stringify({"data":"start"}))
      var a = this //this is not the same inside an arrow function
      this.aa = true
      this.connectionBPM.onmessage = (event) => {

        // console.log(event)
        console.log(JSON.parse(event.data)["value"])
        console.log(JSON.parse(event.data)["topic"])
        // console.log(event.data.HEj)
        if(JSON.parse(event.data)["topic"] == "mqtt"){
          
          a.BPM_data = JSON.parse(event.data)["value"]

        }
        else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
         a.blood_pressure_data = JSON.parse(event.data)["value"]

        }

    }
  },

    blood_pressure(){
      this.bb = true
      var a = this //this is not the same inside an arrow function
      this.connectionBPM.onmessage = (event) => {

        // console.log(event)
        console.log(JSON.parse(event.data)["value"])
        console.log(JSON.parse(event.data)["topic"])
        // console.log(event.data.HEj)
        if(JSON.parse(event.data)["topic"] == "mqtt2"){
          
          a.blood_pressure_data = JSON.parse(event.data)["value"]

        }
        else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
         a.BPM_data = JSON.parse(event.data)["value"]

        }

    }
    

  
    
    },

    stopfunc(){

      this.stop = true
      // console.log("Stiop")
      // this.connection.send(JSON.stringify({"data":"stop"}))
      this.connection.close()
   
      this.connection.onclose = () => console.log("connection closed");
    }


    // Toggle if navigation is shown or hidden

  },
        
    }
</script>

<style lang="scss">

@import url('https://fonts.googleapis.com/css2?family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@700&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@300;700&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@300;700&family=Montserrat:wght@500&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap');
/* font-family: 'Anton', sans-serif;
font-family: 'Lato', sans-serif;
font-family: 'Poppins', sans-serif;
font-family: 'Rubik Mono One', sans-serif; */





</style>