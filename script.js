fetch('./teste2Json.json')
    .then((response) => response.json())
    .then((json) => {
        data = json
        console.log(data.боку)
        init()
    });


function init() {
    
    const phrase = prompt("type phrase")
    const splittedWords = phrase.split(" ")    

    const finalList = []

    splittedWords.forEach(word => {
        if (data[word]) {
            finalList.push(data[word])
        } else {
            finalList.push(word)
        }
    });
    
    alert(`the words with stress marks: \n${finalList.toString().replaceAll(",", ' ')}`)

}




