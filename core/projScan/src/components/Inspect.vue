<template>
    <div class="dashboard-card">
        <Card style="width: 30%">
            <template #header>
                <div class="wrapper-img">
                    <img alt="user header" src="https://i.imgur.com/yGF4yPg.png" style="width: 70%;"/>
                </div>
            </template>
            <template #title> {{selectedScan.ESSID}} </template>
            <template #subtitle> {{selectedScan.BSSID}} </template>
            <template #content>
                <ul>
                    <li>Descoberta da Rede: {{selectedScan.Firsttimeseen}}</li>
                    <li>Último Update: {{selectedScan.Lasttimeseen}}</li>
                    <li>Channel: {{selectedScan.Channel}}</li>
                    <li>Speed: {{selectedScan.Speed}}</li>
                    <li>Privacy: {{selectedScan.Privacy}}</li>
                    <li>Cipher: {{selectedScan.Cipher}}</li>
                    <li>Authentication: {{selectedScan.Authentication}}</li>
                    <li>Power: {{selectedScan.Power}}</li>
                    <li>Beacons: {{selectedScan.Beacons}}</li>
                    <li>IV: {{selectedScan.IV}}</li>
                    <li>LAN IP: {{selectedScan.LANIP}}</li>
                    <li>IDLength: {{selectedScan.IDlength}}</li>
                    <li>Key: {{selectedScan.Key}}</li>
                    <li>WPSVersion: {{selectedScan.WPSVersion}}</li>
                    <li>WPSState: {{selectedScan.WPSState}}</li>
                    <li>WPSLocked: {{selectedScan.WPSLocked}}</li>
                    <li>WPSMethod: {{selectedScan.WPSmethod}}</li>
                    <li>Manufacturer: {{selectedScan.Manufacturer}}</li>


                </ul>
            </template>
            <template #footer>

            </template>
        </Card>
    </div>
    
</template>

  
<script>
import axios from 'axios';
import Card from 'primevue/card';
//CSS
import "primevue/resources/themes/lara-light-indigo/theme.css";     
import "primevue/resources/primevue.min.css";

    export default{
        props: ['id'],
        components: {
            Card,
        },
        data() {
            return {
               selectedScan: ''
            };
        },
        methods:{
            async getScan(specID){
                await axios.get('http://localhost:3000/inspect', {
                    params: {
                        scanID: specID
                    }
                }).then(response => {
                    this.selectedScan = response.data[0]
                }).catch(error => {
                    console.log(error)
                })
            }
        },
        created(){
            this.getScan(this.id)
        }


    };
</script>
  