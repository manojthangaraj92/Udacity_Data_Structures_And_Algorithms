# Course: Data Structures and Algorithms
# Problems Vs. Algoritms
# Problem 7: HTTPRouter using a Trie

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    # Initialize the node with children as before, plus a handler
    def __init__(self):
        self.children = {}
        self.handler = None
        self.is_leaf = False

    # Insert the node as before
    def insert(self, path):
        self.children[path] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.root.handler = handler

    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
    def insert(self, path, handler):
        current_node = self.root
        for sub_path in path:
            if sub_path not in current_node.children:
                current_node.insert(sub_path)
            current_node = current_node.children[sub_path]

        current_node.handler = handler
        current_node.is_leaf = True

    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    def find(self, path):
        current_node = self.root
        for sub_path in path:
            if sub_path not in current_node.children:
                return None
            current_node = current_node.children[sub_path]

        if current_node.is_leaf:
            return current_node.handler
        return None

# The Router class will wrap the Trie and handle
class Router:
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
    def __init__(self, handler):
        self.router = RouteTrie(handler)

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
    def add_handler(self, str_path, handler):
        path = self.split_path(str_path)
        self.router.insert(path,handler)

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
    def lookup(self, str_path):
        path = self.split_path(str_path)
        if path is None:
            handler = self.router.root.handler
            return handler
        handler = self.router.find(path)
        if handler is not None:
            return handler
        handler = 'Page Not Found'
        return handler

    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
    def split_path(self, str_path):
        if str_path.startswith('/'):
            str_path = str_path[1:]
        if str_path.endswith('/'):
            str_path = str_path[:-1]
        if len(str_path) == 0:
            return None
        return str_path.split('/')



if __name__ == "__main__":
    # Here are some test cases and expected outputs you can use to test your implementation

     # create the router and add a route
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup(
        "/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one