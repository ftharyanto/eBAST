document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    var options = {
        'autoClose': true
    }
    M.Datepicker.init(elems, options);
  });