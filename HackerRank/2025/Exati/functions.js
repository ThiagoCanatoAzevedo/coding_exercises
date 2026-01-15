function factorial(n){
    let factorial = n

    for (let i=1;i<n;i++){
        factorial = factorial*(n-i)
    }

    console.log(factorial)
}

factorial(6)