import { MainBlockTransaction } from "./classes.js";
import { noTransactionCompnent, viewMoreButtonComponent } from "./components.js";


async function getTransactions() {

    const requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    const request = await fetch("/get_student_transactions", requestOptions)

    const result = await request.json()

    return result.data

}

async function getUser(){

    const requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    const request = await fetch("/get_user_data", requestOptions)

    const result = await request.json()

    return result.data

}



const balance = document.getElementById("user-balance");

balance.addEventListener("click", async () =>{

    balance.classList.toggle('blur');
})



const transactionsContainer = document.getElementById('transactions');


const user = await getUser();
const mainTransactions = await getTransactions();


const divsToRemove = document.querySelectorAll('#loading-div');

divsToRemove.forEach(function(div) {

    div.classList.add('fade-out');

    setTimeout(function() {
        div.remove();

    }, 1000);
});



let trasactionBlocks = [];

if (Object.keys(mainTransactions).length == 0 ){

    const noTransaction = noTransactionCompnent()

    noTransaction.classList.add('fade-in');


    setTimeout(function() {
        transactionsContainer.appendChild(noTransaction)

    }, 1000);

}
else{

    for (const transactions in mainTransactions) {
        trasactionBlocks.push(new MainBlockTransaction(transactions, mainTransactions[transactions], user.is_merchant))
    }
    
    
    
    for (const transactionBlock of trasactionBlocks) {
    
        const  transactionBlockElement = transactionBlock.getMainBlockRow();
    
        console.log(transactionBlockElement)
    
        transactionBlockElement.classList.add('fade-in')
    
        setTimeout(function() {
            transactionsContainer.appendChild(transactionBlockElement)    
        }, 1000);
        
    }

    setTimeout(function() {
        transactionsContainer.appendChild(viewMoreButtonComponent())

    }, 1000);

}

















