<template>
  <div class="body">
    <div class="sensors">
      <div>
        <v-alert
          id="alertMessage"
          v-if="fallDetected == true"
          outlined
          :value="alert"
          transition="scale-transition"
          prominent
          type="warning"
          style="width: 80%; color: red"
        >
          <h3 style="margin-left: 5rem; color: red">
            Fall detected {{ fallTime }}
          </h3>
          <v-btn
            color="rgb(93, 200, 118)"
            @click="alert = !alert"
            style="margin-left: 4rem"
          >
            I have been notified
          </v-btn>
        </v-alert>

        <div
          class="patient-info"
          style="margin-top: 2rem; margin-bottom: 2rem; width: 30%"
        >
          <h3 style="text-align: center; margin-bottom: 0.5rem">
            Patient info
          </h3>
          <h3>Name: Test Testsson</h3>
          <h3>Age: 86</h3>
          {{mobileData}}
        </div>

        <div>
          <div style="display: flex; flex-direction: row">
            <div>
              <h3 v-if="parseInt(BPM_data) < 100" style="color: green">
                Heart rate data: {{ BPM_data }} beats per minute
              </h3>
              <h3 v-else style="color: red">
                Heart rate data: {{ BPM_data }} beats per minute
              </h3>
              <button
                v-if="toggledBPM == false"
                v-on:click="BPM"
                style="
                  margin-top: 0.5rem;
                  border: solid;
                  border-width: 3px;
                  border-radius: 3px;
                  background-color: rgb(93, 200, 118);
                "
              >
                Collect data
              </button>
              <button
                v-else
                v-on:click="BPM"
                style="
                  margin-top: 0.5rem;
                  border: solid;
                  border-width: 3px;
                  border-radius: 3px;
                  background-color: rgb(93, 200, 118);
                "
              >
                Collecting...
              </button>
              <button
                v-on:click="stopBPM"
                style="
                  margin-top: 0.5rem;
                  border: solid;
                  border-width: 3px;
                  border-radius: 3px;
                  background-color: rgb(225, 90, 90);
                "
              >
                Stop collecting
              </button>
            </div>
            <div>
              <client-only>
                <div id="chart">
                  <component
                    :is="apexchart"
                    height="250"
                    width="500"
                    type="area"
                    :options="options"
                    :series="series"
                  />
                </div>
              </client-only>
            </div>
          </div>

          <div style="display: flex; flex-direction: row">
            <div style="margin-top: 2rem">
              <h3
                v-if="parseInt(blood_pressure_data) < 10"
                style="color: green"
              >
                Blood pressure data: {{ blood_pressure_data }}/{{
                  blood_pressure_data
                }}
                mmHg
              </h3>
              <h3 v-else style="color: red">
                Blood pressure data: {{ blood_pressure_data }}/{{
                  blood_pressure_data
                }}
                mmHg
              </h3>
              <!-- <button v-if="toggledPressure == false" v-on:click="bloodPressure" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px;  background-color:rgb(93, 200, 118);"  >Collect data</button>
             <button v-else v-on:click="bloodPressure" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(93, 200, 118);">Collecting...</button>
             <button  v-on:click="stopPressure" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(225, 90, 90);">Stop collecting</button> -->
            </div>

            <div>
              <client-only>
                <div id="chart">
                  <component
                    :is="apexchart"
                    height="250"
                    width="500"
                    type="area"
                    :options="options1"
                    :series="series1"
                  />
                </div>
              </client-only>
            </div>
          </div>
        </div>
      </div>

      <div style="display: flex; flex-direction: row">
        <div style="margin-top: 2rem">
        <h3 v-if="parseInt(acceleration_data) < 16" style="color: green">
          Acceleration: {{ acceleration_data }} m/s<sup>2</sup>
        </h3>
        <h3 v-else style="color: red">
          Acceleration: {{ acceleration_data }} m/s<sup>2</sup>
        </h3>
        </div>
        <!-- <button v-if="toggledAcceleration == false" v-on:click="acceleration" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px;  background-color:rgb(93, 200, 118);"  >Collect data</button>
             <button v-else v-on:click="acceleration" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(93, 200, 118);">Collecting...</button>
             <button  v-on:click="stopAcceleration" style="margin-top:0.5rem; border:solid;border-width: 3px; border-radius: 3px; background-color:rgb(225, 90, 90);">Stop collecting</button> -->
      
                  <div>
              <client-only>
                <div id="chart" style="margin-left:5rem">
                  <component
                    :is="apexchart"
                    height="250"
                    width="500"
                    type="area"
                    :options="options2"
                    :series="series2"
                  />
                </div>
              </client-only>
            </div>
          </div>

      <div class="additionaInfo" style="">
        <!-- <div id="chart">
        <apexchart type="line" height="350" ref="chart" :series="series"></apexchart>
      </div> -->
      </div>
    </div>

    <div class="map-falls">
      <client-only>
        <l-map
          :zoom="7"
          :minZoom="3"
          :maxZoom="14"
          :center="[58.70887, 13.97456]"
          :attributionControl="true"
        >
          <l-tile-layer
            url="https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png"
          ></l-tile-layer>

          <div v-for="item in items.length" :key="item">
            <l-marker :lat-lng="items[item - 1]">
              <l-icon
                :icon-size="50"
                :icon-anchor="dynamicAnchor"
                icon-url="https://www.freeiconspng.com/uploads/-human-male-man-people-person-profile-red-user-icon--icon--23.png"
              />
              <l-popup style="color: blue">
                <span>Patient: Test Testsson</span>
                <br />
                <span>Id: 25633</span>
                <br />
                <span>Olyckan inträffa klockan:{{ fallTime }}</span>
                <br />
                <span>Koordinater: [Lat: 58.708870, Long:13.974560]</span>
                <br />
                <span>Olyckstyp: Fall från stol</span>
                <br />
                <span>Adress: Stigvägen 3</span>
                <br />
                <span>Telefon: 0782263733</span>
                <br />
                <span>Rum: Vardagsrum</span>
                <br />
                <span>Boende typ: Lägenhet, vån 2 (t.v)</span>
                <br />
                <span>Portkod: 2345 </span>
                <br />
                <span>Medicins info: </span>
                <br />
              </l-popup>
            </l-marker>
            -->
          </div>

          <!-- <l-marker :lat-lng=item> 
                <l-popup style="color:blue" ><span></span></l-popup></l-marker> -->
        </l-map>
      </client-only>
    </div>

    <!-- <h3>{{$nuxt.$fire.auth.currentUser.email}}</h3> -->
  </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>

