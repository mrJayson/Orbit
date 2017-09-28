dateTimePickerOptions = {
    debug: true, // Debug keeps the calendar always open in the UI
    format: 'YYYY-MM-DD HH:mm:ss',
    inline: true,
    keepOpen: true,
    keyBinds: {
    	enter: function(widget) {
    		// Prevent the calendar from hiding when user hits the enter key
    		return;
    	}
    },
    toolbarPlacement: 'top',
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

// Prevent any enter key interactions from other input fields with the calendar
$('.form-control').keypress(function(event){
    if (event.keyCode === 10 || event.keyCode === 13) 
        event.preventDefault();
});