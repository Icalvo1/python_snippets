//function that returns true if the square root of a number is a whole number and false if it is a floating point number

function even_square(x){
x = Math.sqrt(x);
if(x - Math.floor(x) != 0){return false}else{return true}
}