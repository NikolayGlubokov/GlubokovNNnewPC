from jinja2 import Template, Environment, FileSystemLoader



file_loader = FileSystemLoader('my_templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render()

tm2 = env.get_template('main2.html')
msg2 = tm2.render()
print('Вариан прямой вставки',msg)
print('Вариан наследования',msg2) 