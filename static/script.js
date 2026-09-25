
function confirmDelete() {
    return confirm("Are you sure you want to delete this expense?");
}



document.addEventListener("DOMContentLoaded", function () {

    const messages = document.querySelectorAll(".flash-message");

    messages.forEach(function (message) {

        setTimeout(function () {
            message.style.opacity = "0";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 3000);

    });

});