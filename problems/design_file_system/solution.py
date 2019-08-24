from collections import defaultdict
class FileSystem:

    def __init__(self):
        T = lambda: defaultdict(T)
        self.fs = T()
    
    def _parse(self, path):
        return path[1:].split('/')
    
    def _get_node(self, dirs):
        node = self.fs
        for d in dirs:
            if d not in node: return None
            node = node[d]
        return node
            

    def create(self, path: str, value: int) -> bool:
        dirs = self._parse(path)
        parent = self._get_node(dirs[:-1])
        if parent is None or dirs[-1] in parent: return False
        parent[dirs[-1]]["$"] = value
        return True

    def get(self, path: str) -> int:
        dirs = self._parse(path)
        node = self._get_node(dirs)
        if node is None: return -1
        return node['$']
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)