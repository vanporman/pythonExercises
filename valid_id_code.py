
def is_person_code_valid(idcode):

    #kontrollib, kas on string, kui ei ole, siis muudab stringiks ja lisa listi
    if (idcode is not str):
        strIdCode = str(idcode)
        idArr = list(strIdCode)
    #lisab otse listi
    else:
        idArr = list(idcode)
    print myArr

    #muudab listi elemendid int-ideks
    idArr = [int(i) for i in idArr]
    print idArr

    #arvitab lsiti numbrite summa
    sumOfIdArr = 0
    for i in idArr:
        sumOfIdArr += i
    print sumOfIdArr

digit_sum("12345678912")