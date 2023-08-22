// const teste = prompt("type")


//data = JSON.parse('testeJson.json')
fetch('./teste2Json.json')
    .then((response) => response.json())
    .then((json) => {
        data = json
        console.log(data.боку)
        init()
    });


function init() {
    // word = prompt("type")
    // console.log(`the word is ${data[word]}`)


    // isolando palavras da frase
    const phrase = prompt("digita a frase")
    const splittedWords = phrase.split(" ")  // tem q dar um jeito de tirar , e . e ? e ! e : 

    console.log(splittedWords)

    const finalList = []

    splittedWords.forEach(word => {
        if (data[word]) {
            finalList.push(data[word])
        } else {
            finalList.push(word)
        }
    });

    strList = finalList.toString()
    console.log(strList)
    alert(`a lista final é ${finalList.toString().replaceAll(",", ' ')}`)


    // let listaFinal = []

    // for (let i = 0; i < splittedWords.length; i++) {
    //     for (let j = 0; j < wordList.length; j++) {
    //         if (splittedWords[i] === wordList[j]) {
    //             listaFinal += `${ diacrits[j]}, `
    //         }
    //     }
    // }
    // alert(listaFinal)
    // console.log(listaFinal)
}




// var regex = /[.,\s]/g;

// var result = str.replace(regex, '');

// let found = ''
    // for (let i = 0; i < wordList.length; i++) {
    //     if (userInput === wordList[i]) {
    //         found = userInput            
    //         alert(found)
    //     }
    // } if (found === '') alert("not found")
