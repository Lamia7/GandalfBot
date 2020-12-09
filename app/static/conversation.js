// Module that contains functions to create conversation elements (user's questions and bot replies)
import { initMap } from './map.js'

// CREATES DIV CHILD USER INPUT
export function addUserChatElement (text) {
    const chatboxElement = document.getElementById('chatbox')
    const newUserChatElement = document.createElement('div')

    chatboxElement.appendChild(newUserChatElement) // adds div child to chatbox parent
    newUserChatElement.textContent = text
    newUserChatElement.setAttribute('id', 'user_question') // to get user_question css
    newUserChatElement.className = 'col-lg-4 col-12 align-self-end align-items-end' // to get bootstrap

    newUserChatElement.scrollIntoView(true)
}

// CREATES DIV CHILD BOT DESCRIPTION
export function addChatElement (text) {
    const chatboxElement = document.getElementById('chatbox')
    const newChatElement = document.createElement('div')

    chatboxElement.appendChild(newChatElement) // adds div child to chatbox parent
    newChatElement.textContent = text
    newChatElement.setAttribute('id', 'bot_reply') // to get description css
    newChatElement.className = 'col-lg-4 col-12 align-self-start align-items-start' // to get bootstrap

    newChatElement.scrollIntoView(true)
}

// CREATES DIV CHILD BOT URL
export function addChatElementUrl (text) {
    const chatboxElement = document.getElementById('chatbox')
    const newChatElementUrl = document.createElement('a')

    chatboxElement.appendChild(newChatElementUrl) // adds div child to chatbox parent
    newChatElementUrl.textContent = text
    newChatElementUrl.setAttribute('href', text)
    newChatElementUrl.textContent = '[En savoir plus sur Wikipedia]'
    newChatElementUrl.setAttribute('id', 'bot_reply') // to get description css
    newChatElementUrl.setAttribute('target', '_blank')
    newChatElementUrl.className = 'col-lg-4 col-12 align-self-start align-items-start' // to get bootstrap

    newChatElementUrl.scrollIntoView(true)
}

// CREATES DIV CHILD BOT MAP
export function addChatElementMap (latitude, longitude) {
    const chatboxElement = document.getElementById('chatbox')
    const newChatElementMap = document.createElement('div')

    chatboxElement.appendChild(newChatElementMap) // ajouter div à chatbox en tant qu'enfant
    newChatElementMap.setAttribute('id', 'map') // lui attribuer un id map
    initMap(longitude, latitude)

    newChatElementMap.scrollIntoView(true)
}