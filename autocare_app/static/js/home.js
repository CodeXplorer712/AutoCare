// Home page JavaScript

// Scroll to services section when clicking BOOK SERVICE button
function scrollToServices() {
    const promoSection = document.getElementById('promo-section');
    const navbar = document.querySelector('.navbar');
    if (promoSection) {
        const navbarHeight = navbar ? navbar.offsetHeight : 0;
        const elementPosition = promoSection.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - navbarHeight;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    }
}

// Handle scroll effect for navbar visibility
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    const scrollPosition = window.scrollY;

    // Show entire navbar when scrolled down 100px
    if (scrollPosition > 100) {
        navbar.classList.add('show');
    } else {
        navbar.classList.remove('show');
    }
});

// Emergency Modal Functions
function openEmergencyModal() {
    const modal = document.getElementById('emergencyModal');
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
}

function closeEmergencyModal() {
    const modal = document.getElementById('emergencyModal');
    modal.classList.remove('show');
    document.body.style.overflow = 'auto';
}

// Close modal when clicking outside
window.addEventListener('click', function (event) {
    const modal = document.getElementById('emergencyModal');
    if (event.target === modal) {
        closeEmergencyModal();
    }
});

// Close modal with Escape key
window.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        closeEmergencyModal();
    }
});

// Handle emergency form submission
document.addEventListener('DOMContentLoaded', function() {
    const emergencyForm = document.getElementById('emergencyForm');
    if (emergencyForm) {
        emergencyForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = {
                contactNumber: document.getElementById('contactNumber').value,
                carNumber: document.getElementById('carNumber').value,
                location: document.getElementById('location').value
            };

            // For now, just show an alert (you can replace this with actual API call)
            alert('Emergency request submitted!\n\nContact: ' + formData.contactNumber +
                '\nCar: ' + formData.carNumber +
                '\nLocation: ' + formData.location +
                '\n\nOur team will contact you shortly for emergency assistance!');

            // Reset form and close modal
            this.reset();
            closeEmergencyModal();
        });
    }
});
