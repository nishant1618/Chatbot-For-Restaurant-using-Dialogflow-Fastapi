// Toggle chatbot visibility
const chatbotToggle = document.getElementById('chatbot-toggle');
const chatbotContainer = document.getElementById('chatbot-container');

const chatbotClose = document.getElementById('chatbot-close');

chatbotToggle.addEventListener('click', () => {
    chatbotContainer.style.display = 'flex';
    chatbotToggle.style.display = 'none';
});

chatbotClose.addEventListener('click', () => {
    chatbotContainer.style.display = 'none';
    chatbotToggle.style.display = 'inline-block';
});

// Integrate Dialogflow chatbot

