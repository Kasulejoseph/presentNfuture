class FOOTBALL():
    def __init__(self):
        self.test_number = 1
        self.N = 1
        self.P = 1

    def trainingHours(self, N, P, filename):
        with open(filename) as f:
            for line_no, line in enumerate(f):
                # Remember not to count the newline character
                # print (line + '<<<<<<<<<<')
                if line_no %2 ==0:
                    # continue
                    print(line_no, line)
                    self.N = line.strip()[0]
                    self.P = line.strip()[1:]
                    FOOTBALL().checkNeP(self.N, self.P)
                    # print(self.N + ' ==> ' + self.P)
                    # return True

    def footballChallenge(self, filename, S):
        f = open(filename, 'r')
        zz = f.readlines()
        with open(filename) as f:
            for line_no, line in enumerate(f):
                # Remember not to count the newline character
                if line_no %2 ==0:
                    continue
                    # FOOTBALL().trainingHours(self.N, self.P, 'kick.txt')
                    # print(line_no, line)
                self.N = line.strip()[0]
                self.P = line.strip()[1:]
                FOOTBALL().checkNeP(self.N, self.P)
                FOOTBALL().trainingHours(self.N, self.P, 'kick.txt')
                # print(self.N + ' ==> ' + self.P)
                    # return True


                    # return N, P

        list_of_photoes = []
        # print(zz)
        # for each_line in range(zz):
        #     line = f.readline().split()
        #     print(line)
        #     if len(str(each_line)) == 2:
        #         return True
        self.test_number += 1
        print (self.N, self.P)
       
        
    def checkNeP(self, N, P):
        if N == P:
            return FOOTBALL().genarateOutput(self.test_number, 0)
        return None

    def genarateOutput(self, test_number, training_hour):
        yy = 'case #' + str(self.test_number) + ':' + ' '+ str(training_hour)
        return yy

print(FOOTBALL().footballChallenge('kick.txt', [1, 3]))