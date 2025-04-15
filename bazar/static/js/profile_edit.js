document.addEventListener("DOMContentLoaded", function() {
    const editButton = document.getElementById("editButton");
    const saveButton = document.getElementById("saveButton");
    const profileForm = document.getElementById("profileForm");
    const editableFields = ["phone", "telegram", "dormitory"];

    // вкл редактирование полей
    editButton.addEventListener("click", function() {
        editableFields.forEach(field => {
            const input = document.getElementById(`${field}Input`);
            input.readOnly = false;
        });
        editButton.style.display = "none";
        saveButton.style.display = "block";
    });

    // отправка формы с помощью Fetch API
    profileForm.addEventListener("submit", function(e) {
        e.preventDefault();

        const formData = new FormData(profileForm);

        fetch(profileForm.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken"),  // CSRF-токен
                "X-Requested-With": "XMLHttpRequest"  // Для Django is_ajax() (если нужно)
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // блок полей после успешного сохранения
                editableFields.forEach(field => {
                    document.getElementById(`${field}Input`).readOnly = true;
                });
                editButton.style.display = "block";
                saveButton.style.display = "none";
                alert("Данные сохранены!");
            } else {
                alert("Ошибка: " + (data.error || "Неизвестная ошибка"));
            }
        })
        .catch(error => {
            alert("Ошибка сети: " + error);
        });
    });
});