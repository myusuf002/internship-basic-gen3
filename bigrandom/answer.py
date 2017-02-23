class BigRandom:
    def __init__(self):
        self.data = "data.txt"
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag
        j = 0
        # your algorithm
        data = open("data.txt", "r")
        for i in range(10000):
            line = data.readline()
            j = 0
            while line[j] != "#":
                j +=1
            j +=1
            while j != len(line):
                suc = suc + int(ord(line[j]))
                if line[j] == "#":
                    noh +=1
                j +=1

        print (noh)
        print(suc)
        return (noh,suc)

    # add methods if you need more
   
ans = BigRandom()
ans.answer()
