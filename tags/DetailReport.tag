<DetailReport>
  <div class="row">
    <div class="col s10 offset-s1">
      <div class="card">
        <div class="card-content">
          <span class="card-title">Report::{hash}</span>
        </div>
      </div>
      <div class="card" each={ item in list }>
        <div class="card-content">
          <span class="card-title">{ item.username }</span>
          <p class="flow-text" each={ reportbody in item.body }>
            { reportbody }
          </p>
        </div>
      </div>
    </div>
  </div>

  <script>
   this.hash = location.hash.split('#')[1]
   var request = window.superagent;
   var self = this
   request
   .get('http://localhost:8080/api/report/'+this.hash)
   .end(function(err, res){
     self.list = res.body.reports
     self.update();
   });
  </script>
</DetailReport>
