// Scroll chat messages to the bottom on page load
window.addEventListener("load", function () {
    const chatContainer = document.querySelector(".chat-container");
    const chatMessages = document.getElementById("chatMessages");

    if (chatMessages) {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    if (chatContainer instanceof HTMLElement) {
        const resetUrl = chatContainer.dataset.resetUrl;
        if (resetUrl && window.location.pathname !== resetUrl) {
            window.history.replaceState(null, "", resetUrl);
        }
    }
});
