$(document).ready(function () {
    const ENTER_KEY_CODE = 13
    const fields = ['model', 'brand', 'car_year']
    for (const field of fields) {
        $(`#id_${field}`).on('keypress', function (event) {
            if (event.which === ENTER_KEY_CODE) {
                $("#filter-form").submit()
            }
        })
    }
})