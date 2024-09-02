<template>
  <div class="dashboard-frame">
    <div class="dashboard-navbar">
      <div class="navbar-btn" v-for="(category,index) in navbarCategories">
        <button :class="{'active': category.active}" @click="navigate(index)">
          <i :class="category.icon"></i>
          <span>{{ category.name }}</span>
        </button>
      </div>
      <div class="navbar-btn">
        <button @click="logOut()" class="logout-btn">
          <i class="bi bi-door-open-fill"></i>
          <span>Logout</span>
        </button>
      </div>
      
    </div>
    <div class="dashboard-content">
      <DataTable v-model:filters="filters" :value="items" paginator :rows="5" :rowsPerPageOptions="[5, 10, 15]" resizableColumns columnResizeMode="fit" 
      showGridlines filterDisplay="row" v-if="navbarCategories[1].active" selectionMode="single" dataKey="BSSID" :metaKeySelection="false" ref="dt"
                @rowSelect="onRowSelect" style="width:95%">
      <template #header>
          <div style="text-align: left">
              <Button icon="pi pi-external-link" label="Export CSV" @click="exportCSV($event)" />
          </div>
      </template>
        <Column v-for="col of columns" :key="col.field" :field="col.field" :header="col.header" sortable filter>
        <template #filter="{ filterModel, filterCallback }">
            <InputText v-model="filterModel.value" v-tooltip.top.focus="'Hit enter key to filter'" type="text" @keydown.enter="filterCallback()" class="p-column-filter" />
        </template>
        <template #editor="{ data, field }">
            <InputText v-model="data[field]" autofocus />
        </template>
        </Column>
      </DataTable>
      <div class="full-stats-page" v-if="navbarCategories[0].active">
        <div class="full-stats-page-top">
          <Fieldset legend="WiFinder" v-if="items != null">
            <p>
                De momento existem {{items.length}} redes registadas na base de dados.
            </p>
        </Fieldset>
        </div>
        <div class="full-stats-page-bottom">
          <div class="stats-bottom-left">
            <h3 style="margin-top: 0;margin-bottom: 10px;">Fabricantes</h3>
            <Chart type="pie" :data="chartData" :options="chartOptions" v-if="items != null"/>

            <h3 style="margin-top: 5px;margin-bottom: 10px;">Authentication</h3>
            <Chart type="pie" :data="chartData4" :options="chartOptions" v-if="items != null"/>
          </div>  
          <div class="stats-bottom-right">
              <div class="stats-bottom-right-top">
                <h3 style="margin-top: 0;margin-bottom: 10px;">Privacy</h3>
                <Chart type="pie" :data="chartData2" :options="chartOptions" v-if="items != null"/>
              </div>
              <div class="stats-bottom-right-bottom">
                <h3 style="margin-top: 0;margin-bottom: 10px;">WPSVersion</h3>
                <Chart type="pie" :data="chartData3" :options="chartOptions" v-if="items != null"/>
              </div>
            
          </div>
        </div>
      </div>
      <div class="card" v-if="navbarCategories[2].active">
        <Toast />
        <FileUpload name="uploadCSV" :customUpload ="true" @uploader="onAdvancedUpload($event)" :maxFileSize="1000000">
            <template #empty>
                <p>Drag and drop files to here to upload.</p>
            </template>
        </FileUpload>
    </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
//CSS
import "primevue/resources/themes/lara-light-indigo/theme.css";     
import "primevue/resources/primevue.min.css";
//Imports
import { FilterMatchMode } from 'primevue/api';
//Components
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';                   // optional
import InputText from 'primevue/inputtext';
import FileUpload from 'primevue/fileupload';
import Toast from 'primevue/toast';
import Button from 'primevue/button';
import Chart from 'primevue/chart';
import Fieldset from 'primevue/fieldset';


