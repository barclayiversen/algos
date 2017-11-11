function getMiddle(s)
{
    if(s.length % 2 === 0){
        var string = s[s.length/2 - 1] + s[s.length/2];
        return string;
    }
    else{
        var i = Math.floor(s.length/2);
        return (s[i]);
    }
}