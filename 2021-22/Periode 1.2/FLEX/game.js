let canvas = document.getElementById("game");
let ctx = canvas.getContext("2d");
ctx.fillStyle = "red";
ctx.strokeStyle = "black";

ctx.beginPath();
ctx.moveTo(50,0);
ctx.lineTo(-50,-20);
ctx.lineTo(-50,20);
ctx.lineTo(50,0);
ctx.stroke();
ctx.fill();  
ctx.beginPath();
ctx.fillStyle = "blue";
ctx.fillRect(200, 200, 50, 50);
ctx.beginPath();
ctx.strokeStyle = "red";
ctx.strokeRect(200, 200, 50, 50);

//tekenposities
let x = 100;
let y = 100;
let size = 10;
//kleur
ctx.fillStyle = "red";
function update(time){
    //beweging
    x++;
    //teken vierkant
    ctx.beginPath();
    ctx.moveTo(x,y);
    ctx.lineTo(x+1,y);
    ctx.lineTo(x+size,y+size);
    ctx.lineTo(x,y+size);
    ctx.lineTo(x,y);
    ctx.fill();
    window.requestAnimationFrame(update);
}
window.requestAnimationFrame(update);