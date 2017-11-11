function doubleChar(str) {
    var res = ""
    for (var i = 0; i<str.length;i++){
        var new_string = ""+str[i]+str[i];
        res = res.concat(new_string);
  }
  return res;
}