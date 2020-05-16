class StringEditDistance(object):
    def __init__(self, s1, s2):
        self.s1, self.s2 = s1, s2
        self.m, self.n = len(self.s1), len(self.s2)
        self.d = [[0] * (self.n+1) for i in range(self.m+1)]

    def __pairwise_alignment(self):
        for i in range(self.m+1):
            self.d[i][0] = i
        for j in range(self.n+1):
            self.d[0][j] = j

        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                d_1 = self.d[i-1][j] + 1
                d_2 = self.d[i][j-1] + 1
                d_3 = self.d[i-1][j-1] if str1[i-1] == str2[j-1] else self.d[i-1][j-1] + 1
                self.d[i][j] = min([d_1, d_2, d_3])

    def edit_distance(self):
        self.__pairwise_alignment()
        return self.d[self.m][self.n]

    def traceback(self):
        self.__pairwise_alignment()
        i, j = self.m, self.n
        s1, s2 = '', ''
        while i != 0 or j != 0:
            if i == 0 or self.d[i][j] == self.d[i][j-1] + 1:
                s1 += '-'
                s2 += self.s2[j-1]
                j -= 1
            elif j == 0 or self.d[i][j] == self.d[i-1][j] + 1:
                s1 += self.s1[i-1]
                s2 += '-'
                i -= 1
            else:
                s1 += self.s1[i-1]
                s2 += self.s2[j-1]
                i -= 1
                j -= 1
        return s1[::-1], s2[::-1]


if __name__ == '__main__':
    str1 = 'cafe'
    str2 = 'coffe'
    edit_distance = StringEditDistance(str1, str2)
    print(edit_distance.edit_distance())
    print(edit_distance.traceback())
