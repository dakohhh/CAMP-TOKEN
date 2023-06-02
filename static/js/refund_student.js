

import {getCSRFTokenFromCookie} from "./csrf.js"


async function makeRefund(transaction_id, trans_pin) {

    const csrf_token = getCSRFTokenFromCookie();

    const formdata = new FormData();
    formdata.append("transaction_id", `${transaction_id}`);
    formdata.append("trans_pin", `${trans_pin}`);
    
    const  myHeaders = new Headers();
    myHeaders.append("X-CSRFToken", csrf_token);
    
    const response = await fetch(`/dashboard/m/refund/${transaction_id}`, {
        method: 'POST',
        body: formdata,
        headers: myHeaders,  
        redirect: 'follow'
    });
    
    const result = await response.json();

    return result
}




const pay_button = document.getElementById("pay-btn");

const pin_inputs_field = document.getElementById("pin-inputs-field");

const pin_inputs = pin_inputs_field.querySelectorAll('input[type="password"]');



pin_inputs_field.addEventListener('input', function() {
    let allFilled = true;
  
    pin_inputs.forEach((input)=> {
        if (input.value === '') {
            allFilled = false;
        }
    });
  
    if (allFilled) {
        pay_button.disabled = false;
    } 
    else {
        pay_button.disabled = true;
    }
});



pay_button.addEventListener("click", async ()=>{

    const active_page = window.location.href.split("/");

    const transaction_id = active_page[active_page.length - 1]

    let trans_pin = ""

    const pin_inputs = pin_inputs_field.querySelectorAll('input[type="password"]');

    pin_inputs.forEach((inputs)=>{

        trans_pin += inputs.value
    })


    const result = await makeRefund(transaction_id, trans_pin)

    const successModal = document.getElementById('staticBackdrop2');
    const pay_modal = document.getElementById('staticBackdrop')


    if (result.success === true){
        

        pay_modal.classList.remove('show')
        pay_modal.style.display = 'none'
        pay_modal.setAttribute('aria-hidden', 'true');

        successModal.classList.add('fade');

        setTimeout(function() {
            successModal.classList.add('show');
        }, 100);

        successModal.style.display = 'block';
        successModal.setAttribute('aria-hidden', 'false');

        

        const pay_suc_or_fail_img = document.getElementById("pay_suc_or_fail_img")

        const pay_success_fail_info = document.getElementById("pay-success-fail-info")

        const pay_success_fail_reciept_no = document.getElementById("pay-success-fail-reciept-no")

        const pay_success_fail_message = document.getElementById("pay-success-fail-message")

        const redirect_msg = document.getElementById("redirect-msg")


        pay_success_fail_info.textContent = "Success!"

        pay_success_fail_message.textContent = result.message

        pay_success_fail_reciept_no.textContent = `Reciept No: ${result.data.transaction_id}`

        pay_suc_or_fail_img.src = "/static/img/check.png"

        payRedirectToDashboard(redirect_msg);


    }

    else if (result.success === false && result.data === "00"){

        pay_modal.classList.remove('show')
        pay_modal.style.display = 'none'
        pay_modal.setAttribute('aria-hidden', 'true');

        successModal.classList.add('fade');

        setTimeout(function() {
            successModal.classList.add('show');
        }, 100);

        successModal.style.display = 'block';
        successModal.setAttribute('aria-hidden', 'false');

        const pay_suc_or_fail_img = document.getElementById("pay_suc_or_fail_img")

        const pay_success_fail_info = document.getElementById("pay-success-fail-info")

        const pay_success_fail_message = document.getElementById("pay-success-fail-message")

        const redirect_msg = document.getElementById("redirect-msg")


        pay_success_fail_info.textContent = "Transaction Failed"

        pay_success_fail_message.textContent = result.message

        pay_suc_or_fail_img.src = "/static/img/x-mark.png"

        payRedirectToDashboard(redirect_msg);
    

        
    }

    else if (result.success === false && result.data === "01"){
        const incorrect_pin_msg = document.getElementById("incorrect-pin-msg")

        incorrect_pin_msg.textContent = result.message        

    }

    else if (result.success === false && typeof result.data === "object"){

        pay_modal.classList.remove('show')
        pay_modal.style.display = 'none'
        pay_modal.setAttribute('aria-hidden', 'true');

        successModal.classList.add('fade');

        setTimeout(function() {
            successModal.classList.add('show');
        }, 100);

        successModal.style.display = 'block';
        successModal.setAttribute('aria-hidden', 'false');

        const pay_suc_or_fail_img = document.getElementById("pay_suc_or_fail_img")

        const pay_success_fail_info = document.getElementById("pay-success-fail-info")

        const pay_success_fail_reciept_no =  document.getElementById("pay-success-fail-reciept-no")

        const pay_success_fail_message = document.getElementById("pay-success-fail-message")

        const redirect_msg = document.getElementById("redirect-msg")


        pay_success_fail_info.textContent = "Transaction Failed"

        pay_success_fail_message.textContent = result.message

        pay_success_fail_reciept_no.textContent = `Reciept No: ${result.data.transaction_id}`

        pay_suc_or_fail_img.src = "/static/img/x-mark.png"

        payRedirectToDashboard(redirect_msg);        

    }

});



