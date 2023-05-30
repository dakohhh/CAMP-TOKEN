import { transactionBlurComponent, mainTransactionComponent, noTransactionCompnent } from "./components.js"


const balance = document.getElementById("user-balance");

balance.addEventListener("click", async () =>{

    balance.classList.toggle('blur');
})


async function getTransactions() {

    const requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    const request = await fetch("/get_student_transactions", requestOptions)

    const result = await request.json()

    return result

    
}



let transactionsContainer = document.getElementById('transactions');


transactionsContainer.appendChild(noTransactionCompnent())

// for (let index = 0; index < 6; index++) {

//     transactionsContainer.appendChild(transactionBlurComponent())
    
// }



const replaceBtn = document.getElementById("replace-btn")

replaceBtn.addEventListener("click", async()=>{
    const blurComponents = document.querySelectorAll("#loading-div");

    blurComponents.forEach((component)=>{

        component.classList.add('fade-out');

        setTimeout(function() {
            component.remove();
        }, 500);
   })

   setTimeout(function() {
    const div1 = mainTransactionComponent();
    const div2 = mainTransactionComponent();
    const div3 = mainTransactionComponent();
    const div4 = mainTransactionComponent();
    const div5 = mainTransactionComponent();


    div1.classList.add('fade-in')
    div2.classList.add('fade-in')
    div3.classList.add('fade-in')
    div4.classList.add('fade-in')
    div5.classList.add('fade-in')

    transactionsContainer.appendChild(div1);
    transactionsContainer.appendChild(div2);
    transactionsContainer.appendChild(div3);
    transactionsContainer.appendChild(div4);
    transactionsContainer.appendChild(div5);

  }, 500);


})









