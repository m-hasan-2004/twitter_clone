document.addEventListener('DOMContentLoaded', () => {
    const profileForm = document.querySelector('.profile-update form');
    const passwordForm = document.querySelector('.change-password form');
    const emailForm = document.querySelector('.change-email form');
    const logoutForm = document.querySelector('.user-profile form');

    const modal = document.getElementById('popup-modal');
    const messageText = document.getElementById('popup-message');
    const closeBtn = document.querySelector('.close-btn');

    // Function to show the modal
    const showModal = (message) => {
        messageText.textContent = message;
        modal.style.display = 'flex'; // Show modal
        setTimeout(() => {
            closeModal();
        }, 3000); // Auto-close after 3 seconds
    };

    // Function to close the modal
    const closeModal = () => {
        modal.style.display = 'none'; // Hide modal
    };

    // Close modal when 'x' is clicked
    closeBtn.addEventListener('click', closeModal);

    // Show modal and then submit form
    const handleFormSubmission = (form, message) => {
        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent form submission
            showModal(message); // Show popup
            setTimeout(() => {
                form.submit(); // Submit form after modal closes
            }, 3000); // Wait 3 seconds before form submission
        });
    };

    // Attach the modal to each form submission
    if (profileForm) {
        handleFormSubmission(profileForm, 'Profile updated successfully!');
    }

    if (passwordForm) {
        handleFormSubmission(passwordForm, 'Password changed successfully!');
    }

});