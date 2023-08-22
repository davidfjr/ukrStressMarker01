const regex = /[.,:?!'"()]/g;
const input = document.querySelector("#input--text textarea")
const output = document.querySelector("#output--text textarea")
const btn = document.querySelector("#input--text button")


fetch('./data.json')
    .then((response) => response.json())
    .then((json) => {
        data = json
        init()
    });

function marker(phrase) {
    const splittedWords = phrase.replaceAll(regex, '')
        .toLowerCase()
        .split(" ")

    const finalList = []

    splittedWords.forEach(word => {
        if (data[word]) {
            finalList.push(data[word])
        } else {
            finalList.push(word)
        }
    });

    output.value = finalList.toString().replaceAll(",", ' ')
}


function init() {
    btn.addEventListener("click", () => {
        phrase = input.value
        marker(phrase)
    })
}




//  tem q postar a atualização de lower case nas palavras