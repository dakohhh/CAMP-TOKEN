

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


const submit_merchant_id = document.getElementById("merchant_id")
const submit_ammount = document.getElementById("amount_id")
const pay_merchant_button = document.getElementById("pay_merchant_btn")

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

        merchant_id_input.disabled = true


        const csrf_token = getCSRFToken();

        const response = await fetch(`/confirm_merchant_wallet_id?id=${merchant_id_input.value}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'csrftoken' : csrf_token
            }
          });

        
        const result = await response.json();
        
        if (result.success){

            wallet_id_msg.textContent = result.data

            ammount_input.disabled = false;

            show_merchant.textContent = result.data;

            merchant_id_input.disabled = false
            



        }
        else{
            wallet_id_msg.textContent = "Wallet ID Not Found";

            merchant_id_input.disabled = false


        }

        
    }


})

ammount_input.addEventListener("input", async()=>{

    if(ammount_input.value.length >= 1){
        next_btn.disabled = false


    }

    else if(ammount_input.value.length < 1){

        next_btn.disabled = true



        
    }

    show_amount.textContent = ammount_input.value;

})


next_btn.addEventListener("click", async ()=>{
    

    submit_merchant_id.value = merchant_id_input.value;
    submit_ammount.value = ammount_input.value;

})






pay_merchant_button.addEventListener("click", async (event)=>{

    event.preventDefault()

    const pay_msg = document.getElementById("pay_msg")

    const form = document.getElementById("pay_form")
    

    const formData = new FormData(form)

    const myHeaders = new Headers();

    const csrf_token = getCSRFToken();

    myHeaders.append("X-CSRFToken", csrf_token);
    myHeaders.append("Cookie", `csrftoken=${csrf_token}`);

    
    pay_merchant_button.disabled = true

    const response = await fetch(`/dashboard/s/pay`, {
        method: 'POST',
        headers: myHeaders,
        body: formData,
        redirect: "follow"
      });


    
    const result = await response.json();

    const redirect_url = `/payment_success`

    if (response.redirected){
        window.location = redirect_url;
    }
    else if (!result.success){
        pay_msg.textContent = result.msg;
        pay_merchant_button.disabled = false;
    }

})





ammount_input.disabled = true
next_btn.disabled = true





