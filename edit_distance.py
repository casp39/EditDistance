def EditDistance(str1,str2):
    m = len(str1)
    n = len(str2)

    distance = [[0] * (n+1) for i in range(m+1)]
    for i in range(m+1):
        distance[i][0] = i
    for j in range(n+1):
        distance[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            d_1 = distance[i-1][j]+1
            d_2 = distance[i][j-1]+1
            d_3 = distance[i-1][j-1] if str1[i-1]==str2[j-1] else distance[i-1][j-1]+1
            distance[i][j] = min([d_1, d_2, d_3])

    return distance[m][n]

if __name__ == '__main__':
    str1 = 'ship'
    str2 = 'sheep'
    print(EditDistance(str1,str2))
