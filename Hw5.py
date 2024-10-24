game_tree = [
    [
        [3, 5],
        [14, 8]
    ],
    [
        [-2, 5],
        [-1, 7]
    ]
]

def minimax(node, is_maximizing_player):
    if isinstance(node, int):
        return node
    if is_maximizing_player:
        best_value = float('-inf')
        for child in node:
            value = minimax(child, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node:
            value = minimax(child, True)
            best_value = min(best_value, value)
        return best_value

minimax_result = minimax(game_tree, True)
print(minimax_result)
