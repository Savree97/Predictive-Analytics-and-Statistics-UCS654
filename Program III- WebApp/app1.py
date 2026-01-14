from flask import Flask, render_template, request, send_file
import os
from topsis_savree_102317097.topsis import topsis

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]

        # Save uploaded file
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(input_path)

        # Output file path
        output_path = os.path.join(app.config["UPLOAD_FOLDER"], "result.csv")

        try:
            # Call TOPSIS function
            topsis(input_path, weights, impacts, output_path)
        except Exception as e:
            return f"Error: {e}"

        # Send result file to user
        return send_file(output_path, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
