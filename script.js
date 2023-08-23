const regex = /[.,:?!'"()]/g;
const input = document.querySelector("#input--text textarea")
const output = document.querySelector("#output--text textarea")
const btn = document.querySelector("#input--text button")
const modal = document.querySelector("#modal")
const openModal = document.querySelector("#open--modal")
const closeModal = document.querySelector(".close--modal")
const overlay = document.querySelector(".overlay")


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


function toggleModal() {
    modal.classList.toggle("hidden")
    overlay.classList.toggle("hidden")
}

openModal.addEventListener("click", () => {
    toggleModal()
})

closeModal.addEventListener("click", () => {
    toggleModal()
})

overlay.addEventListener("click", () => {
    toggleModal()
})

document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
        if (!modal.classList.contains("hidden")) {
            toggleModal()
        }
    }
})
