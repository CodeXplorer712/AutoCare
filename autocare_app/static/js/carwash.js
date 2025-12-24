// Car Wash Booking Page JavaScript

// Set minimum date to today
document.addEventListener('DOMContentLoaded', function () {
    const dateInput = document.getElementById('booking_date');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }
});

// Open booking modal with selected package
function openBookingModal(packageValue, packageName, packagePrice) {
    const modal = document.getElementById('bookingModal');
    document.getElementById('selectedPackageName').textContent = packageName;
    document.getElementById('selectedPackagePrice').textContent = packagePrice;
    document.getElementById('wash_package').value = packageValue;

    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
}

// Close booking modal
function closeBookingModal() {
    const modal = document.getElementById('bookingModal');
    modal.classList.remove('show');
    document.body.style.overflow = 'auto';
}

// Close modal when clicking outside
window.addEventListener('click', function (event) {
    const modal = document.getElementById('bookingModal');
    if (event.target === modal) {
        closeBookingModal();
    }
});

// Close modal with Escape key
window.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        closeBookingModal();
    }
});

// Handle booking form submission
document.addEventListener('DOMContentLoaded', function () {
    const bookingForm = document.getElementById('bookingForm');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = {
                customer_name: document.getElementById('customer_name').value,
                phone: document.getElementById('phone').value,
                car_number: document.getElementById('car_number').value,
                address: document.getElementById('address').value,
                wash_package: document.getElementById('wash_package').value,
                booking_date: document.getElementById('booking_date').value,
                booking_time: document.getElementById('booking_time').value
            };

            // Submit the form
            this.submit();
        });
    }
});
