const regex = /[.,:?!'"()]/g;
const input = document.querySelector("#input--text textarea")
const output = document.querySelector("#output--text textarea")
const btn = document.querySelector("#input--text button")
const modal = document.querySelector("#modal")
const openModal = document.querySelector("#open--modal")
const closeModal = document.querySelector(".close--modal")
const overlay = document.querySelector(".overlay")
const toggleModalBtns = [openModal, closeModal, overlay]

// OPEN JSON FILE
fetch('./data.json')
    .then((response) => response.json())
    .then((json) => {
        data = json
        init() // initializes the application after the data is fetched
    });

// INITIALIZE APLICATION
function init() {
    btn.addEventListener("click", () => {
        phrase = input.value
        marker(phrase)
    })
}

// SPLITTING THE INDIVIDUAL WORDS
function marker(phrase) {
    const splittedWords = phrase.replaceAll(regex, '') // removes special characters
        .toLowerCase() // turns everything to lower case to make it possible to search in the database
        .split(" ") // takes the words between spaces and add to an array

    // FINDING THE WORD IN THE DATABASE
    const finalList = []
    splittedWords.forEach(word => {
        if (data[word]) { // looks for the key in the JSON file with the same name of the word
            finalList.push(data[word]) // if the key is in the file, its value is added to the array above
        } else {
            finalList.push(word) // if the key is not there, the word is added to array as it is
        }
    });

    // OUTPUTTING THE WORDS WITH ACCENT
    output.value = finalList.toString().replaceAll(",", ' ') // converts the array into a string and changes the comma for spaces
}


// TOGGLE MODAL
function toggleModal() {
    modal.classList.toggle("hidden")
    overlay.classList.toggle("hidden")
}

toggleModalBtns.forEach(btn => btn.addEventListener("click", () => {
    toggleModal()
}))

document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
        if (!modal.classList.contains("hidden")) {
            toggleModal()
        }
    }
})
