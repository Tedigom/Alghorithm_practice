# https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

def solution(genres, plays):
    genresAndPlays = list(zip(plays,genres))
    dictionary = {}
    topCategory = []
    bestSongList=[]
    answer = []

    #장르별  플레이 횟수 추출
    for i in range(len(genres)):
        if genres[i] in dictionary:
            dictionary[genres[i]] += plays[i]
        else:
            dictionary[genres[i]] = plays[i]

    # 장르 ranking 정렬
    for item in dictionary:
        topCategory.append(item)
    topCategory = sorted(topCategory, key = lambda x : dictionary[x], reverse = True)
'''
dictionary 의 item의 value 값에 의해서 정렬하기 위해 key = lambda x : ditcionary[x]로 처리
'''
    #장르 내 랭킹 1,2 선정후 answer에 append
    sortedGP = sorted(genresAndPlays,reverse = True)
    '''
    genresAndPlays를 재생횟수로 정렬하기위해(장르 상관 없이) sortedGP 생성
    '''
    for i in range(len(topCategory)):
        cnt=0
        for j in range(len(sortedGP)):
            if sortedGP[j][1] == topCategory[i] and cnt<2:
                bestSongList.append(sortedGP[j])
                cnt += 1

    print(bestSongList)
    for i in range(len(bestSongList)):
        index = genresAndPlays.index(bestSongList[i])
        genresAndPlays[index] = 0
        print(bestSongList)
        answer.append(index)


    return answer

    '''
    What I learned
    일단 한번 더 풀어봐야겠다.
    '''
