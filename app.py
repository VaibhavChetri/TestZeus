from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the user input from the form
        user_input = request.form.get("user_input")
        
        # Simple processing logic (replace with your desired logic)
        result = f"You entered: {user_input}"
        
        return render_template("output.html", user_input=user_input, result=result)

    # Render the input form
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
