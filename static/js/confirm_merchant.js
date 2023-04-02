

const merchant_id_input = document.getElementById("id_merchant_id")
const ammount_input = document.getElementById("id_amount")


merchant_id_input.addEventListener("input", async (event) =>{

    if (merchant_id_input.value.length == 10){

        merchant_id_input.disabled = true

        //ADD feth  here

        ammount_input.disabled = false;
        



    }


})


ammount_input.disabled = true

