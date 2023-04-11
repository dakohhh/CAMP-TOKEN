

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


// FROM DJANGO
const merchant_id_input = document.getElementById("id_merchant_wallet_id")

const ammount_input = document.getElementById("id_amount")

const wallet_id_msg = document.getElementById("wallet_id_msg")

const next_btn = document.getElementById("next_btn");




//MODAL FORM 

const modal = document.getElementById("modal");

const show_merchant = document.getElementById("show_merchant");

const show_amount = document.getElementById("show_amount");

const form = document.getElementById("pay_form")

const pay_msg = document.getElementById("pay_msg")

const modal_close_btn = document.getElementById("modal_close_btn")

// POST FORM PARAM
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
            wallet_id_msg.textContent = result.message;

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

    modal.style.display = "block";

})

modal_close_btn.addEventListener("click", async ()=>{

    modal.style.display = "none";
    pay_msg.textContent = "";

})




form.addEventListener("submit", async (event)=>{
    event.preventDefault()

    pay_merchant_button.disabled = true;

    const formData = new FormData(form)

    const myHeaders = new Headers();

    const csrf_token = getCSRFToken();

    myHeaders.append("X-CSRFToken", csrf_token);
    myHeaders.append("Cookie", `csrftoken=${csrf_token}`);

    


    const response = await fetch(`/pay_merchant`, {
        method: 'POST',
        headers: myHeaders,
        body: formData,
        redirect: "follow"
    });

    if (response.redirected){
        window.location = response.url
    }

    const result = await response.json();
    

    if (result.success === false){
        pay_msg.textContent = result.message;
    }


    pay_merchant_button.disabled = false;

    
    
})



function openModal() {
}
		
function closeModal() {
    modal.style.display = "none";
}





ammount_input.disabled = true
next_btn.disabled = true





