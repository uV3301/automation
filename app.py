from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import json
# from run import get_stock_main
# from run import get_list_2
app = Flask(__name__)


@app.route("/")
@cross_origin()
def hello_world():
    return "hello there"


@app.route("/api/stock/list", methods=['POST'])
@cross_origin()
def get_stock_list():
    input_json = request.get_json()
    user_name = input_json.get("user_name")
    pass_code = input_json.get('pass_code')
    screener_link = input_json.get('screener_link')
    print(input_json)

    if user_name and pass_code and screener_link:
        print("getting stock list")
        # result = get_stock_main(username=user_name, password=pass_code, screener_link)
        # result2 = get_list_2()
        result = ["success", 'as']
        output_dict = {
            'data': result
        }
        status = 200
    else:
        print(f"Error: Input JSON is incorrect")
        output_dict = "Wrong input format"
        status = 400

    return Response(json.dumps(output_dict), status, mimetype="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001", debug=True)
