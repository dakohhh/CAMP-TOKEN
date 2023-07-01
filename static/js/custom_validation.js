const phoneNumberInput = document.querySelector('#id_phone_number');

phoneNumberInput.addEventListener('input', () => {
    if (phoneNumberInput.value.length === 10) {

        phoneNumberInput.setCustomValidity('');
        phoneNumberInput.classList.remove('is-invalid');
        phoneNumberInput.classList.add('is-valid');
    }


    else if (phoneNumberInput.value.length > 10){
        phoneNumberInput.value = phoneNumberInput.value.slice(0, 10);
    }

    else {
        phoneNumberInput.setCustomValidity('Phone number must be 10-digits');
        phoneNumberInput.classList.remove('is-valid');
        phoneNumberInput.classList.add('is-invalid');
    }
});

const passwordInput = document.querySelector('#id_password1');

const confirmpasswordInput = document.querySelector("#id_password2")


passwordInput.addEventListener('input', () => {

    if (passwordInput.value !== confirmpasswordInput.value) {

        confirmpasswordInput.setCustomValidity('');
        confirmpasswordInput.classList.remove('is-valid');
        confirmpasswordInput.classList.add('is-invalid');
    }

    if (passwordInput.value.length >= 8) {

        passwordInput.setCustomValidity('');
        passwordInput.classList.remove('is-invalid');
        passwordInput.classList.add('is-valid');
    }

    else {
        passwordInput.setCustomValidity('');
        passwordInput.classList.remove('is-valid');
        passwordInput.classList.add('is-invalid');
    }
});



confirmpasswordInput.addEventListener('input', () => {
    if (confirmpasswordInput.value.length >= 8 && confirmpasswordInput.value === passwordInput.value) {

        confirmpasswordInput.setCustomValidity('');
        confirmpasswordInput.classList.remove('is-invalid');
        confirmpasswordInput.classList.add('is-valid');
    }

    else {
        confirmpasswordInput.setCustomValidity('');
        confirmpasswordInput.classList.remove('is-valid');
        confirmpasswordInput.classList.add('is-invalid');
    }
});


const businessNameInput = document.querySelector("#id_business_name")

console.log(businessNameInput)

businessNameInput.addEventListener("input", ()=>{

    if (businessNameInput.value.length >=5) {

        businessNameInput.setCustomValidity('');
        businessNameInput.classList.remove('is-invalid');
        businessNameInput.classList.add('is-valid');
    }
    
    else {
        businessNameInput.setCustomValidity('');
        businessNameInput.classList.remove('is-valid');
        businessNameInput.classList.add('is-invalid');    
    
    }

})




