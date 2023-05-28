/**
 * Adds two numbers together.
 * @param {HTMLElement} modalToClose
 * @returns {HTMLElement}
 */

export function modalCancel(modalToClose = null){

    const divElement = document.createElement('div');
    divElement.classList.add('text-center', 'pay-cancel');

    const buttonElement = document.createElement('button');
    buttonElement.setAttribute('type', 'button');
    buttonElement.setAttribute('style', 'color: #40196d;');
    buttonElement.setAttribute('data-bs-dismiss', 'modal');
    buttonElement.textContent = 'Cancel';

    if (modalToClose){
   
        buttonElement.addEventListener("click", ()=>{
            
            modalToClose.classList.remove('show')
            modalToClose.style.display = 'none'
            modalToClose.setAttribute('aria-hidden', 'true');
        })
    }

    divElement.appendChild(buttonElement);

    return divElement;

}



export function payRedirectToDashboard(redirectMessage = null){

    let count = 3;

    const countdownInterval = setInterval(() => {
        count--;
        if (count > 0) {
            if (redirectMessage){redirectMessage.textContent = `Redirecting you in ${count}...`;}
        }

        else {
            
            clearInterval(countdownInterval);

            if (redirectMessage){redirectMessage.textContent = 'Redirecting now...';}

            setTimeout(() => {

                window.location.href = '/dashboard/s/';

            }, 3000);
        }
        
    }, 1000);

}