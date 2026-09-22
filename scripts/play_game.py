import os
import json
import re
import random
import urllib.request

# 1. Load event payload from GitHub Action
event_path = os.environ.get('GITHUB_EVENT_PATH')
if not event_path or not os.path.exists(event_path):
    print("No GITHUB_EVENT_PATH found.")
    exit(0)

with open(event_path, 'r', encoding='utf-8') as f:
    event_data = json.load(f)

issue = event_data.get('issue', {})
title = issue.get('title', '').strip()
sender = issue.get('user', {}).get('login', 'Player')
issue_number = issue.get('number')
repo = os.environ.get('GITHUB_REPOSITORY')
token = os.environ.get('GITHUB_TOKEN')

if not title.startswith('ttt|'):
    print("Not a tic-tac-toe move.")
    exit(0)

parts = title.split('|')
if len(parts) != 3:
    print("Invalid move title format.")
    exit(0)

try:
    r, c = int(parts[1]), int(parts[2])
except ValueError:
    exit(0)

# 2. Load or initialize board state
state_file = 'game_state.json'
if os.path.exists(state_file):
    with open(state_file, 'r') as f:
        board = json.load(f).get('board', [["", "", ""], ["", "", ""], ["", "", ""]])
else:
    board = [["", "", ""], ["", "", ""], ["", "", ""]]

def check_winner(b):
    lines = [
        [b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]
    ]
    for line in lines:
        if line[0] != "" and line[0] == line[1] == line[2]:
            return line[0]
    if all(b[row][col] != "" for row in range(3) for col in range(3)):
        return "DRAW"
    return None

# 3. Process Player Move (X) & AI Move (O)
msg = ""
reset_board = False

if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == "":
    board[r][c] = "X"
    winner = check_winner(board)

    if not winner:
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
        ai_move = None

        # Check win move for AI
        for er, ec in empty_cells:
            board[er][ec] = "O"
            if check_winner(board) == "O":
                ai_move = (er, ec)
                break
            board[er][ec] = ""

        # Block player win
        if not ai_move:
            for er, ec in empty_cells:
                board[er][ec] = "X"
                if check_winner(board) == "X":
                    ai_move = (er, ec)
                    board[er][ec] = ""
                    break
                board[er][ec] = ""

        # Take center or random
        if not ai_move and board[1][1] == "":
            ai_move = (1, 1)
        if not ai_move:
            ai_move = random.choice(empty_cells)

        board[ai_move[0]][ai_move[1]] = "O"
        winner = check_winner(board)

    if winner == "X":
        msg = f"🎉 **Congratulations @{sender}!** You defeated the GitHub Action AI Bot!"
        reset_board = True
    elif winner == "O":
        msg = f"🤖 **GitHub AI Bot won!** Better luck next time, @{sender}!"
        reset_board = True
    elif winner == "DRAW":
        msg = f"🤝 **It's a draw!** Well played @{sender}."
        reset_board = True
    else:
        msg = f"✅ Move accepted! @{sender} played **X** at ({r+1}, {c+1}). AI responded with **O**."
else:
    msg = f"⚠️ Illegal move by @{sender}. That spot is already taken!"

# 4. Generate Markdown Table
def generate_table(b, repository):
    html = ['<div align="center">\n<table style="border-collapse: collapse;">']
    for i in range(3):
        html.append("  <tr>")
        for j in range(3):
            cell = b[i][j]
            if cell == "X":
                display = "❌"
            elif cell == "O":
                display = "⭕"
            else:
                url = f"https://github.com/{repository}/issues/new?title=ttt%7C{i}%7C{j}&body=Click+%27Submit+new+issue%27+to+confirm+your+move!"
                display = f'<a href="{url}">⬜</a>'
            html.append(f'    <td align="center" width="60" height="60" style="font-size:28px;">{display}</td>')
        html.append("  </tr>")
    html.append("</table>\n</div>")
    return "\n".join(html)

table_md = generate_table(board, repo)

# Reset state if game over
if reset_board:
    board = [["", "", ""], ["", "", ""], ["", "", ""]]

with open(state_file, 'w', encoding='utf-8') as f:
    json.dump({'board': board}, f, indent=2)

# 5. Update README.md
readme_path = 'README.md'
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<!-- TTT GAME START -->)(.*?)(<!-- TTT GAME END -->)'
    replacement = f'\\1\n{table_md}\n\\3'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# 6. Comment and Close Issue
if token and repo and issue_number:
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "GitHubAction-TTT"
    }

    # Post comment
    comment_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    req = urllib.request.Request(comment_url, data=json.dumps({"body": msg}).encode('utf-8'), headers=headers)
    try:
        urllib.request.urlopen(req)
    except Exception as e:
        print("Error commenting:", e)

    # Close issue
    close_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
    req_close = urllib.request.Request(close_url, data=json.dumps({"state": "closed"}).encode('utf-8'), headers=headers, method="PATCH")
    try:
        urllib.request.urlopen(req_close)
    except Exception as e:
        print("Error closing issue:", e)

