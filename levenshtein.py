def LevenshteinDistance(str1,str2):
    '''
    distance[i][j] : str1のi番目までの文字列とstr2のj番目までの文字列の編集距離
    '''
    distance = [[0] * (len(str2)+1)] * (len(str1)+1)
    for i in range(len(str1)+1):
        distance[i][0] = i
    for j in range(len(str2)+1):
        distance[0][j] = j

    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            d_1 = distance[i-1][j-1] if str1[i-1]==str2[j-1] else distance[i-1][j-1]+1
            d_2 = distance[i][j-1]+1
            d_3 = distance[i-1][j]+1
            distance[i][j]=min([d_1, d_2, d_3])

    return distance[i][j]

if __name__ == '__main__':
    str1 = 'coffee'
    str2 = 'cafe'
    print(LevenshteinDistance(str1,str2))
