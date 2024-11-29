document.addEventListener("DOMContentLoaded", () => {
    const message = document.getElementById("message");

    if (message) {
        setTimeout(() => {
            message.remove();
        }, 7000);
    }
});
