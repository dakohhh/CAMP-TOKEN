
const merchant_id_input = document.getElementById("id-merchant-id");

const show_merchant =  document.getElementById("show_merchant")

const amount_input = document.getElementById("amount")

const next_btn = document.getElementById("next-btn")

const modal_merchant_name =  document.getElementById("modal-merchant-name")

const modal_amount = document.getElementById("modal-amount")

const pin_inputs_field = document.getElementById("pin-inputs-field")

const pin_inputs = pin_inputs_field.querySelectorAll('input[type="password"]');

const pay_button = document.getElementById("pay-btn");



merchant_id_input.addEventListener("input", async (event) =>{

    if (merchant_id_input.value.length < 10){
        
        show_merchant.textContent = "";

        show_merchant.classList.remove("form-text", 'prm-color-green', 'pay-msg', 'prm-color-red');

        amount_input.disabled = true;


    }

    else if (merchant_id_input.value.length > 10){

        merchant_id_input.value = merchant_id_input.value.slice(0, 10);
    }

    else if (merchant_id_input.value.length == 10){
        const requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };
        

        const request = await fetch(`/confirm_merchant_wallet?id=${merchant_id_input.value}`, requestOptions)

        const result = await request.json()

        if (result.success){

            show_merchant.classList.add('form-text', 'prm-color-green', 'pay-msg')

            const iElement = document.createElement('i');

            iElement.classList.add('fa-solid', 'fa-circle-check');

            const spanElement = document.createElement('span');

            spanElement.textContent = ` ${result.data}`;

            show_merchant.appendChild(iElement);

            show_merchant.appendChild(spanElement);

            amount_input.disabled = false;

        }
        else{
            const iElement = document.createElement('i');

            iElement.classList.add('fa-solid', 'fa-circle-exclamation');

            const spanElement = document.createElement('span');

            spanElement.textContent = ' INCORRECT MERCHANT ID';

            show_merchant.classList.add('form-text', 'prm-color-red', 'pay-msg')

            show_merchant.appendChild(iElement);

            show_merchant.appendChild(spanElement);

        }
        
    }
})




amount_input.addEventListener("input", async ()=>{

    amount_input.value = amount_input.value.replace(/^0+/, "");

    if (amount_input.value.length >= 3){
        next_btn.disabled = false

    }

    else if (amount_input.value.length < 3){

        next_btn.disabled = true

    }
})



next_btn.addEventListener("click", async ()=>{

    modal_merchant_name.textContent = show_merchant.textContent;

    modal_amount.textContent = `₦${amount_input.value}`;

    modal_merchant_name.style.fontWeight = "bold"

    modal_amount.style.fontWeight = "bold"


})




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
  


pay_button.addEventListener("click", ()=>{

    let merchant_id = merchant_id_input.value;

    let amount  = amount_input.value;

    let trans_pin = ""

    const pin_inputs = pin_inputs_field.querySelectorAll('input[type="password"]');

    pin_inputs.forEach((inputs)=>{

        trans_pin += inputs.value
    })

    console.log(merchant_id, amount, trans_pin)

    let test_trans_req = 1

    const successModal = document.getElementById('staticBackdrop2');
    const pay_modal = document.getElementById('staticBackdrop')


    if (test_trans_req === 1){
        

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

        pay_success_fail_info.textContent = "Success!"

        pay_success_fail_reciept_no.textContent = `Reciept No: 5dc3790abfde4cbdd309432`

        pay_suc_or_fail_img.src = "/static/img/check.png"

        const redirect_msg = document.getElementById("redirect-msg")

        let count = 3;

        const countdownInterval = setInterval(() => {
            count--;
            if (count > 0) {
                redirect_msg.textContent = `Redirecting you in ${count}...`;
            } 
            
            else {
                
                clearInterval(countdownInterval);

                redirect_msg.textContent = 'Redirecting now...';

                setTimeout(() => {

                    window.location.href = '/dashboard/s/';

                }, 3000);
            }
            
        }, 1000);

    }

    else if (test_trans_req === 2){


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

        pay_success_fail_info.textContent = "Transaction Failed"

        pay_success_fail_reciept_no.textContent = `Reciept No: 5dc3790abfde4cbdd309432`

        pay_suc_or_fail_img.src = "/static/img/x-mark.png"
        
        const redirect_msg = document.getElementById("redirect-msg")

        let count = 3;

        const countdownInterval = setInterval(() => {
            count--;
            if (count > 0) {
                redirect_msg.textContent = `Redirecting you in ${count}...`;
            } 
            
            else {
                
                clearInterval(countdownInterval);

                redirect_msg.textContent = 'Redirecting now...';

                setTimeout(() => {

                    window.location.href = '/dashboard/s/';

                }, 3000);
            }
            
        }, 1000);

    }

    else if (test_trans_req === 3){
        const incorrect_pin_msg = document.getElementById("incorrect-pin-msg")

        incorrect_pin_msg.textContent = "Incorrect Pin"        

    }


    

})