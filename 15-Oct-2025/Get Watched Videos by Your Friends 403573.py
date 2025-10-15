# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        visited = set([id])
        q = deque([id])
        current_level = 0

        
        while q and current_level < level:
            for _ in range(len(q)):
                person = q.popleft()
                for f in friends[person]:
                    if f not in visited:
                        visited.add(f)
                        q.append(f)
            current_level += 1

    
        video_count = Counter()

        for person in q:
            for video in watchedVideos[person]:
                video_count[video] += 1

        
        videos = list(video_count.keys())

        
        video_freq = [(v, video_count[v]) for v in videos]

        # Sort by frequency first, then alphabetically
        video_freq.sort(key=lambda item: (item[1], item[0]))

       
        result = [v for v, _ in video_freq]

        return result
