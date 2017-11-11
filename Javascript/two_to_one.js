// Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

// each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"

// a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```


function deDup(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] == arr[i + 1]) {
      arr.splice(i + 1, 1);
      i = i - 1;
    }
  }
  str = arr.join('');
  return str;
}

function longest(s1, s2) {
  return deDup((s1 + s2).split('').sort());
}