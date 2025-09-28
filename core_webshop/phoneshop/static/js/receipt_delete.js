document.querySelectorAll(".delete-receipt").forEach(button => {
    button.addEventListener("click", function() {
        const receiptId = this.getAttribute("data-id");

        // console.log(receiptId)

        fetch(`/receipts/delete/${receiptId}/`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                this.closest("tr").remove();
            } else {
                alert("Hiba történt a törlés során" + (data.error || ''));
            }
        });
    });
});

function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim()
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue
}
