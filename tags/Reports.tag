<Reports>
  <virtual each={ item in list }>
    <Report key={ item.key }></Report>
  </virtual>

  <script>
   var request = window.superagent;
   var self = this
   request
   .get('http://localhost:8080/api/report/list')
   .end(function(err, res){
     self.list=res.body.list
     self.update()
   });
  </script>
</Reports>
