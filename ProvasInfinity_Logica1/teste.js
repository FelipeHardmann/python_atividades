const main = (params) => {
    for (let num = 2; num <= params; num++) {
      let isPrime = true;
      for (let number = 2; number < num; number++) {
        if (num % number == 0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) {
        console.log(num);
      }
    }
  }
  
  main(20);