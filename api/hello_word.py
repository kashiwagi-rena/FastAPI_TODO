# from jinja2 import Environment, FileSystemLoader
# import json

# env = Environment(loader=FileSystemLoader("./", encoding='utf8'))
# tmpl = env.get_template('hello_word.j2')

# with open('hello_word.json') as hello:
#     params = json.load(hello)

# hello_word_html = tmpl.render(params)
# with open('hello_word.html', 'w') as f:
#     f.write(hello_word_html)