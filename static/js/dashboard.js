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



const divsToRemove = document.querySelectorAll('#loading-div');

// console.log(divsToRemove)

// divsToRemove.forEach(function(div) {

//     div.classList.add('fade-out');

//     setTimeout(function() {
//         div.remove();

//     }, 1000);
// });

// setTimeout(function() {
//     let div1 = createDiv('New Div 1');
//     let div2 = createDiv('New Div 2');
//     let div3 = createDiv('New Div 3');
//     container.appendChild(div1);
//     container.appendChild(div2);
//     container.appendChild(div3);
//     animateFadeIn([div1, div2, div3]);
// }, 500);



// function animateFadeIn(divs) {
//   divs.forEach(function(div) {
//     div.classList.add('fade-in');
//   });
// }










// for (const transactionBlock of trasactionBlocks) {

//     transactionsContainer.appendChild(transactionBlock.getMainBlockRow())
    
// }











