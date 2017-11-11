function isValidWalk(walk) {
    var n = 0; var s = 0; var w = 0; var e = 0;
    for (var i=0; i<walk.length; i++){
      if (walk[i] == "n"){
        n++
      }
      if (walk[i] == "s"){
        s++
      }
      if (walk[i] == "e"){
        e++
      }
      if (walk[i] == "w"){
        w++
      }
    }
    if(s - n == 0 && e - w == 0 && walk.length == 10){
      return true;
    } else {
      return false;
    }
  }