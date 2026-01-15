function plusMinus(arr){
    let positives = 0;
    let negatives = 0;
    let zeros = 0;

    for(let i=0; i<arr.length; i++){
        if(arr[i] > 0) positives+=1
        else if(arr[i] < 0) negatives+=1
        else zeros+=1
    }
    
    console.log(positives / arr.length)
    console.log(negatives / arr.length)
    console.log(zeros / arr.length)
}

plusMinus([1,2,-3,-4,0,0])

/*
Exercise anotations:
- Name: Plus Minus
- Difficulty: Easy
- Score: 10/10
*/