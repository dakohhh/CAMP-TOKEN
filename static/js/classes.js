import { transactionBlurComponent, mainTransactionComponent, noTransactionCompnent, transactionRowComponent } from "./components.js"


export class Transaction {
    constructor(amount, date_added, recipient, sender, transaction_id, transaction_status, transaction_type, was_refunded){

        this.amount = amount
        this.date_added = date_added
        this.recipient = recipient
        this.sender = sender
        this.transaction_id = transaction_id
        this.transaction_status = transaction_status
        this.transaction_type = transaction_type
        this.was_refunded = was_refunded

    }

    getTransactionRow(){
        const isCredit = this.transaction_type === 2

        return transactionRowComponent(this.recipient, this.amount, "10:00 AM", isCredit)
    }

}


export class MainBlockTransaction {
    constructor(date, transactions) {
        let arrTrans = [];

        for (const i of transactions) {

            const _  = new Transaction(i.amount, i.date_added, i.recipient, i.sender, i.transaction_id, i.transaction_status, i.transaction_type, i.was_refunded)

            arrTrans.push(_)
        }

        this.date = date;
        this.transactions = arrTrans;

    }

    getMainBlockRow(){

        return mainTransactionComponent(this.date, this.transactions)
    }

}

