// Module that contains functions to create conversation elements (user's questions and bot replies)
import { Map } from './map.js'

const chatboxElement = document.getElementById('chatbox')
let divclassUser = "d-flex justify-content-end offset-lg-6 col-lg-6 col-sm-12 offset-sm-0 mb-4"
let divclassBot = "d-flex justify-content-start mb-4 col-lg-6 col-sm-12"

let botIntroSuccess = "Laisse-moi partager avec toi ce que j'en ai appris... "

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
    newChatElement.textContent = botIntroSuccess.concat(text)
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
    const map = new Map()
    map.initMap(longitude, latitude, mapId)
}

// CREATES DIV CHILD BOT NO ANSWER
export function addBotNoAnswerElement () {
    const divBot = document.createElement('div')
    chatboxElement.appendChild(divBot) // adds div child to chatbox parent

    const noAnswerElement = document.createElement('div')
    divBot.appendChild(noAnswerElement) // adds div child to chatbox parent
    noAnswerElement.textContent = "Il me reste tant de contrés à découvrir ..."
    noAnswerElement.setAttribute('id', 'bot_reply') // to get description css
    divBot.className = divclassBot // to get bootstrap
}

// DISPLAYS A SPINNER
export function addSpinner () {
    const divBot = document.createElement('div')
    chatboxElement.appendChild(divBot)

    let spinner = document.createElement('div')
    divBot.appendChild(spinner)
    spinner.style.visibility = 'visible'
    spinner.setAttribute('class', 'spinner spinner-border text-secondary') // class name: spinner and bootstrap details
}

// HIDES SPINNER
export function hideSpinner () {
    let spinnerList = document.getElementsByClassName('spinner')
    document.getElementsByClassName('spinner')
    if (spinnerList) {
        for (let x = 0; x < spinnerList.length; x++) {
          spinnerList[x].style.visibility = 'hidden'
        }
    }
}