<script>
import { Line } from "vue-chartjs";
import mqtt from 'mqtt'


export default {
  computed: {
    apexchart() {
      return () => {
        if (process.client) {
          return import("vue-apexcharts");
        }
      };
    },
  },

  data() {
    return {
      items: [],
      // items:[[57.708870,11.974560],[55.9464418,8.1277591],[58.9464418,8.1277591]],
      alert: true,
      BPM_data: "0",
      mobileData:"0",
      pressure_data: "0",
      blood_pressure_data: "0",
      acceleration_data: "0",
      connection: null,
      stop: false,
      aa: false,
      bb: false,
      cc: false,
      startSensors: true,
      toggledBPM: false,
      toggledPressure: false,
      toggledAcceleration: false,
      stoppedBPM: false,
      stoppedPressure: false,
      stoppedAcceleration: false,
      fallDetected: false,
      fallTime: null,
      today: null,
      today1: null,
      today2: null,
      time: null,
      time1: null,
      time2: null,
      newData: null,
      newData1: null,
      newData2: null,
      timeData: null,
      timeData1: null,
      timeData2: null,
      options: {
        chart: {
          colors: ["#77B6EA"],
          fill: {
          colors: ["#5091c7",],
        },
          id: "vuechart-example",
        },
        title: {
          text: "Average High & Low Temperature", //https://apexcharts.com/vue-chart-demos/line-charts/data-labels/
          align: "middle",
        },
        xaxis: {
          categories: [],
          title: {
            text: "Time",
          },
        },
      },
      options1: {
        chart: {
          id: "vuechart-example",
        },
        colors: ["#FF94F8"],
        fill: {
          colors: ["#DB82D6",],
        },
        title: {
          text: "Average High & Low Temperature", //https://apexcharts.com/vue-chart-demos/line-charts/data-labels/
          align: "middle",
        },
        xaxis: {
          categories: [],
          title: {
            text: "Time",
          },
        },
      },
      options2: {
        chart: {
          id: "vuechart-example",
        },
        colors: ["#1FFF9D"],
        fill: {
          colors: ["#18E38A"],
        },
        title: {
          text: "Average High & Low Temperature", //https://apexcharts.com/vue-chart-demos/line-charts/data-labels/
          align: "middle",
        },
        xaxis: {
          categories: [],
          title: {
            text: "Time",
          },
        },
      },
      series: [
        {
          name: "Heart Rate [BPM]",
          data: [],
        },
      ],
      series1: [
        {
          name: "Blood pressure [mmHg]",
          data: [],
        },
      ],
      series2: [
        {
          name: "Acceleration [m/s^2]",
          data: [],
        },
      ],

     

      // series: [{
      //   name: 'Heart Rate [BPM]',
      //   data: []
      // },
      // {
      //   name: 'Blood pressure [mmHg]',
      //   data: []
      // },
      // {
      //   name: 'Acceleration [m/s^2]',
      //   data: []
      // }]
    };
  },

  mounted() {
    this.timeData = this.options.xaxis.categories;
    this.newData = this.series[0].data;
    this.timeData1 = this.options1.xaxis.categories;
    this.newData1 = this.series1[0].data;
    this.timeData2 = this.options2.xaxis.categories;
    this.newData2 = this.series2[0].data;
    this.connection = new WebSocket("ws://localhost:8000/bpm");
    this.connection.onopen = () => console.log("connectionBPM established");
  },

  watch: {
    //watch for falls
    fallDetected: function (val) {
      this.today = new Date();
      this.time =
        this.today.getHours() +
        ":" +
        this.today.getMinutes() +
        ":" +
        this.today.getSeconds();

      if (val == true) {
        this.items = [[58.70887, 13.97456]];
        this.fallTime = this.time;
      }
    },
  },

  methods: {

    createChart() {},

    isOpen() {
      return this.connection.readyState === this.connection.OPEN;
    },

    startStopSensor() {
      // if(this.connection.readyState)
      console.log(this.connection.readyState);

      if (this.startSensors == true) {
        this.startSensors = false;
        this.connection.send(JSON.stringify({ stop: false }));

        if (!this.isOpen()) {
          console.log("EJ ÖPPEN");
        }

        return;
      } else {
        this.connection.send(JSON.stringify({ stop: true }));
        this.startSensors = true;
        this.BPM_data = "0";
        this.acceleration_data = "0";
        this.blood_pressure_data = "0";
        this.toggledPressure = false;
        this.toggledAcceleration = false;
        this.toggledBPM = false;

        return;
      }
    },

    BPM() {
    
      if (this.toggledBPM == true) {
        //if the button gets untoggled
        this.toggledBPM = false;
        this.stoppedBPM = true;
        return;
      }

      var a = this; //this is not the same inside an arrow function
      this.aa = true;
      // const newData = this.series[0].data
      // const newData1 = this.series[1].data
      // const newData2 = this.series[2].data
      // this.timeData = this.options.xaxis.categories
      this.connection.onmessage = (event) => {
        // https://github.com/apexcharts/vue-apexcharts
        // console.log(event)
        console.log(JSON.parse(event.data)["topic"])
        console.log(JSON.parse(event.data)["value"])
        if (JSON.parse(event.data)["topic"] == "testseth") {
          console.log("FRÅN MOBIL")
          a.mobileData = JSON.parse(event.data)["value"];
        }
        if (JSON.parse(event.data)["topic"] == "/mqtt") {
          a.today = new Date();

          a.BPM_data = JSON.parse(event.data)["value"];
          a.time =
            a.today.getHours() +
            ":" +
            a.today.getMinutes() +
            ":" +
            a.today.getSeconds();
          console.log("TIME", typeof a.time);

          a.newData.push(a.BPM_data);
          // newData1.push(a.BPM_data*2+4)
          // newData2.push(a.BPM_data*1.2+10)
          a.timeData.push(a.time);

          if (a.timeData.length > 10) {
            a.timeData.splice(0, 1);
            a.newData.splice(0, 1);
          }

          // For reference: https://github.com/apexcharts/vue-apexcharts
          a.options = {
            ...a.options,
            ...{
              xaxis: {
                categories: a.timeData,
              },
            },
          };

          a.series = [
            {
              data: a.newData,
              name: "Heart Rate [BPM]",
            },
          ];

          // a.series1 =  [{
          //   data: a.newData,
          //   name: 'Heart Rate [BPM]'},

          // ]

          // && a.blood_pressure_data > 10 && a.acceleration_data > 17
          if (a.BPM_data > 120 &&
            a.blood_pressure_data > 9 &&
            a.acceleration_data > 15) {
            a.fallDetected = true;
            a.options = {
            ...a.options,
            ...{
              colors:["#FF0000"]
            },
          };
            a.options1 = {
            ...a.options1,
            ...{
              colors:["#FF0000"]
            },
          };
            a.options2 = {
            ...a.options2,
            ...{
              colors:["#FF0000"]
            },
          };
          }
        }
        // else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
        else if (JSON.parse(event.data)["topic"] == "mqtt2") {
          a.blood_pressure_data = JSON.parse(event.data)["value"];

          a.today1 = new Date();

          a.blood_pressure_data = JSON.parse(event.data)["value"];
          a.time1 =
            a.today1.getHours() +
            ":" +
            a.today1.getMinutes() +
            ":" +
            a.today1.getSeconds();
          console.log("TIME", typeof a.time1);

          a.newData1.push(a.blood_pressure_data);
          // newData1.push(a.BPM_data*2+4)
          // newData2.push(a.BPM_data*1.2+10)
          a.timeData1.push(a.time1);

          if (a.timeData1.length > 10) {
            a.timeData1.splice(0, 1);
            a.newData1.splice(0, 1);
          }

          // For reference: https://github.com/apexcharts/vue-apexcharts
          a.options1 = {
            ...a.options1,
            ...{
              xaxis: {
                categories: a.timeData1,
              },
            },
          };

          a.series1 = [
            {
              data: a.newData1,
              name: "Heart Rate [BPM]",
            },
          ];

          if (
            a.BPM_data > 120 &&
            a.blood_pressure_data > 9 &&
            a.acceleration_data > 15
          ) {
            a.fallDetected = true;
            a.options = {
            ...a.options,
            ...{
              colors:["#FF0000"]
            },
          };
            a.options1 = {
            ...a.options1,
            ...{
              colors:["#FF0000"]
            },
          };
            a.options2 = {
            ...a.options2,
            ...{
              colors:["#FF0000"]
            },
          };
          }
        }

        // else if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == true){
        else if (JSON.parse(event.data)["topic"] == "mqtt3") {
          a.acceleration_data = JSON.parse(event.data)["value"];

          a.today2 = new Date();
          a.time2 =
            a.today2.getHours() +
            ":" +
            a.today2.getMinutes() +
            ":" +
            a.today2.getSeconds();
          console.log("TIME", typeof a.time2);

          a.newData2.push(a.acceleration_data);
          // newData1.push(a.BPM_data*2+4)
          // newData2.push(a.BPM_data*1.2+10)
          a.timeData2.push(a.time2);

          if (a.timeData2.length > 10) {
            a.timeData2.splice(0, 1);
            a.newData2.splice(0, 1);
          }

          // For reference: https://github.com/apexcharts/vue-apexcharts
          a.options2 = {
            ...a.options2,
            ...{
              xaxis: {
                categories: a.timeData2,
              },
            },
          };

          a.series2 = [
            {
              data: a.newData2,
              name: "Heart Rate [BPM]",
            },
          ];

          if (
            a.BPM_data > 120 &&
            a.blood_pressure_data > 9 &&
            a.acceleration_data > 15
          ) {
            a.fallDetected = true;
            a.options = {
            ...a.options,
            ...{
              colors:["#FF0000"]
            },
          };
            a.options1 = {
            ...a.options1,
            ...{
              colors:["#FF0000"]
            },
          };
            a.options2 = {
            ...a.options2,
            ...{
              colors:["#FF0000"]
            },
          };
           
            
          }
        }
      };
      this.toggledBPM = true;
      this.stoppedBPM = false;
    },

    stopBPM() {
      // this.series[0].data = [3, 4, 4, 5, 9, 6, 7, 9]
      this.aa = false;
      this.toggledBPM = false;
      this.connection.onmessage = (event) => {
        if (JSON.parse(event.data)["topic"] == "mqtt" && this.aa == false) {
          return;
        } else if (
          JSON.parse(event.data)["topic"] == "mqtt2" &&
          this.bb == true
        ) {
          this.blood_pressure_data = JSON.parse(event.data)["value"];
          if (
            a.BPM_data > 100 &&
            a.blood_pressure_data > 9 &&
            a.acceleration_data > 15
          ) {
            a.fallDetected = true;
          }
        } else if (
          JSON.parse(event.data)["topic"] == "mqtt3" &&
          this.cc == true
        ) {
          this.acceleration_data = JSON.parse(event.data)["value"];
          if (
            a.BPM_data > 100 &&
            a.blood_pressure_data > 9 &&
            a.acceleration_data > 15
          ) {
            a.fallDetected = true;
          }
        }
      };
    },

    //   bloodPressure(){

    //       if(this.toggledPressure == true){ //if the button gets untoggled
    //         this.toggledPressure = false
    //         this.stoppedPressure = true
    //         return
    //       }

    //       this.bb = true
    //       var a = this //this is not the same inside an arrow function
    //       const newDataP = this.series[1].data
    //       if(this.options.xaxis.categories.length == 0){
    //         const timeData = this.options.xaxis.categories
    //       }
    //       this.connection.onmessage = (event) => {

    //         // console.log(event)
    //         console.log(JSON.parse(event.data)["value"])
    //         console.log(JSON.parse(event.data)["topic"])
    //         // console.log(event.data.HEj)
    //         if(JSON.parse(event.data)["topic"] == "mqtt2"){

    //           a.blood_pressure_data = JSON.parse(event.data)["value"]
    //           if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //         }
    //         else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
    //          a.BPM_data = JSON.parse(event.data)["value"]
    //          if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //         }

    //         else if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == true){
    //          a.acceleration_data = JSON.parse(event.data)["value"]
    //          if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //         }

    //     }

    //     this.toggledPressure = true
    //     this.stoppedPressure = false

    //     },

    //     stopPressure(){
    //       this.bb = false
    //       this.toggledPressure = false
    //       this.connection.onmessage = (event) => {

    //         // console.log(event)
    //         console.log(JSON.parse(event.data)["value"])
    //         console.log(JSON.parse(event.data)["topic"])
    //         // console.log(event.data.HEj)
    //         if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == false ){

    //           return

    //         }

    //         else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
    //          this.BPM_data = JSON.parse(event.data)["value"]
    //          if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //         }

    //         else if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == true){
    //          this.acceleration_data = JSON.parse(event.data)["value"]
    //          if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //         }

    //         }

    // },

    // acceleration(){

    // if(this.toggledAcceleration == true){ //if the button gets untoggled
    //   this.toggledAcceleration = false
    //   this.stoppedAcceleration = true
    //   return
    // }

    // var c = this //this is not the same inside an arrow function
    // this.cc = true
    // var a = this
    // this.connection.onmessage = (event) => {

    //   // console.log(event)
    //   // console.log(event.data.HEj)
    //   if(JSON.parse(event.data)["topic"] == "mqtt3" ){

    //     a.acceleration_data = JSON.parse(event.data)["value"]
    //     if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //   }
    //   else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
    //    a.blood_pressure_data = JSON.parse(event.data)["value"]
    //    if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //   }

    //   else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
    //    a.BPM_data = JSON.parse(event.data)["value"]
    //    if(a.BPM_data > 100 && a.blood_pressure_data > 9 && a.acceleration_data > 15){
    //             a.fallDetected = true
    //           }

    //   }

    // }
    // this.toggledAcceleration = true
    // this.stoppedAcceleration = false
    // },

    // stopAcceleration(){
    // this.cc = false
    // this.toggledAcceleration = false
    // this.connection.onmessage = (event) => {

    // if(JSON.parse(event.data)["topic"] == "mqtt3" && this.cc == false ){

    //   return

    // }
    // else if(JSON.parse(event.data)["topic"] == "mqtt" && this.aa == true){
    //    this.BPM_data = JSON.parse(event.data)["value"]

    //   }
    // else if(JSON.parse(event.data)["topic"] == "mqtt2" && this.bb == true){
    //    this.blood_pressure_data = JSON.parse(event.data)["value"]

    //   }

    // }

    // },

    // Toggle if navigation is shown or hidden
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Rubik+Mono+One&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Rubik+Mono+One&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@700&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@300;700&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Lato:wght@300;700&family=Montserrat:wght@500&family=Poppins:wght@400;900&family=Rubik+Mono+One&display=swap");
/* font-family: 'Anton', sans-serif;
font-family: 'Lato', sans-serif;
font-family: 'Poppins', sans-serif;
font-family: 'Rubik Mono One', sans-serif; */

.body {
  position: absolute;
  width: 100vw;
  height: 100vh;
  display: grid;
  grid-template-columns: 1fr 0.5fr 0.3fr;
  grid-template-rows: 1fr 1fr 1fr;
}

.sensors {
  grid-column-start: 1;
  grid-column-start: 1;
}

.additionaInfo {
  grid-column-start: 1;
  grid-column-start: 1;
  grid-row-start: 2;
  grid-row-start: 3;
  // background-color: rgb(183, 199, 236);
  height: 70%;
  width: 95%;
  margin-top: 1rem;
  border-radius: 1rem;
}

.map-falls {
  // background-color: blue;
  height: 95%;

  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 4;
  margin-right: -7rem;
}

#alertMessage {
  grid-column-start: 1;
  grid-column-end: 1;
}
</style>