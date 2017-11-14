//An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
//Implement a function that determines whether a string that contains only letters is an isogram. 
//Assume the empty string is an isogram. Ignore letter case.

//is_isogram("Dermatoglyphics" ) == true
//is_isogram("aba" ) == false
//is_isogram("moOse" ) == false # -- ignore letter case

function isIsogram(str){
   if (str ===""){
    return true;
  }else{
    var str_uppercase = str.toUpperCase();
    var str_split = str_uppercase.split("");
    for(var i=0; i < str_split.length; i++){
      for(var k=i+1; k < str_split.length; k++){
        if(str_split[i] === str_split[k]){
            return false;
        }
      }
    }
    return true;
  }
}
