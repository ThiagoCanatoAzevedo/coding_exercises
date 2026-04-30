function camelCase(str){
    let counter = 1;
    for(let i = 0; i < str.length; i++){
        if(str[i] == str[i].toUpperCase()){
            counter+=1
        }
    }
    console.log(counter)
}

camelCase("saveChangesInTheEditor")

/*
Exercise anotations:
- Name: CamelCase
- Difficulty: Easy
- Score: 15/15
*/