function SubString(str) {
  const myset = [];
  var count = 0;
  var n = str.length;
  for (var i = 0; i < n; i++)
    for (var j = i + 1; j <= n; j++) {
      myset.push(str.substring(i, j));
    }

  for (var k = 0; k < myset.length; k++) {
    element = myset[k];
    num = element.length;
    if (element[0] == element[num - 1]) {
      count++;
    }
  }
  return count;
}

var str = "abcab";
console.log(SubString(str));
