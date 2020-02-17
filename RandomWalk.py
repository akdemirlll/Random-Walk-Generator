class RandomWalk:
    def __init__(self,stations):
        self.stations=stations
        self.start_point=stations[1:-1]
        self.directions=['R','L']

    def walk(self,start=None):
        path=[]
        end=None
        if start==None:
            start=np.random.choice(self.start_point)
        if start not in self.stations:
            raise ValueError ('gecersiz baslangic noktasi')
        else:
            pass
        path.append(start)
        while end!=self.stations[0] and end!=self.stations[-1]:
            direct=np.random.choice(self.directions)
            if direct=='R':
                next_station=self.stations[self.stations.index(start)+1]
                path.append(next_station)
                start=next_station
                end=next_station
            else:
                next_station=self.stations[self.stations.index(start)-1]
                path.append(next_station)
                start=next_station
                end=next_station
        return path


if __name__ == '__main__':
    w=RandomWalk(['A','B','C','D','E','F','G'])

    w.walk()
#     ['C', 'D', 'E', 'F', 'G']

    w.walk(start='D')
# ['D', 'E', 'F', 'E', 'D', 'E', 'F', 'G']
