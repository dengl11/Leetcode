class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def explore(i):
            if i in visited: return
            visited.add(i)
            for j in rooms[i]:
                explore(j)
        explore(0)
        return len(visited) == len(rooms)
        