from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method=="GET":
        return render_template("index.html")
    else:
        id = request.form.get('fname')
        print(id)
        data = requests.get(f"https://stacks-node-api.mainnet.stacks.co/extended/v1/search/{id}").json()
        print(data)
        if data["found"]==False:
            status = "danger"
            return render_template("index.html", txt1="", txt2=data["error"], status = status) 
      
    res = f'''
      Burn Block Time: {data["result"]["block_data"]['burn_block_time']}<br>
      Canonical: {data["result"]["block_data"]['canonical']}<br>
      Hash: {data["result"]["block_data"]['hash']}<br>
      Height: {data["result"]["block_data"]['height']}<br>
      Parent Block Hash: {data["result"]["block_data"]['parent_block_hash']}<br>
      Entity ID: {data["result"]['entity_id']}<br>
      Entity Type: {data["result"]['entity_type']}<br>
    '''
    return render_template("index.html", txt1="", txt2=res, status = "success") 

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, use_reloader=False)