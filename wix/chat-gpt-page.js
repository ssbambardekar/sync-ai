/**
 * ChatGpt Page Code.
 * Page Elements:
 * - Text; Themed Text; Heading 6; Roboto Bold; 26
 * - Text; Paragraph; Heading 2; Helvetica; 16; Tag = ChatMessages
 * - Input; Text Box; Rounded corners; 16; 100 character limit; Tag = UserMessage
 * - Button; Themed Button; Onclick = sendMessage_click; Tag = SendButton 
 */
import { add } from 'public/chat-gpt-client';
import { queryGptAssistant } from 'backend/chat-gpt-module.wix.web';

/**
 * Page onReady function
 */
$w.onReady(async function () {
    // Call a client module - code kept for reference
    let sum = add(16, 5);
    
    $w("#ChatMessages").text = "SYNC: Welcome! I am SYNC Genie at your service! How may I help you today?";
});

/**
 * Button 'Send' onClick event handler
 */
export async function sendMessage_click(event) {
    // Get user message
    let userMessage = $w("#UserMessage").value;
    if (userMessage === null || userMessage.trim() === "") {
        return;
    }

    // Disable the controls
    $w("#SendButton").disable();    
    $w("#UserMessage").disable();
    $w("#UserMessage").text = "Sending...."

    // Update the chat messages with user request
    $w("#ChatMessages").text += "\nYOU   : " + userMessage;

    // Send to server
    let gptResponse = await queryGptAssistant(userMessage);
    console.log("Server reply: ", gptResponse);
    
    // Update the chat messages with server response
    $w("#ChatMessages").text += "\nSYNC  : " + gptResponse;
    
    // Enable the controls
    $w("#SendButton").enable();
    $w("#UserMessage").enable();
}