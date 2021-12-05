import React from "react";
import '../css/MuestraBuscador.css'

function MuestraBuscador(){
 // const estado = React.useState();

  const [searchValue, setSeartchValue] = React.useState('');

  const onSearchValueChange =(event) => {
    console.log(event.target.value);
    setSeartchValue(event.target.value);
  }
  return(
        <input 
        className="MuestraBuscador" 
        placeholder="Ingresar RUN" 
        value={searchValue}
        onChange={onSearchValueChange}
        //onChange={onSearchValueChange}
        />
       
        )
}

export {MuestraBuscador};