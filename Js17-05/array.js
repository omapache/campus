// FORMA ANTIGUA DE CREAR ARRAYS O ARREGLOS
// let autos = new Array("BMW","MERCEDES","VOLVO")

// FORMA ADECUADA
const autos = ["BMW","MERCEDES","VOLVO"];
// ITERAR UNO POR UNO
console.log(autos);
console.log(autos[0])
console.log(autos[1])
console.log(autos[2])
// ITERAR TODOS
for (let i = 0; i<(autos.length); i++) {
    console.log( i + ":" + autos[i])
}

// MODIFICAR ARRAY
autos[0] = "a";
console.log(autos);

// AGREGAR ITEM AL ULTIMO LUGAR ARRAY
autos.push("a");
console.log(autos);

//MIRAR LA CANTIDAD DE ITEM
console.log(autos.length);

// ELIMINAR ITEM
autos.pop();
console.log(autos);
// ELIMINAR ITEM EN UN LUGAR ESPECIFICO
autos.splice(0,1);
console.log(autos);


