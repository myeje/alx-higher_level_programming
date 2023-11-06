('document').ready(function () {
    $('INPUT#btn_translate').click(translate);
    $('INPUT#language_code').focus(function () {
      $(this).keydown(function (even) {
        if (even.keyCode === 13) {
          translate();
        }
      });
    });
  });
  
  function translate () {
    const lang = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(lang + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  }