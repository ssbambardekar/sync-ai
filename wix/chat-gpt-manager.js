/**
 * ChatGpt Manager class
 */
import OpenAI from 'openai';

class ChatGptManager {
    /**
     * Constructor
     * @param {string} gptApiKey 
     * @param {string} assistantId 
     */
    constructor(gptApiKey, assistantId) {
        this.gptApiKey = gptApiKey;
        this.assistantId = assistantId;
    }

    /**
     * Initialize function
     * @returns {openAI instance, assistant, assistantthread}
     */
    async _initialize() {
        // Get the openai object
        let openAI = new OpenAI({
            apiKey: this.gptApiKey
        });

        // Get the assistant
        const assistant = await openAI.beta.assistants.retrieve(this.assistantId);
        
        // Create the assistant thread
        const assistantThread = await openAI.beta.threads.create();
        
        return [openAI, assistant, assistantThread];
    }

    /**
     * Query Chat-Gpt Assistant function
     * @param {string} userMessage 
     * @returns Gpt response 
     */
    async queryGptAssistant(userMessage) {
        console.log("Processing user message: ", userMessage);    

        // Initialize the open ai manager
        const [openAI, assistant, assistantThread] = await this._initialize();

        let chatResponse = "";
        try {
            // Create the message
            const message = await openAI.beta.threads.messages.create(
                assistantThread.id,
                {
                    "role": "user",
                    "content": userMessage
                });

            // Create the run
            let run = await openAI.beta.threads.runs.create(
                assistantThread.id,
                {
                    "assistant_id": assistant.id,
                });

            // Wait for the run to complete
            while (run.status === "queued" || run.status === "in_progress") {
                // Retrieve the run status
                run = await openAI.beta.threads.runs.retrieve(assistantThread.id, run.id);
            }

            if (run.status === "failed") {
                throw run.last_error;        
            }

            // Retrieve all the messages added after our last user message
            let messages = await openAI.beta.threads.messages.list(
                assistantThread.id,
                {
                    "order": "asc",
                    "after": message.id
                });
          
            return messages?.data[0]?.content[0]?.text?.value            
        } 
        catch (err) {
            chatResponse = "Server Overload. Please try later.";
            console.log("Error in querying gpt. Error: ", err);
        }

        return chatResponse;
    }

    /**
     * Query Chat-Gpt function
     * @param {string} userMessage 
     * @returns Gpt response 
     */    
    async queryGpt(userMessage) {        
        console.log("Processing user message: ", userMessage);    

        // Initialize the open ai manager
        const [openAI, aiAssistant, runThread] = await this._initialize();

        let chatResponse = "";
        try {
            // Call the chat gpt api
            chatResponse = await openAI.chat.completions.create({
                messages: [{ role: 'user', content: userMessage }],
                model: 'gpt-3.5-turbo',
            })
        } 
        catch (err) {
          chatResponse = "Server Overload. Please try later.";
          console.log("Error in querying gpt. Error: ", err.error);
        }

        return chatResponse;
    }
}

export {ChatGptManager};

/**
 * Unit test code
 */
console.log("Javascript Node debug session");

let chatGptManager = new ChatGptManager(
    "sk-proj-52L2jSNP6HA0bAXtahSUT3BlbkFJKaYaJIczr4ptsGdsXt4j",
    "asst_HpLlNUjgW0mJYPmD21ZqjSIP");

//chatGptManager.queryGptAssistant("Test");
//chatGptManager.queryGpt("Test");