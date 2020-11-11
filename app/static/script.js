// JavaScript file

// Create variables with data get from HTML
let form = document.querySelector('.questions');

    // Creates function that will post data, takes into params route URL and data
    function postData(url, data) {
        // using fetch(), a JS function
        return fetch(url, {
            method: "POST",
            body: data // data that I am sending
        })
    }

    // Sends the user_input value to the server and chatbox when capture a submit event on form
    form.addEventListener('submit', function (event) {
        event.preventDefault();  // avoid default behavior that sends all the form once we click on button
        let message = document.querySelector('#user_input').value; // gets the value of the input that user enters
        postData("/result", message); // calls postdata function and send data to server
        console.log(message); // prints user input on console
        document.querySelector('#user_question').textContent = message; // sends user_input to chatbox

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







