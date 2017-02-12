$(function () {
    $.getJSON("/hor/703448", function (data) {
        $('#hourlyWeather').highcharts(data);
    });
});
$(function () {
    $.getJSON("/abc/703448", function (data) {
        $('#pressure').highcharts(data);
    });
});