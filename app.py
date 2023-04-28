from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numbers = request.form["numbers"]
        numbers_list = list(map(int, numbers.split(',')))
        return render_template("index.html", numbers_list=numbers_list)

    return render_template("index.html")
'''
<!doctype html>
<html>
  <head>
    <title>Python 工具展示</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        text-align: center;
      }
      input[type="text"] {
        width: 50%;
        padding: 12px 20px;
        margin: 8px 0;
        box-sizing: border-box;
      }
      input[type="submit"] {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <h1>请输入一串数字（用逗号隔开）：</h1>
    <form method="post">
      <input type="text" name="numbers" placeholder="1,2,3,4,5">
      <input type="submit" value="提交">
    </form>
  </body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)
