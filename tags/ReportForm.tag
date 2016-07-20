<ReportForm>
  <div class="row">
    <div class="col s10 offset-s1">
      <div class="card">
        <div class="card-content">
          <form onSubmit={ submitreport } method="POST">
            <div class="row">
              <div class="input-field col s12">
                <input name="username" type="text" value=""/>
                <label for="username">Username</label>
              </div>
            </div>
            <div class="row">
              <div class="input-field col s12">
                <textarea cols="30" id="body" name="body" rows="10" class="materialize-textarea"></textarea>
                <label for="body">body</label>
              </div>
            </div>
            <div class="row">
              <div class="input-field col s2 offset-s10">
                <button class="btn" disabled={ sending  }>Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <script>
   var today = new Date();
   this.year = today.getFullYear();
   var month = today.getMonth()+1;
   if (month<10){
     this.month = '0' + month.toString();
   }else{
     this.month = month.toString();
   }
   this.week = '0' + Math.floor((today.getDate() - today.getDay() + 12) / 7).toString();
   this.update();

   var self = this
   submitreport(e) {
     var request = window.superagent;
     var username = e.target[0].value;
     var body = e.target[1].value;
     var sending = true;
     request
     .post("http://localhost:8080/api/report/"+self.year+"/"+self.month+"/"+self.week)
     .type('form')
     .send({username: username, body: body})
     .end(function(err, res){
       if (res.body['status']){
         location.href = 'index.html';
       }
       sending = false;
     });
   }
  </script>
</ReportForm>
