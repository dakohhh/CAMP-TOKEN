
const merchant_id_input = document.getElementById("id-merchant-id");
const show_merchant  = document.getElementById("show_merchant");



merchant_id_input.addEventListener("input", async (event) =>{

    if (merchant_id_input.value.length < 10){
        
        show_merchant.textContent = "";

    }

    else if (merchant_id_input.value.length > 10){

        merchant_id_input.value = merchant_id_input.value.slice(0, 10);
    }

    else if (merchant_id_input.value.length == 10){

        const iElement = document.createElement('i');

        iElement.classList.add('fa-solid', 'fa-circle-check');

        const spanElement = document.createElement('span');

        spanElement.textContent = ' BUNLAB VENTURES.';

        show_merchant.appendChild(iElement);

        show_merchant.appendChild(spanElement);
        
    }
})




const pay_button = document.getElementById("pay-btn");

pay_button.addEventListener("click", ()=>{

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

                window.location.href = '/dashboard_student.html';

            }, 3000);
        }
        
      }, 1000);

})