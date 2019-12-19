import os
from jinja2 import Template

os.mkdir("dist")

with open("current_page") as fp:
	page = fp.read()

with open("template.html") as fp:
	template = Template(fp.read())

with open("dist/index.html", "w") as fp:
	fp.write(template.render(page=page))

