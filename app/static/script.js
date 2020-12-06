import { initMap } from './map.js'

// CREATES DIV CHILD USER INPUT
function addUserChatElement(text) {
    const chatboxElement = document.getElementById('chatbox')
    const newUserChatElement = document.createElement('div')

    chatboxElement.appendChild(newUserChatElement) // adds div child to chatbox parent
    newUserChatElement.textContent = text
    newUserChatElement.setAttribute('id', 'user_question') // to get user_question css
    newUserChatElement.className = 'col-lg-4 col-12 align-self-end align-items-end' // to get bootstrap
}

// CREATES DIV CHILD BOT DESCRIPTION
function addChatElement(text) {
    const chatboxElement = document.getElementById('chatbox')
    const newChatElement = document.createElement('div')

    chatboxElement.appendChild(newChatElement) // adds div child to chatbox parent
    newChatElement.textContent = text
    newChatElement.setAttribute('id', 'bot_reply') // to get description css
    newChatElement.className = 'col-lg-4 col-12 align-self-start align-items-start' // to get bootstrap
}

// CREATES DIV CHILD BOT URL
function addChatElementUrl(text) {
    const chatboxElement = document.getElementById('chatbox')
    const newChatElementUrl = document.createElement('a')

    chatboxElement.appendChild(newChatElementUrl) // adds div child to chatbox parent
    newChatElementUrl.textContent = text
    newChatElementUrl.setAttribute('href', text)
    newChatElementUrl.textContent = '[En savoir plus sur Wikipedia]'
    newChatElementUrl.setAttribute('id', 'bot_reply') // to get description css
    newChatElementUrl.setAttribute('target', '_blank')
    newChatElementUrl.className = 'col-lg-4 col-12 align-self-start align-items-start' // to get bootstrap
}

// CREATES DIV CHILD BOT MAP
function addChatElementMap(latitude, longitude) {
    const chatboxElement = document.getElementById('chatbox')
    const newChatElementMap = document.createElement('div')
    initMap(longitude, latitude)

    chatboxElement.appendChild(newChatElementMap) // ajouter div à chatbox en tant qu'enfant
    newChatElementMap.setAttribute('id', 'map') // lui attribuer un id map
}

// --- AJAX sends input to back --- //
// Creates function that will post data, takes into params route URL and data to send it to back
function sendInput(message) {
    let xhr = new XMLHttpRequest();

    xhr.open('POST', '/result', message);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(message));
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) { // or 'this.' to represent 'xhr'
            let response = JSON.parse(xhr.responseText) // parsing text response from back into JSON
            const bot_reply_description = response['description']
            const bot_reply_url = response['url']
            const longitude = response['longitude']
            const latitude = response['latitude']

            addUserChatElement(message) // Displays user_input to chatbox
            addChatElement(bot_reply_description) // Displays bot_reply with description to chatbox
            addChatElementUrl(bot_reply_url) // Displays bot_reply with url to chatbox

            // Get coordinates
            addChatElementMap(longitude, latitude)
            console.log(`longitude: ${longitude}, latitude: ${latitude}`)

        } else {
        console.log('Il y a eu un problème.')
        }
    }
}

// --- Listen to submit event with user_input --- //

// Create variables with data get from HTML
let form = document.querySelector('.questions');
// Sends the user_input value to the server and chatbox when capture a submit event on form
form.addEventListener('submit', function(event) {
    event.preventDefault();  // avoid default behavior that sends all the form once we click on button
    let input = document.querySelector('#user_input').value; // gets the value of the input that user enters
    sendInput(input); // calls sendInput function and send data to server
    form.reset(); // clears form after sumbitting
})
