<Reports>
  <virtual each={ item in list }>
    <Report key={ item.key }></Report>
  </virtual>

  <script>
   var request = window.superagent;
   var self = this
   request
   .get(config.apibaseuri + 'list')
   .end(function(err, res){
     self.list=res.body.list
     self.update()
   });
  </script>
</Reports>
