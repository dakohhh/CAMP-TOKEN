

function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Look for the cookie that starts with "csrftoken="
            if (cookie.substring(0, 10) === 'csrftoken=') {
                // Extract the value of the csrf token
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}



const merchant_id_input = document.getElementById("id_merchant_wallet_id")

const ammount_input = document.getElementById("id_amount")

const wallet_id_msg = document.getElementById("wallet_id_msg")

const next_btn = document.getElementById("next_btn");

const trans_form = document.getElementById("trans_form");

const show_merchant = document.getElementById("show_merchant");

const show_amount = document.getElementById("show_amount");

merchant_id_input.addEventListener("input", async (event) =>{

    if (merchant_id_input.value.length < 10){
        
        wallet_id_msg.textContent = "";

        ammount_input.disabled = true

        next_btn.disabled = true
    }

    else if (merchant_id_input.value.length > 10){

        merchant_id_input.value = merchant_id_input.value.slice(0, 10);
    }

    else if (merchant_id_input.value.length == 10){

        const csrf_token = getCSRFToken();

        const response = await fetch(`/confirm_merchant_wallet_id?id=${merchant_id_input.value}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'csrftoken' : csrf_token
            }
          });

        const result = await response.json();
        
        if (result.success === true){

            wallet_id_msg.textContent = result.data

            ammount_input.disabled = false;

            show_merchant.textContent = result.data;


        }
        else{
            wallet_id_msg.textContent = "Wallet ID Not Found";

        }

        
    }


})

ammount_input.addEventListener("input", async()=>{

    if(ammount_input.value.length >= 1){
        next_btn.disabled = false
    }

    else if(ammount_input.value.length < 1){

        next_btn.disabled = true

        show_merchant.textContent = merchant_id_input.value;
        
    }

    show_amount.textContent = ammount_input.value;

})

trans_form.addEventListener("submit", async (event)=>{

    event.preventDefault();

})

ammount_input.disabled = true
next_btn.disabled = true



