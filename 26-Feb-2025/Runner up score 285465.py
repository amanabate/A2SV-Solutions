# Problem: Runner up score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
    scores = list(arr)  

    max_score = max(scores)

    runner_up_scores = [score for score in scores if score != max_score]

    print(max(runner_up_scores))
