# HTML Tag

The systematic way to write HTML in Python. Efficient and Pragmatic.

## Installation

```bash
pip install htmltag
```

## Usage

```python
from htmltag import HtmlTag

def home():
    home_div = html_tag.HtmlTag("div").set_id("home")
    home_div.add_child(html_tag.HtmlTag("h1").set_body("Hello World"))

    a = html_tag.HtmlTag("a").add_attribute("href", "https://youtube.com").set_body("YouTube")

    home_div.add_child(a)

    return home_div.render()

if __name__ == "__main__":
    print(home())
```

Output:

```html
<div id="home">
    <h1>Hello World</h1>
    <a href="https://youtube.com">YouTube</a>
</div>
```
