document.addEventListener("DOMContentLoaded", function () {
    const resetBtn = document.getElementById("reset-mfa-btn");
    const modal = document.getElementById("reset-mfa-modal");
    const cancelBtn = document.getElementById("cancel-reset-btn");
    const modalBox = modal.querySelector(".modal-box");

    function openModal() {
        modal.classList.remove("hidden");
    }

    function closeModal() {
        modal.classList.add("hidden");
    }

    resetBtn.addEventListener("click", function (event) {
        event.preventDefault();
        openModal();
    });

    cancelBtn.addEventListener("click", function () {
        closeModal();
    });

    modal.addEventListener("click", function (event) {
        if (!modalBox.contains(event.target)) {
            closeModal();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && !modal.classList.contains("hidden")) {
            closeModal();
        }
    });
});