class Team:
    def __init__(self, teammembers):
        self._team = teammembers

    def add_team_memeber(self, memeber):
        self._team.append(memeber)

    def remove_team_memeber(self, memeber):
        if memeber in self._team:
            self._team.remove(memeber)

    def __iter__(self):
        return TeamIterator(self)


class TeamIterator:
    def __init__(self, teamObj):
        self.index = 0
        self.data = teamObj._team

    def __next__(self):
        if (self.index >= len(self.data)):
            raise StopIteration("no more items to iterate over")

        else:
            val = self.data[self.index]
            self.index += 1
            return val


team = Team(["Ram", "Shyam"])
team.add_team_memeber("Mohan")
team.add_team_memeber("Anton")
team.remove_team_memeber("Ram")

## because of __iter__() our Team class is iterable
for members in team:
    print(members)

print(team._team)

iterator = iter(team)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

print("="*75)

class AlternateIterable:
    def __init__(self,data):
        self.data = data

    def __getitem__(self, idx):
        return self.data[idx]


for i in AlternateIterable([1,2,3,5,6]):
    print(i)






