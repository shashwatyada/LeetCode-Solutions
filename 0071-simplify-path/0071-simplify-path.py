class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        # Split path by slashes
        tokens = path.split("/")

        for token in tokens:
            if token == "" or token == ".":
                # Ingore empty tokens from consecutive slashes and current directory markers
                continue
            elif token == "..":
                # Go up one directory level if stack is not empty
                if stack:
                    stack.pop()
            else:
                # Add valid directory or file name
                stack.append(token)
                
        # Join components with '/' preceded by root '/'
        return '/' + "/".join(stack)