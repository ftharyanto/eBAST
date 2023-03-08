document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.input_date');
  var options = {
    autoClose: true,
  };
  M.Datepicker.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.collapsible');
  M.Collapsible.init(elems);
});
