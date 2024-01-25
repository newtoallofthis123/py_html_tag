import html_tag
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    home_div = html_tag.HtmlTag("div").set_id("home")
    home_div.add_child(html_tag.HtmlTag("h1").set_body("Hello World"))

    a = html_tag.HtmlTag("a").add_attribute("href", "https://youtube.com").set_body("YouTube")

    home_div.add_child(a)

    return home_div.render()

app.run(debug=True)