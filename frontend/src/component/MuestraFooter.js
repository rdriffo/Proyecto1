import React from "react";
import '../css/MuestraFooter.css'

function MuestraFooter(){
    return(
        <footer className="MuestraFooter">
            <p>&copy; {(new Date().getFullYear())} Nuestro Proyecto, @Ati..</p>
        </footer>
    )
}

export {MuestraFooter};