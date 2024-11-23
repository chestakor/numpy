from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/result', methods=['GET'])
def square_number():
    try:
        # Get the value from the URL parameter
        num = int(request.args.get('num'))
        result = num ** 2
        
        response = {
            "status": "success",
            "result": f"{num} square is {result}",
            "Dev": "Aftab"
        }
        return jsonify(response)
    
    except (ValueError, TypeError):
        return jsonify({
            "status": "error",
            "message": "Invalid input. Please provide a valid number."
        })

if __name__ == '__main__':
    app.run(debug=True)
