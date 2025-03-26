document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll(".task-checkbox");

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", function () {
            const taskId = this.dataset.taskId;
            const completeUrl = `complete/${taskId}/`;

            console.log("Sending GET request to:", completeUrl);

            fetch(completeUrl, { method: "GET" })
            .then(response => response.json())
            .then(data => {
                console.log("Task completed:", data);
            })
            .catch(error => console.error("Error completing task:", error))
            .finally(() => {
                window.location.reload();
            });
        });
    });
});