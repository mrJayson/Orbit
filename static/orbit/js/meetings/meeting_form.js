
dateTimePickerOptions = {
    debug: true, // debug keeps the calendar always open in the UI
    inline: true,
    useCurrent: false,
}

// Hook in bootstrap-datetimepicker
$('#startDateTimePicker').datetimepicker(dateTimePickerOptions);
$('#endDateTimePicker').datetimepicker(dateTimePickerOptions);

// Enforce min and max datetimes
$("#startDateTimePicker").on("dp.change", function (e) {
    $('#endDateTimePicker').data("DateTimePicker").minDate(e.date);
});
$("#endDateTimePicker").on("dp.change", function (e) {
    $('#startDateTimePicker').data("DateTimePicker").maxDate(e.date);
});
