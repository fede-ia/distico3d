document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const nameInput = document.getElementById('name');
    const phoneInput = document.getElementById('phone');
    const formSuccess = document.getElementById('formSuccess');

    // Validación del formulario
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Resetear errores
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
        document.querySelectorAll('.form-control').forEach(el => el.classList.remove('error'));
        
        let isValid = true;

        // Validar nombre
        if (nameInput.value.trim().length < 3) {
            document.getElementById('nameError').textContent = 'El nombre debe tener al menos 3 caracteres';
            nameInput.classList.add('error');
            isValid = false;
        }

        // Validar teléfono (solo números, mínimo 8)
        const phoneRegex = /^\d+$/;
        if (!phoneRegex.test(phoneInput.value) || phoneInput.value.length < 8) {
            document.getElementById('phoneError').textContent = 'Ingresa un teléfono válido (mínimo 8 números)';
            phoneInput.classList.add('error');
            isValid = false;
        }

        if (isValid) {
            // Guardar en localStorage (opcional)
            const formData = {
                name: nameInput.value.trim(),
                phone: phoneInput.value.trim(),
                businessType: document.getElementById('businessType').value,
                services: Array.from(document.querySelectorAll('input[name="service"]:checked')).map(el => el.value),
                message: document.getElementById('message').value.trim(),
                timestamp: new Date().toISOString()
            };
            localStorage.setItem('lastContact', JSON.stringify(formData));

            // Mostrar mensaje de éxito
            formSuccess.textContent = `¡Gracias ${formData.name}! Te respondo a la brevedad.`;
            formSuccess.style.display = 'block';

            // Resetear formulario
            contactForm.reset();

            // Ocultar mensaje después de 5 segundos
            setTimeout(() => {
                formSuccess.style.display = 'none';
            }, 5000);
        }
    });

    // Cargar datos previos si existen
    const lastContact = localStorage.getItem('lastContact');
    if (lastContact) {
        const data = JSON.parse(lastContact);
        nameInput.value = data.name || '';
        phoneInput.value = data.phone || '';
    }
});
