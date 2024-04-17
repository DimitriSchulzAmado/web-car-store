$(document).ready(function () {
    setTimeout(() => {
        const queryParams = new URLSearchParams(window.location.search);
        const situation = queryParams.get("situation");
        const situationField = $("#id_situation")

        if (situation) {
            $(`input[name="situation_aux"][id="${situation}"]`).prop('checked', true);
            situationField.val(situation)
        }

        if (situationField.attr("disabled")) {
            $('input[name="situation_aux"]').prop('disabled', true)
        }
    }, 100);
});
