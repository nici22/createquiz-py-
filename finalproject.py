one=True
a=[]
q=[] #questions
opt=[] #options
crrctansw=[] #correct answers
variants=["A","B","C","D"]
mytrues=open('answers_of_user.txt', 'a') #answers of student
mytrues.close()
lists=open('siyahi.txt','a')
lists.close()
answers=open('answers.txt','a')
answers.close()
crrct=open("correctanswers.txt",'a') #list of correct answers
crrct.close()
query=open('questions.txt','a')
query.close()
crrct=open("correctanswers.txt","r")
for i in crrct:
    crrctansw=i.split('$%@')
crrct.close()
query=open('questions.txt','r')
for i in query:
    q=i.split('$%@')
query.close()
answers=open('answers.txt','r')
for i in answers:
    opt=i.split('$%@')
answers.close()
usernames=[]
passwords=[]
while one:
    ask=''
    start=input("For registering type 'register', for logging in type 'login': ").lower() #login or register
    lists=open('siyahi.txt','r')
    for i in lists:
        a=i.split()
    lists.close()
    usernames=[]
    passwords=[]
    for i in a:
        if a.index(i)%3==0:
            usernames.append(i)
        elif a.index(i)%3==1:
            passwords.append(i)
    if start=='login':
        namecheck=input("type your username: ")
        duration=True
        while namecheck not in usernames:
            ask=input("Error!!! This username does not exists. If you want to back type 'yes', if you want to correct it type anything: ").lower()
            if ask=='yes':
                break
            else:
                namecheck=input("Correct it. ")
                pass
        if ask!='yes':
            passwordcheck=  input("type your password: ")
            while passwordcheck!=a[a.index(namecheck)+1]:
                ask=input("Password is incorrect!!! If you want to back type 'yes' if you want to correct it type anything: ").lower()
                if ask=='yes':
                    break
                passwordcheck=input("Correct it. ")
        if ask!='yes':
            print("You logged in succesfully.")
        if ask!='yes':
            if a[a.index(namecheck)+2]=="teacher" :
                while True:
                    options=input("Choose one of them: 'create quiz'-1, 'delete quiz'-2, 'view the list of all quizzes'-3, 'view the responses'-4, 'exit'-5. ").lower()
                    if options=='create quiz' or options=='1':
                        query=open('questions.txt','a')
                        answers=open("answers.txt",'a')
                        crrct=open("correctanswers.txt",'a')
                        while True:
                            try:
                                number=int(input("Input the number of questions: "))
                                if number==int(number):
                                    break
                            except:
                                print("Type just number!!! ")
                        for i in range(number):
                            question=input("Insert number "+str(i+1)+" question. : ")
                            query.write(question+'$%@')
                            print("Insert 4 options and insert the correct answer with UPCASES. (one-by-one) : ")
                            for l in range(4):
                                answ=input(variants[l]+") ")
                                answers.write(answ+'$%@')
                            correct=input("Set correct answer (A,B,C,D) : ").upper()
                            while correct not in variants:
                                print("Error!!!")
                                correct=input("Set correct answer (A,B,C,D) : ").upper()
                            crrct.write(correct+"$%@")
                        crrct=open('correctanswers.txt','r')
                        for i in crrct:
                            crrctansw=i.split('$%@')
                        crrct.close()
                        query=open('questions.txt','r')
                        for i in query:
                            q=i.split('$%@')
                        query.close()
                        answers=open('answers.txt','r')
                        for i in answers:
                            opt=i.split('$%@')
                        answers.close
                    elif options=='delete quiz' or options=='2':
                        while True:
                            try:
                                if len(q)==0:
                                    print("First create quiz!!!")
                                    break
                                for i in range(len(q)):
                                    print(str(i+1)+'. '+q[i])
                                nmbr=int(input('Insert the number of quiz that you want to delete: '))
                                if nmbr>len(q):
                                    print(int('acsd'))
                                if nmbr==int(nmbr):
                                    break
                            except:
                                print("Just enter the NUMBER of quiz!!! ")
                        if len(q)!=0:
                            ##########################################
                            q.pop(nmbr-1)
                            stringg=''
                            for i in q:
                                stringg=stringg+i+'$%@'
                            #stringg=stringg[:-3]
                            query=open('questions.txt','w')
                            query.write(stringg)
                            query.close()
                            '''deleted=q[nmbr-1]
                            query=open('questions.txt','r')
                            for o in query:
                                o=o.replace(deleted+'$%@','')
                            query.close()
                            query=open('questions.txt','w')
                            query.write(o)
                            query.close()
                            query=open('questions.txt','r')
                            for i in query:
                                q=i.split('$%@')    
                            query.close()'''
                            ##########################################
                            rmv=0+4*(nmbr-1)
                            for i in range(4):
                                opt.pop(rmv)
                            string=''
                            for i in opt:
                                string=string+i+'$%@'
                            string=string[:-3]
                            answers=open('answers.txt','w')
                            answers.write(string)
                            answers.close()
                            ##########################################
                            crrctansw.pop(nmbr-1)
                            sstring=''
                            for i in crrctansw:
                                sstring=sstring+i+'$%@'
                            sstring=sstring[:-3]
                            crrct=open('correctanswers.txt','w')
                            crrct.write(sstring)
                            crrct.close()
                            '''crrct=open('correctanswers.txt','r')
                            for i in crrct:
                                ii=i.split('$%@')#'a','b',''
                            crrct.close()
                            ii.remove(ii[nmbr-1])#'b',''
                            crrct=open('correctanswers.txt','w')
                            for x in ii:
                                crrct.write(x+'$%@')
                            crrct.close()
                            crrct=open('correctanswers.txt','r')
                            for i in crrct:
                                crrctansw=i.split('$%@')
                            crrct.close()'''
                            ##########################################
                    elif options=='view the list of all quizzes' or options=='3':
                        if len(q)==0:
                            print("There is no quiz. ")
                        for i in range(1,len(q)+1):
                            print(str(i)+'. '+q[i-1])
                    elif options=='view the responses' or options=='4':
                        #try:
                            #zzzqaz=response
                            mytrues=open('answers_of_user.txt', 'r') #answers of student
                            for p in mytrues:
                                response=p.split()
                            yy=0
                            a=0
                            try:
                                while yy<len(response):
                                    print("Username: ",end='')
                                    for i in response[a:a+len(q)]:
                                        print(i,end=' ')
                                        if yy%len(q)==0:
                                            print("\n"+i+"'s answers: ",end='')
                                        if yy%len(q)==len(q)-1:
                                            print()
                                        yy+=1
                                    a+=len(q)
                            except:
                                print("Students have not answered any quizzes yet.")
                            mytrues.close()
                        #except:
                            #print("No response")
                    elif options=='exit' or options=='5':
                        break
                    decide=input("for backing previous page type 'back', for logging out type anything: ")
                    if decide=='back':
                        pass
                    else:
                        print('Logging out... ')
                        break
            else:
                one=True
                points=0
                digit=0
                line=[]
                take=[]
                myanswer=[]
                variants=["A","B","C","D"]
                crrct=open("correctanswers.txt",'a') #list of correct answers
                crrct.close()
                crrct=open("correctanswers.txt",'r')
                for i in crrct: #correct answers
                    crrctansw=i.split('$%@')
                crrct.close()
                mytrues=open('answers_of_user.txt', 'a') #answers of student
                mytrues.close()
                mytrues=open('answers_of_user.txt', 'r')
                for i in  mytrues:
                    myanswer=i.split()
                mytrues.close()
                done=open('done.txt', 'a') #list of student that have done the quiz
                mytrues.close()
                done1=open('done.txt','r')
                for i in done1:
                    take= i.split()
                done1.close()
                lists=open('siyahi.txt','r') # users' list
                for i in lists:
                    a = i.split()
                lists.close()
                usernames = []
                for i in a:
                    if a.index(i) % 3 == 0:
                        usernames.append(i)
                query=open('questions.txt','r')
                for i in query:
                    q=i.split('$%@')
                query.close()
                answers = open('answers.txt', 'r') #variants
                for i in answers:
                    t=i.split('$%@')
                answers.close()
                crrct=open('correctanswers.txt','r')
                for i in crrct:
                    y=i.split('$%@')
                crrct.close()
                print('\nHere You Are!\nIf You Want To Start Type 1 or  Type Anything To Leave\n')
                ans2 = input("write your choise: ")

                if ans2 == "1":
                    ready=input('To start quiz write your username or To leave  write "exit" ')
                    while ready in a:
                        if ready in take:
                            var = -1
                            z = 0
                            ah = ''
                            for i in range(len(q) - 1):
                                print(i+1,end='')
                                print('. '+q[i])
                                for i in range(z, z + 4):
                                    if z >= len(t) or i >= len(t):
                                        print("That is all")
                                        break
                                    else:
                                        var = var + 1
                                        print(variants[var] + ")" + t[i])
                                var = var - 4
                                z = z + 4
                            print(ready +', you have already done your quiz.')
                            print("Yours     Rights")
                            index=myanswer.index(ready)

                            for i in range( len(q)-1):
                                digit=digit+1
                                index=index+1
                                print(i+1,end='')
                                print('. '+myanswer[index]+'      \t '+ crrctansw[digit-1])
                            break
                        else:
                            mytrues = open('answers_of_user.txt', 'a')
                            mytrues.write(ready + ' ')
                            mytrues.close()
                            query = open('questions.txt', 'r')  # open quizes
