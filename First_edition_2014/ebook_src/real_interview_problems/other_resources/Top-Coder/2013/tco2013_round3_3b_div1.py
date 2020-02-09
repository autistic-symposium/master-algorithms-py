#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

   
                                
def findToneDiff(tones):
    tonesDiff = []
    n = len(tones)    
    for i, tone in enumerate(tones):
        for j in range(i+1, len(tones)):  
            sum_here = abs(tone - tones[j])
            tonesDiff.append([sum_here, i, j])            
    return sorted(tonesDiff)  
     
def findAllPossible(duration, tones, T):
    tonesDiff = findToneDiff(tones)
    sumsTone1 = [(song, i) for i, song in enumerate(duration) if song <= T]
    sumsTone2 = []
    for song in tonesDiff:
        sum_here = song[0] + duration[song[1]] + duration[song[2]]
        if sum_here <= T:
            sumsTone2.append((sum_here, song[1], song[2], 2))
    return sumsTone1, sumsTone2          
            
   
def findAllPossibleNext(sumsTone, T, n_music):
    sumsTone2 = []
    for i, song1 in enumerate(sumsTone):
        index1 = song1[1]
        for j in range(i+1, len(sumsTone)):
            song2 = sumsTone[j]
            index2 = song2[1]
            if index1 == index2:
                sum_here = song1[0] + song2[0]
                if sum_here < T:
                    sumsTone2.append((sum_here, song2[1], song2[2], n_music))
        
                    
    return sumsTone2
            
            
def maxSongs(duration, tones, T):

    if min(duration) >= T:
            return 0
               
    sumsTone1, sumsTone = findAllPossible(duration, tones, T)
    if not sumsTone:
        return 1
    
    while sumsTone:
        n_music = sumsTone[0][3]+1
        sumsTone = findAllPossibleNext(sumsTone, T, n_music)    
        if not sumsTone:
            return n_music 


   
def tests_250():
    print(maxSongs([3, 5, 4, 11], [2, 1, 3, 1], 17)) #3
    print(maxSongs([9, 11, 13, 17], [2, 1, 3, 4], 20)) #1
    print(maxSongs([100, 200, 300], [1,2,3], 99)) #0
    print(maxSongs([87,21,20,73,97,57,12,80,86,97,98,85,41,12,89,15,41,17,68,37,21,1,9,65,4,67,38,91,46,82,7,98,21,70,99,41,21,65,11,1,8,12,77,62,52,69,56,33,98,97], [88,27,89,2,96,32,4,93,89,50,58,70,15,48,31,2,27,20,31,3,23,86,69,12,59,61,85,67,77,34,29,3,75,42,50,37,56,45,51,68,89,17,4,47,9,14,29,59,43,3], 212))


                   
if __name__ == '__main__':
    tests_250()

