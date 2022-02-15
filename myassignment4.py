import random

win1 = 0
win2 = 0
draw = 0
xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
'''first question'''
print('First question')
for i in range(0,100):
    for i in xarti:
     for j in color:
        xartia.append([i,j])
    random.shuffle(xartia)
    player1 = []
    sum1 = 0
    while sum1 < 16:
        sum1 = 0
        player1.append(xartia.pop())

        for card in player1:
            if card[0] in figures:
                sum1 = sum1 + 10
            else:
                sum1 = sum1 + card[0]

    if sum1 > 21:

        win2 = win2 + 1
    else:



        player2 = []
        sum2 = 0
        while sum2 < 16:
            sum2 = 0
            player2.append(xartia.pop())

            for card in player2:
                if card[0] in figures:
                    sum2 = sum2 + 10
                else:
                    sum2 = sum2 + card[0]

        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:

            win1 = win1 + 1
        elif sum2 > sum1:

            win2 = win2 + 1
        else:
            draw = draw + 1
print('the first player won:', win1, 'times.\n', 'the second player won:', win2, 'times.\n', 'there was a draw', draw, 'times.')


'''next question'''
print('Next question')
win1 = 0
win2 = 0
draw = 0
sum1=0
for i in range(0,100):
 for i in xarti:
        for j in color:
          xartia.append([i, j])
 random.shuffle(xartia)
 player1=[]
 sum1 = 0
 round1 = 1
 round2 = 1
 while sum1<16:
     sum1=0
     if round1 == 1:
         temp = 0
         temp3 = 0

         i = 0

         while i <= 51 and temp == 0:
             temp2 = 0
             j = 0
             while temp2 == 0 and j <= 2:
                 an = type(xartia[i][0])
                 if an == 'int':
                     new = str(xartia[i][0])
                 else:
                     new = xartia[i][0]
                 if new == figures[j]:

                     player1.append(xartia[i])

                     temp2 = 1
                 else:
                     j = j + 1
             if temp2 == 0:
               temp3 = 0
               j = 0
               while temp3 == 0 and j<= 39:
                 if xartia[i][0] == 10:

                     player1.append(xartia[i])


                     temp3 = 1
                 else:
                     j = j + 1
             if temp2 == 1 or temp3 == 1:
                 temp = 1
                 round1 = 0
             else:
                 i = i + 1

     if round1 == 0:
      player1.append(xartia.pop())

      for card in player1:
          if card[0] in figures:
            sum1=sum1+10
          else:
             sum1=sum1+card[0]

 if sum1>21:
     win2 = win2 + 1

 else:



     player2=[]
     sum2=0
     while sum2<16:
         sum2 = 0

         if round2 == 1:
             temp = 0
             temp3= 0
             i = 0

             while i <= 51 and temp == 0:
                 temp2 = 0
                 j = 0
                 an2 = 0
                 while temp2 == 0 and j <= 2:
                     an = type(xartia[i][0])
                     if an == 'int':
                         new = str(xartia[i][0])
                     else:
                         new = xartia[i][0]
                     if new != figures[j]:

                       temp2 = 1
                     else:
                         j = j + 1
                 if temp2 == 1:
                     temp3 = 0
                     if xartia[i][0] != 10:

                             player2.append(xartia[i])

                             temp3 = 1
                     else:
                             j = j + 1
                 if temp2 == 1 or temp3 == 1:
                     temp = 1
                     round2 = 0
                 else:
                     i = i + 1

         else :
          sum2=0
          player2.append(xartia.pop())
          # print (player2)
          for card in player2:
             if card[0] in figures:
                 sum2=sum2+10
             else:
                 sum2=sum2+card[0]

     if sum2>21:
         sum2=0
     if sum1>sum2:

         win1 = win1 + 1
     elif sum2>sum1:

         win2 = win2 + 1
     else:

         draw = draw + 1
print('the first player won:', win1, 'times.\n', 'the second player won:', win2, 'times.\n', 'there was a draw', draw, 'times.')