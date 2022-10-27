import os
# import from Flask starting with uppercase "F" indicates its a class
from flask import Flask, render_template

'''
The first argument of the Flask class is the name of the
application's module(__name__) = our pakage, since we're just using
a single module, we can use __name__ which is a built_in python variable.
'''

# storing an instance of Flask after import in a
# variable called "app"(by convention)
app = Flask(__name__)


# Flask needs us so that it knows where to look for templates and static files.
# Therefore we use the app.route decorator.
# decorator: load function from the root directory and return code block.
@app.route("/")
def index():
    '''
    here, we render an html text directly inside our function.
    But this will make things complicated. Hence we import from flask
    the "render_template" and link it to our html file.
    '''
    # return "<h1>Hello</h1>, <h2>World</h2>"
    # flask expects to find this file in templates folder created
    return render_template("index.html")


# Attach additional html page from root
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


'''
Next we import os, an additional functionality to keep our python running
'''
if __name__ == "__main__":  # main is the name of the default module in python
    app.run(
        # using the os module to get the IP address and
        # set at default 0 if no IP is found.
        host=os.environ.get("IP", "0.0.0.0"),
        # 5000, common port used by python, an integer
        port=int(os.environ.get("PORT", "5000")),
        # True helps us to debug our code much easier
        # during testing or development stage.
        debug=True
        # debug is set to True & must be removed before submitting for
        # assessment or for production deployment to avoid security breach.
        )
