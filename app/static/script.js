// JavaScript file


// Creates function that will post data, takes into params route URL and data
function sendInput(message) {
    let xhr = new XMLHttpRequest();

    xhr.open('POST', '/result', message);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(message));
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) { // 'this' represents 'xhr'
            let response = JSON.parse(xhr.responseText) // parsing text response into JSON
            document.querySelector('#bot_reply').textContent = response; // displays bot_reply to chatbox
            //console.log(`Réponse côté JS POSTresponse:  ${response}`)
            //return response
        } else {
        console.log('pas ok');
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
    })


/* APRES EVENT.PREVENTDEFAULT() LIGNE 8
let user_input = document.querySelector('#user_input').value; // gets the value of the input that user enters
console.log(user_input); // prints user input on console
document.querySelector('#user_question').textContent = user_input;
*/


// GET ELEMENTS
/*document.getElementsByClassName('send_btn').addEventListener('click', function () {
    const user_input = document.getElementById('user_input').value;
    console.log(user_input);
});
form.reset(); // clears form after sumbitting
console.log("fin");




/*
-------------
// What to do when submit form (make it a function later)
form.addEventListener('submit', function (event) {
    event.preventDefault();  // avoid default behavior that sends all the form once we click on button
    console.log(user_input); // prints user input on console
    document.querySelector('#user_question').textContent = user_input;


    // Sends user_input content to the server
    fetch('/result', {
        method: "POST",
        body: document.querySelector('#user_input').value // data that I am sending
    });

})
---------------

// QUERY SELECTOR
let send_btn = document.querySelector('.send_btn')
send_btn.addEventListener('click', function (event) {
    event.preventDefault();  // avoid default behavior that sends all the form once we click on button
    const user_input = document.querySelector('#user_input').value; // gets the value of the input that user enters
    console.log(user_input); // prints user input on console
    document.querySelector('#user_question').textContent = user_input;*/ // updates the user_question part with the value entered by user on user_input







