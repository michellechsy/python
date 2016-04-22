""" Basic todo list using webpy 0.3 """
import web
import model

from todoList import *

### Templates
render = web.template.render(TEMPLATES_DIR, base='base')

class Index:

    form = web.form.Form(
            web.form.Textbox('title', web.form.notnull,
                             description=ADD_TODO_ITEM_TEXT),
            web.form.Button(ADD_TODO_BUTTON),
    )

    def GET(self):
        """ Show page """
        todos = model.get_todos()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother(URL_ROOT)


class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother(URL_ROOT)


app = web.application(URLS, globals())

if __name__ == '__main__':
    app.run()
