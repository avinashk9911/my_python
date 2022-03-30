# given a string which contains only two letters 'B' (boy) and 'G'(girl).
# now task is to arrage latters in alternative manner
# i.e. agter every G there should be one and only one B.
# ex= string='BBBGGGBGGGB' out='GBGBGBGBGBG  (in input string there are 6 'G' and 5 'b')


def boygirl(string):
    boy=0
    girl=0
    for i in string:
        if i=='B':
            boy+=1
        else:
            girl+=1
    seats=""
    for i in range(boy):
        seats+="B"
        seats+="G"
        boy-=1
        girl-=1
    print(seats)

string='BBGGBGBGBBBBGGGG'
boygirl(string)