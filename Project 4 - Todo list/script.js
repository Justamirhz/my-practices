let button = document.querySelector("button")
var newtodo = "";
button.addEventListener("click",function(e){
   let inputvalue = document.querySelector("input").value
    newtodo += inputvalue
    newtodo += ","
  localStorage.setItem("todos",newtodo)
})

let todos = localStorage.getItem("todos")
let todointoarray = todos.split(",")

console.log(todointoarray)

for(i=0;i<todointoarray.length-1;){
document.querySelector("ul").innerHTML +=  `<li>${todointoarray[i]}</li>`
i++
}
