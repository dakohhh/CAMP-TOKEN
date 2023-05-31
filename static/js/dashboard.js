import { transactionBlurComponent, mainTransactionComponent, noTransactionCompnent } from "./components.js"
import { Transaction, MainBlockTransaction } from "./classes.js";


async function getTransactions() {

    const requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    const request = await fetch("/get_student_transactions", requestOptions)

    const result = await request.json()

    return result.data

}



const balance = document.getElementById("user-balance");

balance.addEventListener("click", async () =>{

    balance.classList.toggle('blur');
})



let transactionsContainer = document.getElementById('transactions');

// for (let index = 0; index < 6; index++) {

//     transactionsContainer.appendChild(transactionBlurComponent())
    
// }



const mainTransactions = await getTransactions();

let trasactionBlocks = [];


for (const transactions in mainTransactions) {


    trasactionBlocks.push(new MainBlockTransaction(transactions, mainTransactions[transactions]))

}

for (const transactionBlock of trasactionBlocks) {

    transactionsContainer.appendChild(transactionBlock.getMainBlockRow())
    
}











