

#Parsing example:
## Requiest :
        curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "Name Family"}' http://localhost:5000/foo

## Response:
         HTTP/1.0 200 OK
        Content-Type: application/json
        Content-Length: 50
        Server: Werkzeug/0.16.0 Python/3.7.5
        Date: Sat, 28 Dec 2019 11:26:33 GMT
        
        {
          "userId": "1", 
          "username": "Name Family"
        }

## Debug:
        127.0.0.1 - - [28/Dec/2019 13:26:33] "POST /foo HTTP/1.1" 200 -

## Other :
        For URL query parameters, use request.args.
        
        search = request.args.get("search")
        page = request.args.get("page")
        
        For posted form input, use request.form.
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        For JSON posted with content type application/json, use request.get_json().
        
        data = request.get_json()

## Info
        #@app.route('/', methods=['GET', 'POST'])
        #def index():
        #    print(request.form)
        #    return
        """
        <form method="post">
            <input type="text">
            <input type="text" id="txt2">
            <input type="text" name="txt3" id="txt3">  
            <input type="submit">
        </form>
        """
        
        @app.route('/foo', methods=['GET','POST'])
        def foo():
            data = request.json    #{"userId":"1", "username": "User Name"}
        #
        #        request.args
        #        or request.form
        #        or request.get_json(force=True, silent=True)
        #        or request.data
        #
        #    data = request.get_json()
        #    data = request.get_data()    # out data as str(data)
            return jsonify(data)
