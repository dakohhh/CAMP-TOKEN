function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Look for the cookie that starts with "csrftoken="
            if (cookie.substring(0, 10) === 'csrftoken=') {
                // Extract the value of the csrf token
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}



const modal = document.getElementById("modal");

const modal_close_btn = document.getElementById("modal_close_btn")

const next_btn = document.getElementById("next_btn");

const refund_student_btn = document.getElementById("refund_student_btn");

const form = document.getElementById("pay_form")




next_btn.addEventListener("click", async ()=>{

	modal.style.display = "block";
})



modal_close_btn.addEventListener("click", async ()=>{

	modal.style.display = "none";
    pay_msg.textContent = "";


})





form.addEventListener("submit", async (event)=>{
    event.preventDefault()

    refund_student_btn.disabled = true;

    const formData = new FormData(form)

    const myHeaders = new Headers();

    const csrf_token = getCSRFToken();

    myHeaders.append("X-CSRFToken", csrf_token);
    myHeaders.append("Cookie", `csrftoken=${csrf_token}`);


    
    const response = await fetch(form.action, {
        method: 'POST',
        headers: myHeaders,
        body: formData,
        redirect: "follow"
    });

    if (response.redirected){
        window.location = response.url
    }

    const result = await response.json();
    

    if (result.success === false){
        pay_msg.textContent = result.message;
    }


    refund_student_btn.disabled = false;

    
    
})