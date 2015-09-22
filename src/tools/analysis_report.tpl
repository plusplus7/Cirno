<html>
 <head>
  <title> log analysis report </title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
 </head>
 <body>
 <div class="container" id="editor_page">
  <div class="row">
   <div class="col-md-3 sidebar">
    <div class="widget">
     <h4 class="title"> Ops </h4>
     <div class="content community">
      <div class="list-group">
       <p><a id="p_add_post" class="list-group-item active"> View all request </a></p>
       <p><a id="p_add_area" class="list-group-item"> View ip index </a></p>
       <p><a id="p_add_area" class="list-group-item"> View httpcode index </a></p>
      </div>
     </div>
    </div>
   </div>
   <div class="col-md-9">
    <div class="list-group">
     {% for ip in ipindex.keys() %}
      <a href="#" class="list-group-item">{{ ip }}&nbsp;({{ ip_geo[ip] }})&nbsp;访问次数{{ len(ipindex[ip]) }}</a>
     {% end %}
    </div>
    <div id="m_all_request">
     <table class="table">
      <tr><td>Date</td><td>Time</td><td>Httpcode</td><td>Method</td><td>Url</td><td>IP</td><td>Latency</td></tr>
      {% for req in reqlist %}
          <tr><td>{{ req["date"] }}</td><td>{{ req["time"] }}</td><td>{{ req["code"] }}</td><td>{{ req["method"] }}</td><td>{{ req["path"] }}</td><td>{{ req["ip"] }}</td><td>{{ req["latency"] }}</td></tr>
      {% end %}
     </table>
    </div>
   </div>
  </div>
 </div>
  <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
  <script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
 </body>
</html>
