function numberGenerator() {
  // Local “free” variable that ends up within the closure
  var num = 1;
  function checkNumber() {
    num++;
    console.log(num);
  }
  

  return checkNumber;
}

var number = numberGenerator();
number(); // 2
number(); // 2
number(); // 2
number(); // 2
