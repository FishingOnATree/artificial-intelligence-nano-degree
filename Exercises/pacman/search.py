# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    unvisited_stack = []
    unvisited_stack.append(problem.getStartState())
    paths = dict()
    explored = set()
    while len(unvisited_stack) > 0:
        curr_state = unvisited_stack.pop()
        explored.add(curr_state)
        path = paths.get(curr_state, [])
        if problem.isGoalState(curr_state):
            return path
        else:
            successors = problem.getSuccessors(curr_state)
            if successors:
                for next_state, direction, _ in successors:
                    if next_state not in explored:
                        unvisited_stack.append(next_state)
                        new_path = list(path)
                        new_path.append(direction)
                        paths[next_state] = new_path


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    unvisited_queue = [problem.getStartState()]
    paths = dict()
    explored = set()
    while len(unvisited_queue) > 0:
        curr_state = unvisited_queue.pop(0)
        explored.add(curr_state)
        path = paths.get(curr_state, [])
        if problem.isGoalState(curr_state):
            return path
        else:
            successors = problem.getSuccessors(curr_state)
            if successors:
                for next_state, direction, _ in successors:
                    if next_state not in explored:
                        unvisited_queue.append(next_state)
                        new_path = list(path)
                        new_path.append(direction)
                        paths[next_state] = new_path




def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    unvisited_queue = PriorityQueue()
    unvisited_queue.push(problem.getStartState(), 0)
    paths = dict()
    costs = dict()
    explored = set()
    while not unvisited_queue.isEmpty():
        curr_state = unvisited_queue.pop()
        explored.add(curr_state)
        path = paths.get(curr_state, [])
        cost_from_root = costs.get(curr_state, 0)
        if problem.isGoalState(curr_state):
            return path
        else:
            successors = problem.getSuccessors(curr_state)
            if successors:
                for next_state, direction, cost in successors:
                    if next_state not in explored:
                        new_path = list(path)
                        new_path.append(direction)
                        new_cost = cost_from_root + cost
                        paths[next_state] = new_path
                        costs[next_state] = new_cost
                        unvisited_queue.push(next_state, new_cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    unvisited_queue = PriorityQueue()
    unvisited_queue.push((problem.getStartState(), [], 0), 0)
    explored = set()
    while not unvisited_queue.isEmpty():
        curr_state, path, cost_from_root = unvisited_queue.pop()
        if problem.isGoalState(curr_state):
            return path
        else:
            if curr_state not in explored:
                explored.add(curr_state)
                for next_state, direction, step_cost in problem.getSuccessors(curr_state):
                    if next_state not in explored:
                        estimated_cost = heuristic(curr_state, problem)
                        new_path = list(path)
                        new_path.append(direction)
                        new_cost = cost_from_root + step_cost + estimated_cost
                        unvisited_queue.push((next_state, new_path, new_cost), new_cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
