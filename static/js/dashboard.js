import { MainBlockTransaction, Transaction } from "./classes.js";
import { noTransactionCompnent, viewMoreButtonComponent } from "./components.js";


async function getTransactions(page=1) {

    const requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    const request = await fetch(`/get_student_transactions?page=${page}`, requestOptions)

    const result = await request.json()

    return result

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

async function goToAddMoney(){
    window.location.href = "/addmoney"
}


const balance = document.getElementById("user-balance");

balance.addEventListener("click", async () =>{

    balance.classList.toggle('blur');
})



const transactionsContainer = document.getElementById('transactions');


const user = await getUser();
const transactionRequest = await getTransactions()
const mainTransactions = transactionRequest.data;
let currentTransactionPageNo = 1;

let prevMainTransactionBlock = null;



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


    prevMainTransactionBlock = trasactionBlocks[trasactionBlocks.length -1]
    
    
    for (const transactionBlock of trasactionBlocks) {
    
        const  transactionBlockElement = transactionBlock.getMainBlockRow();
    
    
        transactionBlockElement.classList.add('fade-in')
    
        setTimeout(function() {
            transactionsContainer.appendChild(transactionBlockElement)    
        }, 1000);
        
    }

    const viewMoreButton = viewMoreButtonComponent();

    viewMoreButton.addEventListener("click", async ()=>{
        currentTransactionPageNo = currentTransactionPageNo + 1


        const moreTransactionRequest = await getTransactions(currentTransactionPageNo);

        const moreTransactions = moreTransactionRequest.data;


        // if prevMainTransactionBlock.date


        for (const key in moreTransactions) {
            
            if (key === prevMainTransactionBlock.date){

                let onPrevTrasaction  = []

                const prevTransactionBlocks = document.querySelectorAll("#main-tran-sec");

                const lastTransactionBlock = prevTransactionBlocks[prevTransactionBlocks.length -1]


                for (const item of moreTransactions[key]) {

                    const _  = new Transaction(
                        item.amount, 
                        item.date_added, 
                        item.merchant, 
                        item.student, 
                        item.transaction_id, 
                        item.transaction_status, 
                        item.transaction_type, 
                        item.was_refunded, 
                        item.formated_time, 
                        user.is_merchant
                    )

                    onPrevTrasaction.push(_)

                }

                for (const item of onPrevTrasaction){

    
                    const transactionBlockElement = item.getTransactionRow();
                        
                    transactionBlockElement.classList.add('fade-in')
                
                    setTimeout(function() {
                        lastTransactionBlock.appendChild(transactionBlockElement)    
                    }, 1000);
                        

                }

            }

            else{

                let moreTransactionBlocks = [];

                moreTransactionBlocks.push(new MainBlockTransaction(key, moreTransactions[key], user.is_merchant))

                prevMainTransactionBlock = moreTransactionBlocks[moreTransactionBlocks.length - 1]

                for (const transactionBlock of moreTransactionBlocks) {

                    const  transactionBlockElement = transactionBlock.getMainBlockRow();
                        
                    transactionBlockElement.classList.add('fade-in')
                
                    setTimeout(function() {
                        transactionsContainer.appendChild(transactionBlockElement)    
                    }, 1000);
                    
                }

            }
        }
    
        if (!moreTransactionRequest.extra_vals.page_detials.has_next){
            setTimeout(function() {
                viewMoreButton.remove()

            }, 1000);

        }

    })

    try{
        if (transactionRequest.extra_vals.page_detials.has_next){

            setTimeout(function() {
                transactionsContainer.appendChild(viewMoreButton)
    
            }, 1000);
    
        }
    
    }
    catch(e){
        console.log("error", error)
    }

}

















