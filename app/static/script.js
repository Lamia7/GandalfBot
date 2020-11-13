// JavaScript file


// Creates function that will post data, takes into params route URL and data
function sendInput(message) {
    let xhr = new XMLHttpRequest();

    xhr.open('POST', '/result', message);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(message));
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) { // or 'this.' to represent 'xhr'
            let response = JSON.parse(xhr.responseText) // parsing text response into JSON
             // displays bot_reply to chatbox
            document.querySelector('#bot_reply').textContent = response;
        } else {
        console.log('Il y a eu un problème.');
        }
    }
};

// Create variables with data get from HTML
let form = document.querySelector('.questions');

// Sends the user_input value to the server and chatbox when capture a submit event on form
form.addEventListener('submit', function(event) {
    event.preventDefault();  // avoid default behavior that sends all the form once we click on button
    let input = document.querySelector('#user_input').value; // gets the value of the input that user enters
    document.querySelector('#user_question').textContent = input; // displays user_input to chatbox
    sendInput(input); // calls sendInput function and send data to server
    form.reset(); // clears form after sumbitting
})
