<DetailReport>
  <div class="row">
    <div class="col s10 offset-s1">
      <div class="card">
        <div class="card-content">
          <span class="card-title">Report::{hash}</span>
          <virtual each={ item in list }>
            <h6>{ item.username }</h6>
            <p class="flow-text">
              { item.body }
            </p>
          </virtual>
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
