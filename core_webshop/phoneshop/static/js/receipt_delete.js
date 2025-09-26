document.querySelectorAll(".delete-receipt").forEach(button => {
    button.addEventListener("click", function() {
        const receiptId = this.getAttribute("data-id");

        fetch(`/receipts/delete/${receiptId}/`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
        })
        .then(response => {
            if (response.ok) {
                this.closest("tr").remove();
            } else {
                alert("Hiba történt a törlés során!");
            }
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
