/**
 * ChatGpt Page Code
 */
import { add } from 'public/chat-gpt-client'
import { queryGptAssistant } from 'backend/chat-gpt-module.wix.web';

/**
 * Page onReady function
 */
$w.onReady(async function () {
    // Call a client module
    let sum = add(16, 5);
    
    $w("#ChatMessages").text = "SYNC: Welcome! How may I help you today?"
});

/**
 * Button 'Send' onClick event handler
 */
export async function sendMessage_click(event) {
    // Get user message
    let userMessage = $w("#userMessage").value
    if (userMessage === null || userMessage.trim() === "") {
        return
    }

    // Update the chat messages with user request
    $w("#ChatMessages").text += "\nYOU  : " + userMessage

    // Send to server
    let gptResponse = await queryGptAssistant(userMessage)     
    console.log("Server reply: ", gptResponse)
    
    // Update the chat messages with server response
    $w("#ChatMessages").text += "\nSYNC  : " + gptResponse
}