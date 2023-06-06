import { getCSRFTokenFromCookie } from "./csrf.js";


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

      } 
      catch (error) {
        console.log('error', error);
      }

}




const addMoneyButton = document.getElementById("addmoney-btn");
const amount = document.getElementById("amount");

const incorrect_amount_msg = document.getElementById("incorrect-pin-msg")





amount.addEventListener("input", async (event) =>{

    if (+amount.value < 100){
        
        incorrect_amount_msg.textContent = "The minimum deposit amount is NGN 100.00";
        addMoneyButton.disabled = true;


    }

    else if (+amount.value >= 100){

        incorrect_amount_msg.textContent = ""
        addMoneyButton.disabled = false;

    }

});

addMoneyButton.addEventListener("click", async ()=>{

    await makePayment(amount.value);

})