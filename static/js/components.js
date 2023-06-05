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



export function transactionBlurComponent(){

    const transactionDiv = document.createElement("div")

    transactionDiv.id = "loading-div"

    transactionDiv.className = "go-down-sm row transaction d-flex align-items-center justify-content-start"

    return transactionDiv;

}



export function dateRowComponent(date = "Today"){

    let dateDiv = document.createElement('div');
    dateDiv.className = 'trans-date d-flex align-items-center justify-content-start';
    dateDiv.textContent = date; 
    
    return dateDiv;

}


export function transactionRowComponent(merchantName, amount , isCredit, isFailed, time="10:00 AM"){

    let transactionRow = document.createElement('div');
    transactionRow.className = 'row transaction d-flex align-items-center justify-content-start';

    let transactionInfo1 = document.createElement('div');
    transactionInfo1.className = 'col transaction-info-1';

    let span1 = document.createElement('span');
    span1.textContent = merchantName;

    let p1 = document.createElement('p');
    p1.textContent = time;

    transactionInfo1.appendChild(span1);
    transactionInfo1.appendChild(p1);

    let transactionInfo2 = document.createElement('div');
    transactionInfo2.className = 'col transaction-info-2 d-flex align-items-center justify-content-end';

    let innerDiv1_2 = document.createElement('div');

    let span1_2 = document.createElement('span');

    if (isCredit && !isFailed){
        span1_2.className = 'prm-color-green';
    }
    else if (!isCredit && !isFailed){
        span1_2.className = '';
    }
    else{
        span1_2.className = 'prm-color-red';
    }

    span1_2.textContent = isCredit ? `+₦${amount}` : `₦${amount}`;

    innerDiv1_2.appendChild(span1_2);
    transactionInfo2.appendChild(innerDiv1_2);

    transactionRow.appendChild(transactionInfo1);
    transactionRow.appendChild(transactionInfo2);

    return transactionRow

}


export function mainTransactionComponent(date, transactions) {

    let mainDiv = document.createElement('div');
    mainDiv.className = 'row transaction d-flex align-items-center justify-content-start';

    mainDiv.appendChild(dateRowComponent(date));

    for (const transaction of transactions) {

        mainDiv.appendChild(transaction.getTransactionRow());
    }

    return mainDiv;

}


export function noTransactionCompnent(){

    const mainHead = document.createElement("h5")

    mainHead.className = "go-down-bg prm-color-grey text-center";

    mainHead.textContent = "No Transactions yet!"

    return mainHead

}



export function viewMoreButtonComponent(){
    const mainDiv = document.createElement("div");

    mainDiv.className = "go-down-sm row d-flex align-items-center justify-content-start"

    const button = document.createElement("button");

    const iElement = document.createElement("i");

    iElement.className = "prm-color fa-solid fa-magnifying-glass";

    button.className = "prm-color text-center view-more-btn";

    const buttonText = document.createTextNode(" View More");

    button.appendChild(iElement);
    
    button.appendChild(buttonText)
    
    mainDiv.appendChild(button);

    return mainDiv;

}