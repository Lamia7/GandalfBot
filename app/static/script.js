// Module that contains function that listens to submit event and ajax function
import { addUserChatElement, addChatElement, addChatElementUrl, addChatElementMap, addBotNoAnswerElement } from './conversation.js'

/*function refreshScreen () {
  const chatbox = document.getElementById('chatbox')
  chatbox.scrollIntoView()

}
*/

// --- AJAX sends input to back --- //
// Creates function that will post data, takes into params route URL and data to send it to back
function sendInput(message) {
    let xhr = new XMLHttpRequest();

    xhr.open('POST', '/result', message);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(message));
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) { // or 'this.' to represent 'xhr'
            addUserChatElement(message) // Displays user_input to chatbox
            // Get infos from response
            let response = JSON.parse(xhr.responseText) // parsing text response from back into JSON

            if ('description' in response) {
                const bot_reply_description = response['description']
                const bot_reply_url = response['url']
                const longitude = response['longitude']
                const latitude = response['latitude']

                // Bot
                addChatElement(bot_reply_description) // Displays bot_reply with description to chatbox
                addChatElementUrl(bot_reply_url) // Displays bot_reply with url to chatbox
                addChatElementMap(longitude, latitude) // Displays bot_reply with map
                console.log(`longitude: ${longitude}, latitude: ${latitude}`)
                // refreshScreen()
            } else {
                console.log('Il y a eu un problème.')
                addBotNoAnswerElement()
            }
        }
    }
}

// --- Listen to submit event with user_input --- //

// Sends the user_input value to the server and chatbox click ENTER on keyboard
let input = document.querySelector('#user_input')
input.addEventListener('keyup', function(event) {
    if (event.keyCode === 13) {
        event.preventDefault() // avoid default behavior that sends all the form once we click on button
        let input_value = input.value // gets the value of the input that user enters
        sendInput(input_value) // calls sendInput function and send data to server
        input.value = '' // clears form after sumbitting
    }
})

// Sends the user_input value to the server and chatbox click on button
const button = document.querySelector('#button')
button.addEventListener('click', function(event) {
        event.preventDefault()
        let input_value = input.value
        sendInput(input_value)
        input.value = ''
})