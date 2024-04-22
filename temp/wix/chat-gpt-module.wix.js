/**
 * ChatGpt Module Wix Backend Code
 */
import { Permissions, webMethod } from "wix-web-module";
import { ChatGptManager } from "backend/chat-gpt-manager";
import { getSecret } from "wix-secrets-backend";

 /**
 * Query Chat-Gpt Assistant function
 * @param {string} userMessage 
 * @returns Gpt response 
 */
export const queryGptAssistant = webMethod(
    Permissions.Anyone,
    async (userMessage) => {
        // Get the secrets
        const gptApiKey = await getSecret("gpt_api_key");
        const assistantId = await getSecret("assistant_id");

        // Create the chat gpt manager
        let chatGptManager = new ChatGptManager(gptApiKey, assistantId);
     
        return await chatGptManager.queryGptAssistant(userMessage);
    }
);

/**
 * Query Chat-Gpt function
 */
export const queryGpt = webMethod(
    Permissions.Anyone,
    async (userMessage) => {
         // Get the secrets
         const gptApiKey = await getSecret("gpt_api_key");
         const assistantId = await getSecret("assistant_id");
 
         // Create the chat gpt manager
         let chatGptManager = new ChatGptManager(gptApiKey, assistantId);
      
         return await chatGptManager.queryGpt(userMessage);
    }
);