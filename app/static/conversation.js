// Module that contains functions to create conversation elements (user's questions and bot replies)
import { initMap } from './map.js'

const chatboxElement = document.getElementById('chatbox')
let divclassUser = "d-flex justify-content-end mb-4 "
let divclassBot = "d-flex justify-content-start mb-4"

// CREATES DIV CHILD USER INPUT
export function addUserChatElement (text) {
    const divUser = document.createElement('div')
    chatboxElement.appendChild(divUser) // adds div child to chatbox parent

    const newUserChatElement = document.createElement('div')
    divUser.appendChild(newUserChatElement) // adds div child to divUser parent
    newUserChatElement.textContent = text
    newUserChatElement.setAttribute('id', 'user_question') // to get user_question css
    divUser.className = divclassUser // to get divUser Bootstrap
}

// CREATES DIV CHILD BOT DESCRIPTION
export function addChatElement (text) {
    const divBot = document.createElement('div')
    chatboxElement.appendChild(divBot) // adds div child to chatbox parent

    const newChatElement = document.createElement('div')
    divBot.appendChild(newChatElement) // adds div child to chatbox parent
    newChatElement.textContent = text
    newChatElement.setAttribute('id', 'bot_reply') // to get description css
    divBot.className = divclassBot // to get bootstrap
}

// CREATES DIV CHILD BOT URL
export function addChatElementUrl (text) {
    const divBot = document.createElement('div')
    chatboxElement.appendChild(divBot) // adds div child to chatbox parent

    const newChatElementUrl = document.createElement('a')

    divBot.appendChild(newChatElementUrl) // adds div child to chatbox parent
    newChatElementUrl.textContent = text
    newChatElementUrl.setAttribute('href', text)
    newChatElementUrl.textContent = '[En savoir plus sur Wikipedia]'
    newChatElementUrl.setAttribute('id', 'bot_reply') // to get description css
    newChatElementUrl.setAttribute('target', '_blank')
    divBot.className = divclassBot // to get bootstrap
}

let mapIdCounter = 0 // counter used later to generate different map ids
let mapId = ''
// CREATES DIV CHILD BOT MAP
export function addChatElementMap (latitude, longitude) {
    const newChatElementMap = document.createElement('div')

    mapIdCounter += 1
    mapId = 'map'.concat(mapIdCounter)
    newChatElementMap.setAttribute('id', mapId) // sets the mapId (one per map)

    chatboxElement.appendChild(newChatElementMap) // adds div child to chatbox parent
    newChatElementMap.className = divclassBot
    initMap(longitude, latitude, mapId)
}