import {API_URL} from '../utils/constante.js';


export const getDatos = async () => {
    try{
        const URL = `${API_URL}/${rut}`;
        const rut='15242286';
        console.log('Estoy Aca');
        const response = await fetch(URL);
        const data = await response.json();
        const datos =  data.map(persona=>{
            return{
                run: persona.RUN,
                dv_run: persona.DV_RUN,
                npi: persona.NPI,
                dv_npi: persona.DV_NPI,
                apell_pat: persona.APELL_PAT,
                apell_mat: persona.APELL_MAT,
                primer_nombre: persona.PRIMER_NOMBRE,
                segundo_nombre: persona.SEGUNDO_NOMBRE,
                sigla_unid_rep: persona.SIGLA_UNID_REP,
                estado_cto: persona.ESTADO_CTO,
            }
        });
        return data;
       console.log(datos);
    } catch (error)
    {
        // ...
      }
    // console.log("Huston Tenemos un Problema");
}