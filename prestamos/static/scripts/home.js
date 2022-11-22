
var label1 = document.getElementById("leerUsuario-label1");
var label2 = document.getElementById("leerUsuario-label2");

function leerUsuario(n){
    const xhr = new XMLHttpRequest();
    //xhr.open("GET", "http://192.168.0.10/enviarId");
    xhr.open("GET", "http://127.0.0.1:8000/guardarId/12345");
    xhr.send();
    xhr.responseType = "text";
    xhr.onload = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
        const data = xhr.response;
        if(n==1){
            label1.value = data
        }else{
            label2.value = data
        }

    } else {
        console.log(`Error: ${xhr.status}`);
    }
    };

}
