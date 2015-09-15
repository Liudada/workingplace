var xmlHTTP;

function showHint (str) {
  if (str.length === 0) {
    document.getElementById('txtHint').innerHTML = '';
    return;
  }
  xmlHTTP = GetXmlHttpObject();
  if (xmlHTTP === null) {
    alert('Browser does not support HTTP Request');
    return;
  }
  var url = 'practice.php';
  str = str.replace(/\+/g, '%2B');
  str = str.replace(/\&/g, '%26');
  url = url + '?q=' + str;
  url = url + '&sid=' + Math.random();
  xmlHTTP.onreadystatechange = stateChanged;
  xmlHTTP.open('GET', url, true);
  xmlHTTP.send(null);
}

function stateChanged () {
  if (xmlHTTP.readyState === 4 || xmlHTTP.readyState === 'complete') {
    document.getElementById('txtHint').innerHTML = xmlHTTP.responseText;
  }
}

function GetXmlHttpObject () {
  var xmlHTTP = null;
  try {
    xmlHTTP = new XMLHttpRequest();
  } catch (e) {
    try {
      xmlHTTP = new ActiveXObject('Msxml2.XMLHTTP');
    } catch (e) {
      xmlHTTP = new ActiveXObject('Microsoft.XMLHTTP');
    }
  }
  return xmlHTTP;
}