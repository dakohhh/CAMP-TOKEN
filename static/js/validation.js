(() => {
    'use strict';
  
    const forms = document.querySelectorAll('.needs-validation');

  
    Array.from(forms).forEach(form => {

      form.addEventListener('submit', event => {

        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
  
        form.classList.add('was-validated');
      });
  
  
      // Reset validation on input change
      form.querySelectorAll('.form-control').forEach(input => {
        input.addEventListener('input', () => {
          input.classList.remove('is-invalid', 'is-valid');
          input.setCustomValidity('');
        });
      });
    });
  })();
  