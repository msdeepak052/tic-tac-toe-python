from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize the game board
board = [" "] * 9
current_player = "X"

# Function to check for a winner
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
            return board[condition[0]]
    return None

# API to reset the game
@app.route("/reset", methods=["POST"])
def reset_game():
    global board, current_player
    board = [" "] * 9
    current_player = "X"
    return jsonify({"message": "Game reset!", "board": board, "current_player": current_player})

# API to make a move
@app.route("/move", methods=["POST"])
def make_move():
    global current_player
    data = request.json
    index = data.get("index")

    if board[index] == " ":
        board[index] = current_player
        winner = check_winner()

        if winner:
            return jsonify({"winner": winner, "board": board})

        if " " not in board:
            return jsonify({"winner": "Tie", "board": board})

        # Switch player
        current_player = "O" if current_player == "X" else "X"
        return jsonify({"board": board, "current_player": current_player})

    return jsonify({"error": "Invalid move!"})

# Serve the game UI
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
