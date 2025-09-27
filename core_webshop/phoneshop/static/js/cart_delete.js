console.log("Csatlakozás sikeres")
let delete_buttons = document.querySelectorAll(".delete-item")

function delete_item_from_cart(event) {
    if (event.target.closest("tr")) {
        const itemId = event.target.closest("tr").id
        console.log(itemId)

        fetch(`/cart/delete/${itemId}/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                event.target.closest("tr").remove()
            } else {
                alert("Hiba: " + data.error)
            }
        })
    }
}

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

delete_buttons.forEach(del_but => {
    del_but.addEventListener("click", delete_item_from_cart)
})
