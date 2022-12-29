from numgen1 import Generator1
from numgen2 import Generator2
from numgen3 import Generator3

NumOfValues = 10000
Bins = 20
NumOfTests = 3
ListOfLambda = [1, 0.5, 10]

for lambda_val in ListOfLambda:
    print(f'\t###__Lambda = {lambda_val}__###')
    generator_1 = Generator1(lambda_val, NumOfValues)
    generator_1.analyze(Bins)
    print()

ListOfAlpha = [1, 0.3, 11]
ListOfSigma = [2, 0.8, 15]

for i in range(0, NumOfTests):
    print(f'\t###__Alpha = {ListOfAlpha[i]}; Sigma = {ListOfSigma[i]}__###')
    generator_2 = Generator2(ListOfAlpha[i], ListOfSigma[i], NumOfValues)
    generator_2.analyze(Bins)
    print()

ListOfA = [pow(5, 13), pow(5, 3), pow(5, 2)]
ListOfC = [pow(2, 31), pow(2, 7), pow(2, 5)]


for i in range(0, NumOfTests):
    print(f'\t###__A = {ListOfA[i]}; C = {ListOfC[i]}__###')
    generator_3 = Generator3(NumOfValues, ListOfA[i], ListOfC[i])
    generator_3.analyze(Bins)
    print()
