from mrjob.job import MRJob

class MRRatingCounter(MRJob):
    def mapper(self, key, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer(self, movieID, occurences):
        yield movieID, sum(occurences)

if __name__ == '__main__':
    MRRatingCounter.run()
