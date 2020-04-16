#!/usr/bin/python3



class IDIterator:
    
    def __init__(self, id_num):
        self._id = id_num
        #self._id = '123456784'
        self.iter_index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._id == '999999992': #the last valid ID of the limit
            raise StopIteration('no more availble ID\'s')
        tmp = int(self._id)
        tmp += 1
        tmp = str(tmp)
        while len(tmp) < 9:
            tmp = '0{}'.format(tmp)
        while not check_id_valid(tmp):
            tmp = int(tmp)
            tmp += 1
            tmp = str(tmp)
            while len(tmp) < 9:
                tmp = '0{}'.format(tmp)
        self._id = tmp
        return tmp
        
        #if self.iter_index >= 



def id_geteraotr():
    pass


def check_id_valid(id_number):
    '''
    I'm sorry to tell you that you have Bug on your instruction :( 
    because there are lot of ID's which start by 0, and if I get 
    param of type int: the function can't check these ID's !!!
    this is the reason why I implemented this function diffrent :)
    '''
    if not isinstance(id_number,str):
        raise TypeError('I can\'t see any characters here :(')
    if len(id_number) < 9:
        raise ValueError('Length Error (try to add zero (0) if you need:)')
    if len(id_number) > 9 and set(str(id_number)[:-9]) != {'0'}:
        raise ValueError('not valid ID number')
    sum_num = 0
    for i in range(0,9):
        current = int(id_number[i])
        if i % 2 == 0:
            sum_num += current 
        else:
            current *= 2
            if current > 9:
                current = current % 10 + current//10
            sum_num += current
    return sum_num % 10 == 0
        
 
        
        
def main():
    check = IDIterator('123456780')
    i = 0
    while i < 10:
        print(next(check))
        i += 1
        
if __name__ == '__main__':
    main()