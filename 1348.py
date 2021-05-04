class TweetCounts:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.dic[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            f = 60
        elif freq == 'hour':
            f = 3600
        else:
            f = 86400
        res = [0] * math.ceil((endTime - startTime + 1) / f)
        ls = self.dic[tweetName]
        for k in ls:
            if startTime <= k <= endTime:
                res[(k - startTime) // f] += 1
        return res

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)