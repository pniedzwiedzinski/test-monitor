import os
import subprocess
from jinja2 import Template

os.mkdir("dist")
# Hash of HEAD commit
head = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1]

## Generate site
with open("current_page") as fp:
	page = fp.read()

with open("scripts/template.html") as fp:
	template = Template(fp.read())

with open("dist/index.html", "w") as fp:
	fp.write(template.render(page=page, head=head))


## Generate `head` file
with open("dist/head", "w") as fp:
	fp.write(head)