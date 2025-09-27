let orderButton = document.querySelector("#order")
let orderProductDiv = document.querySelector(".order-product")
let backButton = document.querySelector(".back_btn")

function clickOrderButton(){
    orderProductDiv.classList.remove("order-product-out")
    orderProductDiv.classList.add("order-product-in")
}


orderButton.addEventListener("click", clickOrderButton)


function backIntoItemInfo(){
    orderProductDiv.classList.remove("order-product-in")
    orderProductDiv.classList.add("order-product-out")
}

backButton.addEventListener("click", backIntoItemInfo)
