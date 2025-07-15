from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Addition App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to right, #6dd5ed, #2193b0);
            font-family: 'Segoe UI', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.25);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            max-width: 500px;
            width: 100%;
            color: #fff;
        }
        h2 {
            text-align: center;
            margin-bottom: 25px;
        }
        label {
            color: #f8f9fa;
        }
        .btn-custom {
            background-color: #0d6efd;
            color: #fff;
            transition: all 0.3s ease;
        }
        .btn-custom:hover {
            background-color: #0b5ed7;
            transform: scale(1.03);
        }
        .result {
            margin-top: 20px;
            font-size: 1.25rem;
            text-align: center;
            color: #e2f0ff;
        }
        .spinner {
            display: none;
            margin-top: 10px;
            text-align: center;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="glass-card">
        <h2>Addition Calculator</h2>
        <form id="addForm">
            <div class="mb-3">
                <label for="num1" class="form-label">Number 1</label>
                <input type="number" class="form-control" id="num1" required>
            </div>
            <div class="mb-3">
                <label for="num2" class="form-label">Number 2</label>
                <input type="number" class="form-control" id="num2" required>
            </div>
            <button type="submit" class="btn btn-custom w-100">Add</button>
            <div class="spinner" id="spinner">Calculating...</div>
        </form>
        <div class="result" id="resultText"></div>
    </div>

    <script>
        document.getElementById("addForm").addEventListener("submit", async function(e) {
            e.preventDefault();
            const num1 = document.getElementById("num1").value;
            const num2 = document.getElementById("num2").value;
            const spinner = document.getElementById("spinner");
            const resultBox = document.getElementById("resultText");

            resultBox.innerText = "";
            spinner.style.display = "block";

            try {
                const res = await fetch(`/addition?num1=${num1}&num2=${num2}`);
                const result = await res.json();
                resultBox.innerText = result;
            } catch (err) {
                resultBox.innerText = "Something went wrong.";
            } finally {
                spinner.style.display = "none";
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def greet():
    return render_template_string(HTML_TEMPLATE)

@app.route('/addition')
def addition():
    a = request.args.get('num1', type=int)
    b = request.args.get('num2', type=int)
    return jsonify(f"The addition of {a} and {b} is: {a + b}")

if __name__ == '__main__':
    app.run(debug=True)
