from flask import Flask
from flask import request
import requests
import os
import json
app = Flask(__name__)

def get_api_key() -> str:
    secret = os.environ.get("COMPUTE_API_KEY")
    if secret:
        return secret
    else:
        #local testing
        return "ya29.a0AfB_byD3pUTsIhZG0trte5ENCQcPPJBMntmTNyFGElCkiNWI14m4TIQqgmveqi5WMhrVZXo3UwHjsf-pB5vWrquJycmm1D-E3NGr_pFmmAepfLvQlUlv3TBPe3Dc-J5JkKlz0VRh_D7KJXvGTo6YwCwLBTiGggihjICdtnS3LVGiK03eNNwWag7ZD9Eq1dKtfLMnXelStbGcBzC29st-5S78NdeSMj5ZCgiuP4_Y_tHJSv7qTxA6s4pvGYZjzOV2Nv3U9hNXyVzBm7HOp3NCAFCh_TyFWtByr_AaYPYGpT8ymnEPnFR-10T9LtHCX8sC9qEUR0cm4fU3fjc-LLSwCE5lJ066LLpqaSN95F8D0RY1J4aQM2FrNq59kGp760NIv_eNRJHuLtHnaqYntkUJPV0vqfeV5qG3BwaCgYKAfYSARMSFQHGX2MiW-Wgr15eo-pqwAGra-PoZg0425"     
@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/test")
def test():
    #return "Test" # testing 
    return(get_api_key())

@app.route("/add",methods=['GET','POST'])
def add():
  if request.method=='GET':
    return "Use post to add" # replace with form template
  else:
    token=get_api_key()
    ret = addWorker(token,request.form['num'])
    return ret


def addWorker(token, num):
    with open('payload.json') as p:
      tdata=json.load(p)
    tdata['name']='sparkplug-master-'+str(num)
    data=json.dumps(tdata)
    url='https://www.googleapis.com/compute/v1/projects/lab5-407311/zones/europe-west1-b/instances'
    headers={"Authorization": "Bearer "+token}
    resp=requests.post(url,headers=headers, data=data)
    if resp.status_code==200:     
      return "Done"
    else:
      print(resp.content)
      return "Error\n"+resp.content.decode('utf-8') + '\n\n\n'+data



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
