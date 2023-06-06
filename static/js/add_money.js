import { getCSRFTokenFromCookie } from "./csrf.js";


const addMoneyButton = document.getElementById("addmoney-btn");
const amount = document.getElementById("amount");

const incorrect_amount_msg = document.getElementById("incorrect-pin-msg")

async function  makePayment(amount){

    const myHeaders = new Headers();

    myHeaders.append("X-CSRFToken", getCSRFTokenFromCookie());

    const formdata = new FormData();

    formdata.append("amount", amount);
    try {
        const requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: formdata,
          redirect: 'follow'
        };
    
        const response = await fetch("/dashboard/addmoney", requestOptions);

        const result = await response.json()

        addMoneyButton.disabled = false;


        if (response.status == 200){

            window.location.href = result.data.checkout


        }
        else{
            incorrect_amount_msg.innerHTML = `<i class='fa-solid fa-circle-exclamation'></i> ${result.message}`
    
        }

      } 
      catch (error) {
        console.log('error', error);
      }

}





amount.addEventListener("input", async (event) =>{

    if (+amount.value < 100){
        
        incorrect_amount_msg.innerHTML = "<i class='fa-solid fa-circle-exclamation'></i> The minimum deposit amount is NGN 100.00";
        addMoneyButton.disabled = true;


    }

    else if (+amount.value >= 100){

        incorrect_amount_msg.innerHTML = ""
        addMoneyButton.disabled = false;

    }

});

addMoneyButton.addEventListener("click", async ()=>{

    incorrect_amount_msg.innerHTML = ""

    addMoneyButton.disabled = true

    await makePayment(amount.value);

})