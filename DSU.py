class DSU:
    def __init__(self, set_a):
        self.parent = set_a

    def find(self, num):
        if num == self.parent[num]:
            return num
        else:
            self.parent[num] = self.find(self.parent[num])
            return self.parent[num]

    def union(self, ver1, ver2):
        root_ver1 = self.find(ver1)
        root_ver2 = self.find(ver2)

        if root_ver1 == root_ver2:
            return False
        else:
            self.parent[root_ver1] = root_ver2
            return True