export default {
  components: {
    DataTable,
    Column,
    ColumnGroup,
    Row,
    InputText,
    FileUpload,
    Toast,
    Button,
    Chart,
    Fieldset
  },
  data() {
    return {
      items: null,
      columns: null,
      filters: {
          ESSID: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          BSSID: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Firsttimeseen: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Channel: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Speed: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Privacy: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Cipher: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Authentication: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Authentication: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          Manufacturer: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
          WPSVersion: { value: null, matchMode: FilterMatchMode.STARTS_WITH }
      },
      navbarCategories:[
        {
          name: 'Estatisticas',
          icon: 'bi bi-house-door',
          active: true
        },
        {
          name: 'Visualizar Dados',
          icon: 'bi bi-search',
          active: false
        },
        {
          name: 'Importar Dados',
          icon: 'bi bi-send-plus',
          active: false
        },
        
    ],
    userData:{},
    chartOptions: {
      options: {
            responsive: true,
        }
    },
    chartData:{
        labels: [],
        datasets: [
            {
                data: [],
            }
        ]
    },
    chartData2:{
        labels: [],
        datasets: [
            {
                data: [],
            }
        ]
    },
    chartData3:{
        labels: [],
        datasets: [
            {
                data: [],
            }
        ]
    },
    chartData4:{
        labels: [],
        datasets: [
            {
                data: [],
            }
        ]
    }
  }
  },
    created() {
        this.columns = [
              {field: 'ESSID', header: 'Nome da Rede (ESSID)'},
              {field: 'BSSID', header: 'BSSID'},
              {field: 'Firsttimeseen', header: 'Data e Hora'},
              {field: 'Channel', header: 'Canal'},
              {field: 'Speed', header: 'Velocidade'},
              {field: 'Privacy', header: 'Privacidade'},              
              {field: 'Cipher', header: 'Cifra'},
              {field: 'Authentication', header: 'Autenticação'},
              {field: 'WPSVersion', header: 'Versão do WPS'},
              {field: 'Manufacturer', header: 'Fabricante'}
        ];
        this.userData = this.$store.getters.getUser
        console.log(this.userData)
    },
    async mounted() {
      if (this.$store.getters.getUser == null) {
        this.$router.push('/')
      }
      try {
        const response = await axios.get('http://localhost:3000/items');
        this.items = response.data;
        
        
        // Map this.items and change the WPSVersion from 0 to off and 1 to on 
        this.items.map(item => {
          if(item.WPSVersion == 0){
            item.WPSVersion = 'Desligado'
          }else if(item.WPSVersion == 1){
            item.WPSVersion = 'Ligado V1.0'
          }else if (item.WPSVersion == 2){
            item.WPSVersion = 'Ligado V2.0'
          }
        })

        this.items.map(item => {
          if(item.Authentication.trim().length == 0){
            item.Authentication = 'None'
          }
        })

        // Build Manufacturer PIE
          const columnName = 'Manufacturer';
          const listOfManufacturers = Object.values(response.data).map(arr => arr[columnName]);

          const uniqueList = [...new Set(listOfManufacturers)];
          this.chartData.labels = uniqueList;

          const countObject = {};

          this.items.forEach(obj => {
            const manufacturer = obj.Manufacturer;
            if (listOfManufacturers.includes(manufacturer)) {
              if (countObject[manufacturer]) {
                countObject[manufacturer]++;
              } else {
                countObject[manufacturer] = 1;
              }
            }
          });
          this.chartData.datasets[0].data = Object.values(countObject)

          // Build Privacy PIE
          const columnPrivacy = 'Privacy';
          const listOfPrivacy = Object.values(response.data).map(arr => arr[columnPrivacy]);

          const uniqueListPrivacy = [...new Set(listOfPrivacy)];
          this.chartData2.labels = uniqueListPrivacy;

          const countPrivacy = {};

          this.items.forEach(obj => {
            const privacy = obj.Privacy;
            if (listOfPrivacy.includes(privacy)) {
              if (countPrivacy[privacy]) {
                countPrivacy[privacy]++;
              } else {
                countPrivacy[privacy] = 1;
              }
            }
          });
          this.chartData2.datasets[0].data = Object.values(countPrivacy)

          // Build WPSVersion PIE
          const columnWPSVersion = 'WPSVersion';
          const listOfWPSVersion = Object.values(response.data).map(arr => arr[columnWPSVersion]);

          const uniqueListWPSVersion = [...new Set(listOfWPSVersion)];
          this.chartData3.labels = uniqueListWPSVersion;

          const countWPSVersion = {};

          this.items.forEach(obj => {
            const wpsVersion = obj.WPSVersion;
            if (listOfWPSVersion.includes(wpsVersion)) {
              if (countWPSVersion[wpsVersion]) {
                countWPSVersion[wpsVersion]++;
              } else {
                countWPSVersion[wpsVersion] = 1;
              }
            }
          });
          this.chartData3.datasets[0].data = Object.values(countWPSVersion)

           // Build Authentication
           const columnAuthentication = 'Authentication';
          const listOfAuthentication = Object.values(response.data).map(arr => arr[columnAuthentication]);

          const uniqueListAuthentication = [...new Set(listOfAuthentication)];
          this.chartData4.labels = uniqueListAuthentication;

          const countAuthentication = {};

          this.items.forEach(obj => {
            const auth = obj.Authentication;
            if (listOfAuthentication.includes(auth)) {
              if (countAuthentication[auth]) {
                countAuthentication[auth]++;
              } else {
                countAuthentication[auth] = 1;
              }
            }
          });
          this.chartData4.datasets[0].data = Object.values(countAuthentication)
        
        

      } catch (error) {
        console.error(error);
      }
    },
    methods: {
        navigate(category){
          for(let i in this.navbarCategories){
            this.navbarCategories[i].active = false
          }
          this.navbarCategories[category].active = !this.navbarCategories[category].active
          
        },
        async onAdvancedUpload(event) {
          
          const file = event.files[0]; // get the file from the event
          const formData = new FormData();
          formData.append('file', file); // 'file' is the field name expected by the server

          try {
            const response = await axios.post('http://localhost:3000/upload', formData, {
              headers: {
                'Content-Type': 'multipart/form-data',
              },
            });
            console.log(response.data);
            // The response should be the parsed CSV data
          } catch (error) {
            console.error(error);
          }
      },
      onRowSelect(event){
        console.log(event.data.scanID)
        // Navigate to the inspect page but open in a new tab
        const routeData = this.$router.resolve({name: 'Inspect', params: {id: event.data.scanID}});
        window.open(routeData.href, '_blank');
      },
      logOut(){
        this.$store.commit('setLogout', null)
        this.$router.push('/')
      },
      exportCSV(){
        this.$refs.dt.exportCSV();
        
      },
    }

};
</script>
