HTTPRequest.get("http://10.0.0.2:5000/start?token=" + token,
     new HttpRequestCallback() {
       @Override
       public void onSuccess(String response) {
           // ...
       }
   });
