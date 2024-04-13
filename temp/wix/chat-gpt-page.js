/**
 * ChatGpt Page Code
 */

/**
 * Imports
 */
import { add } from 'public/test-gpt-client.js'
import { queryGpt } from 'backend/chat-gpt-module.web';

/**
 * Page onReady function
 */
$w.onReady(async function () {
    // Print hello world:
    console.log("Hello world!");

    let sum = add(6, 7);
    console.log("Client Call: ", sum);

    $w("#ChatMessages").text = "SYNC: Welcome! How may I help you today?"
});

/**
 * Button 'Send' onClick event handler
 */
export async function sendMessage_click(event) {
    // Get user message
    let userMessage = $w("#userMessage").value
    console.log("User message: ", userMessage)
    if (userMessage === null || userMessage.trim() === "") {
        return
    }

    // Update the chat messages with user request
    $w("#ChatMessages").text += "\nYOU  : " + userMessage

    // Send to server
    let gptResponse = await queryGpt(userMessage)     
    console.log("Server reply: ", gptResponse)
    
    // Update the chat messages with server response
    $w("#ChatMessages").text += "\nSYNC  : " + gptResponse
}