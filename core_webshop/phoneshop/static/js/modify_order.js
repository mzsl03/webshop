let modifyOrderButtons = document.querySelectorAll(".modify_order_button")

function modify_order_status(event) {
    const button = event.target
    const row = button.closest("tr")
    const statusCell = row.children[5]


    const currentStatus = statusCell.textContent.trim()


    const select = document.createElement("select")
    const statuses = [
        {value: "feldolgozás_alatt", label: "Feldolgozás alatt"},
        {value: "kiszállítva", label: "Kiszállítva"},
        {value: "törölve", label: "Törölve"}
    ]

    let currentValue = statuses.find(s => s.label === statusCell.textContent.trim())?.value


    statuses.forEach(s => {
        const option = document.createElement("option")
        option.value = s.value
        option.textContent = s.label
        if (s.value === currentValue) option.selected = true
        select.appendChild(option)
    })


    statusCell.textContent = ""
    statusCell.appendChild(select)


    button.textContent = "Mentés"


    button.removeEventListener("click", modify_order_status)
    button.addEventListener("click", function save_status() {
        const newStatus = select.value


        fetch(`/order/update/${button.id}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({status: newStatus})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                if (data.redirect_url) {
                    window.location.href = data.redirect_url
                } else {
                    const selectedLabel = statuses.find(s => s.value === newStatus).label
                    statusCell.textContent = selectedLabel
                    button.textContent = "Szerkesztés"

                    button.removeEventListener("click", save_status)
                    button.addEventListener("click", modify_order_status)
                }
            } else {
                alert("Hiba a státusz frissítésekor!")
            }
        })
        .catch(err => {
            console.error("Fetch error:", err)
            alert("Hálózati hiba történt!")
        })
    })
}


function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";")
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim()
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue
}

modifyOrderButtons.forEach(but => {
    but.addEventListener("click", modify_order_status)
})
