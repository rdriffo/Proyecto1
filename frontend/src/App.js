//import React from 'react';
import React, { useState, useEffect } from 'react';
// Importando los Componentes
import { MuestraBuscador } from './component/MuestraBuscador';
import { MuestraTitulo } from './component/MuestraTitulo';
import { MuestraImagen } from './component/MuestraImagen';
import { MuestraNombre } from './component/MuestraNombre';
import { MuestraDatos } from './component/MuestraDatos';
import { MuestraFooter } from './component/MuestraFooter';

import {getDatos} from './datos/obtienedatos';

// Usando nuestros componentes
function App() {
  
  // const datos =[
  //   {run:1, nombre:'Rodrigo'},
  //   {run:2, nombre:'Pedro'},
  //   {run:3, nombre:'Francisco'},
  //   {run:4, nombre:'Emilia'}
  // ]
  const datos = [
  {
    "identificacion": {
      "run": 15242285,
      "dv_run": "7",
      "npi": 200808,
      "dv_npi": 8,
      "apell_pat": "RIFFO",
      "apell_mat": "CURIPAN",
      "primer_nombre": "RODRIGO",
      "segundo_nombre": "ESTEBAN",
      "sigla_unid_rep": "PENTAGONO",
      "estado_cto": "ACTIVO",
    }
  ]
  const [infopersonas, setPersonas] = useState({
    // data:[],
    // loaded:false
  });


    useEffect (()=>{
    console.log('Luego Paso II, Accedio al useEffect')
    setPersonas(identificacion[run])
  },[])





  // Llamado a la API
  const obtDatos = async()=> {
    const rut='15242285';
    //const data = await fetch(`http://127.0.0.1:8000/APP/pagina/${rut}`)
   // const data = await fetch(`http://127.0.0.1:8000/APP/get_data/${rut}`)
    const infopersonas = await data.json()
    console.log(data)
  }

  
  // const [personas, getDatos] = useState({
  //     data:[]
  //     //loaded:false
  //   });
  // useEffect (()=>{
  //   console.log('Luego Paso II, Accedio al useEffect')
  // })

  // const [personas, getDatos] = useState({
  //   data:[]
  //   //loaded:false
  // });

  // // useEffect(()=>{
  // //   getDatos().then(resultado=>{
  // //     data: resultado
  //     //loader:true
  //   })
  // }
  // );


  // const [count, setCount] = useState(0);
  // useEffect(() => {
    // Actualiza el título del documento usando la API del navegador
    // document.title = `You clicked ${count} times`;
  // });


//  Datos de ejemplo pra pruebas
//   return (
//     <div>
//       <p>You clicked {count} times</p>
//       <button onClick={() => setCount(count + 1)}>
//         Click me
//       </button>
//     </div>
//   );



console.log('Primero Pasa por Aca');

  return (
    <React.Fragment>
        <MuestraBuscador/>
        <MuestraTitulo />
        <MuestraImagen />
        <MuestraNombre />
        <MuestraDatos />
        <MuestraFooter/>       
    </React.Fragment>
  
  );
 
}
export default App;
