// Module that contains functions to create conversation elements (user's questions and bot replies)
import { initMap } from './map.js'

const chatboxElement = document.getElementById('chatbox')

// CREATES DIV CHILD USER INPUT
export function addUserChatElement (text) {
    const newUserChatElement = document.createElement('div')

    chatboxElement.appendChild(newUserChatElement) // adds div child to chatbox parent
    newUserChatElement.textContent = text
    newUserChatElement.setAttribute('id', 'user_question') // to get user_question css
    newUserChatElement.className = 'col-lg-4 col-12 align-self-end align-items-end' // to get bootstrap

    newUserChatElement.scrollIntoView(true)
}

// CREATES DIV CHILD BOT DESCRIPTION
export function addChatElement (text) {
    const newChatElement = document.createElement('div')

    chatboxElement.appendChild(newChatElement) // adds div child to chatbox parent
    newChatElement.textContent = text
    newChatElement.setAttribute('id', 'bot_reply') // to get description css
    newChatElement.className = 'col-lg-4 col-12 align-self-start align-items-start' // to get bootstrap

    newChatElement.scrollIntoView(true)
}

// CREATES DIV CHILD BOT URL
export function addChatElementUrl (text) {
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

let mapIdCounter = 0 // counter used later to generate different map ids
let mapId = ''
// CREATES DIV CHILD BOT MAP
export function addChatElementMap (latitude, longitude) {
    const newChatElementMap = document.createElement('div')

    // chatboxElement.appendChild(newChatElementMap)
    mapIdCounter += 1
    mapId = 'map'.concat(mapIdCounter)
    newChatElementMap.setAttribute('id', mapId) // sets the mapId (one per map)

    chatboxElement.appendChild(newChatElementMap) // adds a div child to chatbox
    initMap(longitude, latitude, mapId)

    newChatElementMap.scrollIntoView(true)
}