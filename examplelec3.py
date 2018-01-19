from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/oranges')
def lemons(action='/result'):
    title_var = "My Ice Cream Form"
    # Add code -- what type should options hold?
    options = ['Chocolate', 'Vanilla', 'Superman', 'Pistachio', 'Butter Pecan', 'Many More :)']
    return render_template('seeform.html',title=title_var, lst_stuff=options)

@app.route('/apples',methods=['GET','POST'])
def plants():
    ## Add code here
    if request.method == 'GET':
        name = str(request.args['name'])
        name_len = len(str(request.args['name']))
        flavor_options = []
        options = dict(request.args)
        i = 0
        for item in options:
            if i != 0:
                flavor_options.append(item)
            i += 1
        return render_template('results.html',flavors=flavor_options, name_len=name_len, name=name)


if __name__ == "__main__":
    app.run(use_reloader=True,debug=True)
