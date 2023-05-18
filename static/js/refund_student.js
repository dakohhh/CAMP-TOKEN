

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