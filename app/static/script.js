// JavaScript file

// QUERY SELECTOR
document.querySelector('.send_btn').addEventListener('click', function (event) {
    event.preventDefault();  // avoid default behavior that sends all the form once we click on button
    const user_input = document.querySelector('#user_input').value; // gets the value of the input that user enters
    console.log(user_input); // prints user input on console
    document.querySelector('#user_question').textContent = user_input; // updates the user_question part with the value entered by user on user_input
});

console.log("fin");


// GET ELEMENTS
/*document.getElementsByClassName('send_btn').addEventListener('click', function () {
    const user_input = document.getElementById('user_input').value;
    console.log(user_input);
});
console.log("fin");*/






