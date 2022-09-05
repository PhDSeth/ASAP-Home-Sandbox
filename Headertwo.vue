<template>
    <div class="body">


          
         
     

    


            <div class ="sensors">
            <div >
              <v-alert id = "alertMessage" v-if="fallDetected == true"
            outlined
            :value="alert"
            transition="scale-transition"
            prominent
            type="warning"
            style="width:80%; color:red"
              >
              <h2 style="margin-left:5rem; color:red">Fall detected</h2>
              <v-btn color="rgb(93, 200, 118)" @click="alert = !alert" style="margin-left:4rem">
                I have been notified
              </v-btn>
              </v-alert>


            <div class = "patient-info" style="margin-top:2rem; margin-bottom:2rem;">
              <h2>Patient info: </h2>
              <h2>Name: </h2>
              <h2>Age: </h2>

            </div>
             <h2 v-if="parseInt(BPM_data)<100" style="color:green">Heart rate data: {{BPM_data}} beats per minute</h2> 
             <h2 v-else style="color:red">Heart rate data: {{BPM_data}} beats per minute</h2> 
             <button v-if="toggledBPM == false" v-on:click="BPM" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(93, 200, 118);"  >Collect data</button>
             <button v-else v-on:click="BPM" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(93, 200, 118);">Collecting...</button>
             <button  v-on:click="stopBPM" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(237, 58, 58);">Stop collecting</button>
            </div>   

            <div style="margin-top:2rem">
             <h2 v-if="parseInt(blood_pressure_data)<10" style="color:green">Blood pressure data: {{blood_pressure_data}}/{{blood_pressure_data}} mmHg</h2> 
             <h2 v-else style="color:red">Blood pressure data: {{blood_pressure_data}}/{{blood_pressure_data}} mmHg</h2> 
             <button v-if="toggledPressure == false" v-on:click="bloodPressure" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px;  background-color:rgb(93, 200, 118);"  >Collect data</button>
             <button v-else v-on:click="bloodPressure" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(93, 200, 118);">Collecting...</button>
             <button  v-on:click="stopPressure" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(237, 58, 58);">Stop collecting</button>
            </div>   

            <div style="margin-top:2rem">
              <h2 v-if="parseInt(acceleration_data)<16" style="color:green">Acceleration: {{acceleration_data}} mmHg</h2> 
             <h2 v-else style="color:red">Acceleration: {{acceleration_data}} mmHg</h2>  
             <button v-if="toggledAcceleration == false" v-on:click="acceleration" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px;  background-color:rgb(93, 200, 118);"  >Collect data</button>
             <button v-else v-on:click="acceleration" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(93, 200, 118);">Collecting...</button>
             <button  v-on:click="stopAcceleration" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(237, 58, 58);">Stop collecting</button>
            </div>  

            <div class ="additionaInfo" style="">
              GRAf
        
              <div id="chart">
        <apexchart type="line" height="350" :options="chartOptions" :series="series"></apexchart>
      </div>
            </div>

          </div> 

            <div class ="map-falls">
            <client-only>
                <l-map :zoom=5 :minZoom=4.3 :maxZoom=14 :center="[61.58870,16.974560]" :attributionControl="true"
              >
                <l-tile-layer url='https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png'></l-tile-layer>
                
                <div v-for="item in items.length" :key="item">
                
                <l-marker :lat-lng=items[item-1]> 
                  <l-icon
                    :icon-size="50"
                    :icon-anchor="dynamicAnchor"
                    icon-url="https://www.freeiconspng.com/uploads/-human-male-man-people-person-profile-red-user-icon--icon--23.png"
                    />
                    <l-popup style="color:blue" >
                      <span>Patient: Jakob</span>
                      <br/>
                      <span>Id: 25633</span>
                      <br/>
                      <span>Adress: Stigvägen 3</span>
                      <br/>
                      <span>Telefon: 0782263733</span>
                      <br/>
                    </l-popup>

                </l-marker> -->
                
                </div>
            
                <!-- <l-marker :lat-lng=item> 
                <l-popup style="color:blue" ><span></span></l-popup></l-marker> -->
            </l-map>

   
        
      </client-only>
    </div>
   

                       
      

          
                 
      
    

                        

       










   

 

    
        <!-- <h2>{{$nuxt.$fire.auth.currentUser.email}}</h2> -->

    </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>
<script>
// import Vue from 'vue'
// import BackToTop from 'vue-backtotop'

