"""
This function(s) should handle the search algorithm
"""

def iterative_deep_search(board_dict):

    #PSUEDOCODE
    """
    depth = 1

    move_stack = stack

    FOR every white piece in the board dictionary:
        
            generate a (board state?, move?) for each possible move (up, down, left, right, explode)
            remember that stacks can move upto n tiles in a direction

            add those moves to the top of the stack

    
            

    WHILE there are still black pieces on the board (win condition):

        take a move off the top of the stack

# doesn't make sense to end up in the same place as before. comparing dicts is expensive though :(

def dfs(visited, , node):
    if node not in visited:
        print node,
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
"""

def iterativeDeepeningRECURSE(startBoard):
    visited = []   
    # parent map is a dictionary which lets us retrace the path we've taken
    parentMap = {}

    goalFound = False
    nextDepth = 1;
    while not goalFound:
        for i in range(nextDepth):
            goalFound = depthFirstSearchRECURSE(startBoard, visited, parentMap, i, 1)
        nextDepth++
        


def depthFirstSearchRECURSE(currentState, visited, parentMap, maxDepth, currentDepth):
    if (isGoal(currentState)):
        return victory #maybe returning itself to be looked for in the parent map later
    
    if currentState not in visited:
        visited.append(currentState)

        if currentDepth < maxDepth:
            children = getSuccessors(currentState)
            
            for child in children:
                parentMap[child] = currentState

                depthFirstSearch(child, visited, maxDepth, currentDepth + 1)
    return False

        

def depthFirstSearchLOOP(startBoard, maxDepth):
    
    stack = Stack()
    visited = []
    stack.push(startBoard)

    # parent map is a dictionary which lets us retrace the path we've taken
    parentMap = {} 

    # just in case initial board is victory
    if (isGoal(startBoard)):
        return victory

    while stack:
        parent = stack.pop()
        if parent in visited: continue

        if (isGoal(parent)):
            return victory

        vistited.append(parent)
        
        # getSuccessors should only return children from apporopriate depths.
        children = getSuccessors(parent, maxDepth)
        for child in children:
            stack.push(child)
            parentMap[child] = parent
    


Later on, when you found your target, you can get the path from the source to the target (pseudo code):

curr = target
while (curr != None):
  print curr
  curr = parentMap[curr]
Note that the order will be reversed, it can be solved by pushing all elements to a stack and then print.


        

        
            
        
