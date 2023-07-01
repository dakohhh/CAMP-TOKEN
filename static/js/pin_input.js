
const inputs = document.querySelectorAll('.pin-input input');

inputs.forEach((input, index) => {
    input.addEventListener('input', e => {

        const val = input.value;
        const sanitizedVal = val.replace(/[^0-9.]/g, '');

        input.value = sanitizedVal;

        if (input.value.length >= input.maxLength) {
            if (inputs[index + 1]) {
                inputs[index + 1].focus();
            }
        }

        if (e.inputType === 'deleteContentBackward' && input.value.length === 0) {
            if (inputs[index - 1]) {
                inputs[index - 1].focus();
            }
        }
    });
});