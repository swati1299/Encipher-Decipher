from flask import Flask,render_template,request,redirect
app=Flask(__name__)


@app.route('/',methods=["GET","POST"])
def encipher_function():
    def encode(message):
        s=[]
        for i in message:
            key=25-(ord(i)-ord('a'))+ord('a')
            s.append(chr(key))

        s=''.join(s)  
        return s
    if request.method=="POST":
        message=request.form['plaintext']
        return render_template("index.html",encoded=encode(message))
    else:
        return render_template("index.html")




@app.route('/decrypt',methods=["POST"])
def decipher_function():
    def decode(message):
        s=[]
        for i in message:
            key=25-(ord(i)-ord('a'))+ord('a')
            s.append(chr(key))
        
        s=''.join(s)
        return s
    decoded_message=request.form['decipher']
    message=decode(decoded_message)
    return render_template("index.html",message=message)

    
app.run()
