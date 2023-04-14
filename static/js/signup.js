

const phoneInput = document.getElementById("id_phone_number");
  
  phoneInput.addEventListener("input", function(event) {

    if (phoneInput.value.length > 10) {
      phoneInput.value = phoneInput.value.slice(0, 10);
    }
});