// Check to see if a string has the same amount of 'x's and 'o's. 
// The method must return a boolean and be case insensitive. The string can contains any char.

function XO(str) {
    var countX = 0
    var countO = 0
    for(var i = 0 ; i < str.length ; i++){
      if(str[i] == "x" || str[i] == "X"){
        countX += 1
      }
      if(str[i] == "O" || str[i] == "o"){
        countO += 1
      }
    }
    if( countX == countO){
      return true;
    }
    else{
      return false;
    }
}
