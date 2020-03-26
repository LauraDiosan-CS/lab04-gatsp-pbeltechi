
class Ui:
    def __init__(self, service):
        self.__service = service

    def run(self):
        try:
            # sn = int(input("Source node = "))
            # popsize = int(input("Population size ="))
            # nogen = int(input("Generations number = "))
            # chromo = self.__service.solveTsp(sn,popsize,nogen)
            chromo = self.__service.solveTsp(0,500,500)
            print("Best chromo of all: ")
            print(chromo)
        except ValueError as e:
            print(e)