#
                            '''for d in query:
                                if len(q) == 0:
                                    print("There is no quiz. ")
                                for quiz_num in range(1, len(q)):
                                    print(str(quiz_num) + '. ' + q[quiz_num - 1])
                            while True:
                                try:
                                    if len(q) == 0:
                                        print("No Quiz!")
                                        break
                                    nmbr = int(input('Insert the number of quiz that you want to choose: '))
                                    if nmbr > len(q):
                                        print(int('wrong num'))
                                    if nmbr == int(nmbr):
                                        break
                                except:
                                    print('Just enter the NUMBER of quiz!!!')
                            if len(q)!=0:
                                print(q[nmbr-1])
                                ans_num= 0 + 4*(nmbr-1)
                                answers = open("answers.txt", 'r')
                                var=-1
                                for s in range(ans_num,ans_num+4) :  #errora bax
                                    var=var+1
                                    print(variants[var]+")"+t[s])
                                a=input("Press enter the write answer")
                                mytrues = open('answers_of_user.txt', 'w')
                                mytrues.write(a)
                                mytrues.close()


                            else:
                                print("DIQQET")'''
#
                            var = -1
                            z = 0
                            ah = ''
                            for i in range(len(q) - 1):
                                print(i+1,q[i])
                                for i in range(z, z + 4):
                                    if z >= len(t) or i >= len(t):
                                        print("That is all")
                                        break
                                    else:
                                        var = var + 1
                                        print(variants[var] + ")" + t[i])
                                var = var - 4
                                z = z + 4
                                ah = input("Please enter the write answer: ")
                                mytrues = open('answers_of_user.txt', 'a')
                                mytrues.write(ah + ' ')
                                mytrues.close()
                            done1 = open('done.txt', 'a')
                            done1.write(ready + ' ')
                            done1.close()
                        print('That is all. See you later')
                        break
                    print("End of the quiz")
                else:
                    print("Logging out...")
    elif start=='register':
        name=input("type your username: ")
        while name in usernames:
            print("This usernames is used. Write another one... ")
            name=input("type your username: ")
        password=input("type your password: ")
        repass=input("type your password again: ")
        while password!=repass:
            print("Error!!! ")
            password=input("type your password: ")
            repass=input("type your password again: ")
        posession=input("enter your posession 'teacher' or 'student': ").lower()
        while posession!='teacher' and posession!='student':
            print("Error!!! ")  
            posession=input("enter your posession 'teacher' or 'student': ").lower()
        print("Congratulations... You have registered succesfully.")
        lists=open('siyahi.txt','a')
        lists.write(name+' ')
        lists.write(password+' ')
        lists.write(posession+' ')
        lists.close()
    asking=input("If you want to quit programme type 'exit', else type anything: ").lower()
    if asking=='exit':
        print("Exiting...")
        break
q=q[:-1]
opt=opt[:-1]
crrctansw=crrctansw[:-1]
    
