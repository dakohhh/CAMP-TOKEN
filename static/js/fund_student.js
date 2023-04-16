

async function get_user(){
    const response = await fetch(`/get_user`, {
        method: 'GET',
    });

    const result = await response.json()

    return result

}


const fund_wallet_btn = document.getElementById("fund_wallet_button");

const amount_input = document.getElementById("amount_id")

const description_input = document.getElementById("description")



fund_wallet_btn.addEventListener("click", async ()=>{


    const user = await get_user();
    payWithMonnify(+amount_input.value, user.data.first_name, user.data.last_name, user.data.email, description.value);

});



function payWithMonnify(amount, first_name, last_name, email, description) {
    MonnifySDK.initialize({
        amount: amount,
        currency: "NGN",
        reference: new String((new Date()).getTime()),
        customerFullName: `${first_name} ${last_name}`,
        customerEmail: "wisdomdakoh@gmail.com",
        apiKey: "",
        contractCode: "",
        paymentDescription: description,
        isTestMode: true,
        metadata: {
            "name": "",
            "age": 45
        },

        onLoadStart: () => {
            console.log("loading has started");
        },
        onLoadComplete: () => {
            console.log("SDK is UP");
        },

        onComplete: function(response) {
            //Implement what happens when the transaction is completed.
            console.log(response);
        },
        onClose: function(data) {
            //Implement what should happen when the modal is closed here
            console.log(data);
        }
    });
}




document.addEventListener('input', function(event) {
    if (amount_input.value.length >= 1 && description_input.value.length >= 3) {
        fund_wallet_btn.disabled = false;
    } else {
        fund_wallet_btn.disabled = true;
    }

  });

fund_wallet_btn.disabled = true;
