$(document).ready(function () {
  var index = 0;
  var len = 0;
  var clear_flag = false;
  var xmlHttp;

  function showVal (expression) {
    if (expression.length === 0) {
      $('#screen').val('');
      return;
    }
    var url = '../practice.php';
    expression = expression.replace(/\+/g, "%2B");
    expression = expression.replace(/\&/g, "%26");
    expression = expression.replace('ans', '$ans');
    var postStr = 'expression=' + expression;
    var ajax = false;
    if (window.XMLHttpRequest) {
      ajax = new XMLHttpRequest();
      if (ajax.overrideMimeType) {
        ajax.overrideMimeType('text/xml');
      }
    } else if (window.ActiveXObject) {
      try {
        ajax = new ActiveXObject('Msxml2.XMLHTTP');
      } catch (e) {
        try {
          ajax = new ActiveXObject('Microsoft.XMLHTTP');
        } catch (e) {}
      }
    }
    if (!ajax) {
      window.alert('Unable to create XMLHttpRequest Object');
      return false;
    }
    ajax.open('POST', url, false);
    ajax.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    ajax.send(postStr);
    $('#screen').val(ajax.responseText);
  }

  function clear_screen (flag) {
    index = 0;
    len = 0;
    $('#screen').val('');
    if (flag) {
      $('#screen').focus();
      document.getElementById('screen').setSelectionRange(index, index);
    }
  }

  $('button').attr('disabled', 'disabled');
  $('#on').removeAttr('disabled');

  $('#on').click(function () {
    $('button').removeAttr('disabled');
    clear_screen(true);
    return false;
  });
  $('#off').click(function () {
    $('button').attr('disabled', 'disabled');
    $('#on').removeAttr('disabled');
    clear_screen(false);
    return false;
  });
  $('.show').click(function () {
    if (clear_flag) {
      clear_screen(false);
      clear_flag = false;
    }
    var expression = $('#screen').val();
    $('#screen').val(expression.substr(0, index) + $(this).text() + expression.substr(index));
    index += $(this).text().length;
    len += $(this).text().length;
    $('#screen').focus();
    document.getElementById('screen').setSelectionRange(index, index);
    return false;
  });
  $('#lt').click(function () {
    if (clear_flag) {
      clear_screen(false);
      clear_flag = false;
    }
    if (index > 0)
      index -= 1;
    $('#screen').focus();
    document.getElementById('screen').setSelectionRange(index, index);
    return false;
  });
  $('#rt').click(function () {
    if (clear_flag) {
      clear_screen(false);
      clear_flag = false;
    }
    if (index < len)
      index += 1;
    $('#screen').focus();
    document.getElementById('screen').setSelectionRange(index, index);
    return false;
  });
  $('#del').click(function () {
    if (clear_flag) {
      clear_screen(false);
      clear_flag = false;
    }
    if (index > 0) {
      var expression = $('#screen').val();
      if (expression.substr(index-3, 3) === 'ans') {
        index -= 3;
        len -= 3;
        $('#screen').val(expression.substr(0, index) + expression.substr(index+3));
        $('#screen').focus();
        document.getElementById('screen').setSelectionRange(index, index);
      }
      else {
        index -= 1;
        len -= 1;
        $('#screen').val(expression.substr(0, index) + expression.substr(index+1));
        $('#screen').focus();
        document.getElementById('screen').setSelectionRange(index, index);
      }
    }
    return false;
  });
  $('#ac').click(function () {
    clear_screen(true);
    return false;
  }); 

  $('#eq').click(function () {
    clear_flag = true;
    showVal($('#screen').val());
  });
});