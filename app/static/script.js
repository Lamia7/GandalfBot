// JavaScript file

// CREATES DIV CHILD USER
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
    newChatElement.setAttribute('id', 'description') // to get description css
    newChatElement.className = 'col-lg-4 col-12 align-self-start align-items-start' // to get bootstrap
}

// CREATES DIV CHILD BOT URL
// CREATES DIV CHILD BOT MAP

// AJAX sends input to back
// Creates function that will post data, takes into params route URL and data to send it to back
function sendInput(message) {
    let xhr = new XMLHttpRequest();

    xhr.open('POST', '/result', message);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(message));
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) { // or 'this.' to represent 'xhr'
            let response = JSON.parse(xhr.responseText) // parsing text response from back into JSON
            bot_reply_description = response['description']
            bot_reply_url = response['url']

            // Displays user_input to chatbox
            addUserChatElement(message)

            // Displays bot_reply with description to chatbox
            addChatElement(bot_reply_description) // calls

        } else {
        console.log('Il y a eu un problème.')
        }
    }
};

// Create variables with data get from HTML
let form = document.querySelector('.questions');

// Sends the user_input value to the server and chatbox when capture a submit event on form
form.addEventListener('submit', function(event) {
    event.preventDefault();  // avoid default behavior that sends all the form once we click on button
    let input = document.querySelector('#user_input').value; // gets the value of the input that user enters
    sendInput(input); // calls sendInput function and send data to server
    form.reset(); // clears form after sumbitting
})


