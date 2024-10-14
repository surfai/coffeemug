## CallTaiphi

The `CallTaiphi` class is a key component of the Taiphi library, responsible for managing API calls to language models and handling various aspects of the conversation flow. Here's an overview of its main features and functionalities:

1. **Initialization**: The class is initialized with configuration parameters, including the model to use, temperature, and other settings.

2. **Conversation Management**: It maintains a conversation history, allowing for context-aware interactions with the language model.

3. **API Interaction**: The class handles API calls to the specified language model, supporting different providers like OpenAI and Anthropic.

4. **Prompt Handling**: It processes user inputs and system prompts, combining them with the conversation history to generate appropriate queries for the language model.

5. **Response Processing**: The class manages the responses from the language model, including parsing, formatting, and updating the conversation history.

6. **Error Handling**: It includes mechanisms to handle various errors that may occur during API calls or processing.

7. **Customization**: The class allows for customization of various parameters, such as the number of tokens to consider from the conversation history.

8. **Utility Functions**: It provides utility methods for tasks like counting tokens, truncating conversations, and formatting prompts.

The `CallTaiphi` class serves as a central component for interacting with language models in the Taiphi library, abstracting away much of the complexity involved in managing conversations and API interactions.

::: taiphi.calltaiphi

