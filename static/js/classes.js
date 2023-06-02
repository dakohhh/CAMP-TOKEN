import { transactionBlurComponent, mainTransactionComponent, noTransactionCompnent, transactionRowComponent } from "./components.js"


export class Transaction {
    constructor(amount, date_added, recipient, sender, transaction_id, transaction_status, transaction_type, was_refunded, is_for_merchant){

        this.amount = amount
        this.date_added = date_added
        this.recipient = recipient
        this.sender = sender
        this.transaction_id = transaction_id
        this.transaction_status = transaction_status
        this.transaction_type = transaction_type
        this.was_refunded = was_refunded
        this.is_for_merchant = is_for_merchant

    }

    getTransactionRow(){
        let isCredit;

        if (this.is_for_merchant && this.transaction_type === 1){
            isCredit = true
        }
        else if(this.is_for_merchant && this.transaction_type === 2){
            isCredit = false
        }
        else if(this.is_for_merchant ===false && this.transaction_type ===1){
            isCredit = false

        }
        else if(this.is_for_merchant === false && this.transaction_type ===2){
            isCredit = true;
        }

        return transactionRowComponent(this.is_for_merchant ? this.sender : this.recipient, this.amount, isCredit, "10:00 AM")
    }

}


export class MainBlockTransaction {
    constructor(date, transactions, is_for_merchant) {
        let arrTrans = [];

        for (const i of transactions) {

            const _  = new Transaction(i.amount, i.date_added, i.recipient, i.sender, i.transaction_id, i.transaction_status, i.transaction_type, i.was_refunded, is_for_merchant)

            arrTrans.push(_)
        }

        this.date = date;
        this.transactions = arrTrans;

    }

    getMainBlockRow(){

        return mainTransactionComponent(this.date, this.transactions)
    }

}

