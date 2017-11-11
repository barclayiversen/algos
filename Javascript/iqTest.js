function iqTest(numbers){
  var numbersSplit = numbers.split(" ")
  for(var i=0; i<numbersSplit.length; i++){
    numbersSplit[i] = parseInt(numbersSplit[i], 10);
  }
  var evens=0;
  var odds=0;
  for(var i = numbersSplit.length-1; i>=0; i--){
    if(numbersSplit[i] % 2 == 0){
      evens += 1;
      var index1 = i + 1;
    }
    else {
      odds += 1;
      var index2 = i + 1;
    }
  }
  if(evens>odds){
    return index2;
  }
  else {
    return index1;
  }
}