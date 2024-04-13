/**
 * ChatGpt Module Code
 */

/**
 * Imports
 */
import { Permissions, webMethod } from "wix-web-module";
import OpenAI from 'openai';
import { getSecret } from 'wix-secrets-backend';

/**
 * Initialize function
 */
async function initialize() {
    const gpt_api_key = await getSecret("gpt_api_key");
    let openAI = new OpenAI({
        apiKey: gpt_api_key
    });

    console.log("Server modules initialized");

    return openAI;
}

/**
 * Query Chat-Gpt function
 */
export const queryGpt = webMethod(
    Permissions.Anyone,
    async (request) => {
        // Initialize the open ai manager
        let openAI = await initialize();

        let chatCompletion = "";
        try {
            // Call the chat gpt api
            chatCompletion = await openAI.chat.completions.create({
                messages: [{ role: 'user', content: 'Say this is a test' }],
                model: 'gpt-3.5-turbo',
            })
        } 
        catch (err) {
          chatCompletion = "Server Overload. Please try later.";
          console.log("Error in querying gpt.", err);
        }

        return chatCompletion;
    }
);