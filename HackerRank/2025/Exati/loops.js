function loops(s){
    const array_vowels = []
    const array_consonants = []

    const vowels = ["a", "e", "i", "o", "u"]


    for (i=0;i < s.length; i++){
        if (vowels.includes(s[i])){
            array_vowels.push(s[i])
        }else{
            array_consonants.push(s[i])
        }
    }

    const final_array = array_vowels.concat(array_consonants)

    for(j=0;j<final_array.length; j++){
        console.log(final_array[j])
    }
}

loops("javascriptloops")