// Vue.use(BackToTop)

    export default {
 
      data() {
    return {
      items:[],
      // items:[[57.708870,11.974560],[55.9464418,8.1277591],[58.9464418,8.1277591]],
      alert: true,
      BPM_data:"0",
      pressure_data:"0",
      blood_pressure_data:"0",
      acceleration_data:"0",
      connection:null,
      stop:false,
      aa:false,
      bb:false,
      cc:false,
      startSensors: true,
      toggledBPM: false,
      toggledPressure: false,
      toggledAcceleration:false,
      stoppedBPM: false,
      stoppedPressure:false,
      stoppedAcceleration:false,
      fallDetected: false,
      

    }
  },      
  

  mounted(){

    this.connection = new WebSocket("ws://localhost:8000/bpm");
    this.connection.onopen = () => console.log("connectionBPM established");
  },

  watch:{
  
  //watch for falls
fallDetected: function(val){

  if(val == true){
    this.items = [[58.708870,13.974560]]
}
}


},

  methods: {

    createChart(){

      


    },

    isOpen(){

      return this.connection.readyState === this.connection.OPEN

    },

    startStopSensor(){


      // if(this.connection.readyState)
      console.log(this.connection.readyState)

      if(this.startSensors == true){
        this.startSensors = false
        this.connection.send((JSON.stringify({"stop":false})))

        if(!this.isOpen()){
          console.log("EJ ÖPPEN")

        }

        return
      }
      else{

        this.connection.send((JSON.stringify({"stop":true})))
        this.startSensors = true
        this.BPM_data = "0"
        this.acceleration_data = "0"
        this.blood_pressure_data = "0"
        this.toggledPressure = false
        this.toggledAcceleration = false
        this.toggledBPM = false

        
        return

      }

    },

    BPM(){
      this.createChart()
      if(this.toggledBPM == true){ //if the button gets untoggled
        this.toggledBPM = false
        this.stoppedBPM = true
        return
      }

      var a = this //this is not the same inside an arrow function
      this.aa = true
      this.connection.onmessage = (event) => {

        // console.log(event)
        // console.log(event.data.HEj)
        if(JSON.parse(event.data)["topic"] == "mqtt" ){
          
          a.BPM_data = JSON.parse(event.data)["value"]

          if(a.BPM_data > 110 && a.blood_pressure_data > 10 && a.acceleration_data > 17){
            a.fallDetected = true
          }

        }
        else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
         a.blood_pressure_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }

        else if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == true){
         a.acceleration_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }


    }
    this.toggledBPM = true
    this.stoppedBPM = false
  },

  stopBPM(){
    this.aa = false
    this.toggledBPM = false
    this.connection.onmessage = (event) => {

      if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == false ){
        
        return

      }
      else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
         this.blood_pressure_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }

      else if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == true){
         this.acceleration_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }

      }

  },

  bloodPressure(){

      if(this.toggledPressure == true){ //if the button gets untoggled
        this.toggledPressure = false
        this.stoppedPressure = true
        return
      }

      this.bb = true
      var a = this //this is not the same inside an arrow function
      this.connection.onmessage = (event) => {

        // console.log(event)
        console.log(JSON.parse(event.data)["value"])
        console.log(JSON.parse(event.data)["topic"])
        // console.log(event.data.HEj)
        if(JSON.parse(event.data)["topic"] == "mqtt2"){
          
          a.blood_pressure_data = JSON.parse(event.data)["value"]
          if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }
        else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
         a.BPM_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }

        else if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == true){
         a.acceleration_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }

    }

    this.toggledPressure = true
    this.stoppedPressure = false

    },

    stopPressure(){
      this.bb = false
      this.toggledPressure = false
      this.connection.onmessage = (event) => {
        

        // console.log(event)
        console.log(JSON.parse(event.data)["value"])
        console.log(JSON.parse(event.data)["topic"])
        // console.log(event.data.HEj)
        if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == false ){
          
          return

        }

        else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
         this.BPM_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }

        else if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == true){
         this.acceleration_data = JSON.parse(event.data)["value"]
         if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

        }
        

        }

},

acceleration(){

if(this.toggledAcceleration == true){ //if the button gets untoggled
  this.toggledAcceleration = false
  this.stoppedAcceleration = true
  return
}

var c = this //this is not the same inside an arrow function
this.cc = true
var a = this
this.connection.onmessage = (event) => {

  // console.log(event)
  // console.log(event.data.HEj)
  if(JSON.parse(event.data)["topic"] == "mqtt3" ){
    
    a.acceleration_data = JSON.parse(event.data)["value"]
    if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

  }
  else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
   a.blood_pressure_data = JSON.parse(event.data)["value"]
   if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

  }

  else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
   a.BPM_data = JSON.parse(event.data)["value"]
   if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
            a.fallDetected = true
          }

  }

}
this.toggledAcceleration = true
this.stoppedAcceleration = false
},

stopAcceleration(){
this.cc = false
this.toggledAcceleration = false
this.connection.onmessage = (event) => {

if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == false ){
  
  return

}
else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
   this.BPM_data = JSON.parse(event.data)["value"]

  }
else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
   this.blood_pressure_data = JSON.parse(event.data)["value"]

  }

}

},


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


.body{
  position:absolute;
  width:100vw;
  height: 100vh;
  display: grid;
  grid-template-columns: 1fr 1fr 0.3fr;
  grid-template-rows: 1fr 1fr 1fr;
}

.sensors{
  grid-column-start: 1;
  grid-column-start: 1;
}

.additionaInfo{
  grid-column-start: 1;
  grid-column-start: 1;
  grid-row-start:2;
  grid-row-start:3;
  // background-color: rgb(183, 199, 236);
  height:70%;
  width:95%;
  margin-top:1rem;
  border-radius: 1rem;

  
}

.map-falls{
  // background-color: blue;
  height:95%;
  
  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 4;
  right:3rem;
}



#alertMessage{
  grid-column-start: 1;
  grid-column-end: 1;
}

</style>