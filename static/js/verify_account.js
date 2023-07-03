

const form = document.getElementById("verify_form")

const pin_inputs_field = document.getElementById("pin-inputs-field")

const pin_inputs = pin_inputs_field.querySelectorAll('input[type="password"]');

const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

const verifyAccountButton = document.getElementById("verify-btn")


pin_inputs_field.addEventListener('input', function() {
    let allFilled = true;
  
    pin_inputs.forEach((input)=> {
        if (input.value === '') {
            allFilled = false;
        }
    });
  
    if (allFilled) {
        verifyAccountButton.disabled = false;
    } 
    else {
        verifyAccountButton.disabled = true;
    }

});


verifyAccountButton.addEventListener("click", async ()=>{

    const form = document.getElementById("verify_form")

    let trans_pin = ""

    const pin_inputs = form.querySelectorAll('input[type="password"]');

    pin_inputs.forEach((inputs)=>{

        trans_pin += inputs.value
    })

    const currentURLParts = window.location.href.split("/");

    const extractedURL = currentURLParts[currentURLParts.length - 2] + "/" + currentURLParts[currentURLParts.length - 1]

    const postURL = `/accounts/verify/${extractedURL}`

    console.log(postURL)

    
    let formdata = new FormData();
    formdata.append("transaction_pin", `${trans_pin}`);
    formdata.append("csrfmiddlewaretoken", `${csrfToken}`);
 
    const response = await fetch(postURL, {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
    });
    
    const result = await response.json();

    console.log(result);


    const modal = new bootstrap.Modal(document.getElementById('staticBackdrop2'));


    if (result.success == true){

        const suc_or_fail_img = document.getElementById("suc_or_fail_img")

        const success_fail_info = document.getElementById("success_fail_info")

        const redirect_msg = document.getElementById("redirect_msg")

        const success_fail_message = document.getElementById("success_fail_message")

        suc_or_fail_img.src = "https://res.cloudinary.com/do1iufmkf/image/upload/v1686433502/static/img/check.011bb4cf6289.png"

        success_fail_info.textContent = "Account Verified"

        payRedirectToDashboard(redirect_msg);
  
        modal.show()
    }

    else{

        const suc_or_fail_img = document.getElementById("suc_or_fail_img")

        const success_fail_info = document.getElementById("success_fail_info")

        const success_fail_message = document.getElementById("success_fail_message")

        suc_or_fail_img.src = "https://res.cloudinary.com/do1iufmkf/image/upload/v1686433506/static/img/x-mark.a142a3b18fe3.png"

        success_fail_info.textContent = "Oops"

  
        modal.show()


    }

    





})