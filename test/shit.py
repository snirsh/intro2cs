class ExamQuestion:
    def __init__(self,id,difficulty=0,duration=0):
        self.difficulty=difficulty
        self.duration=duration
        self.id=id
    def __repr__(self):
        return "q"+str(self.id)

def my_key1(exam_question):
    return exam_question.difficulty

def merge(L1,L2,key):
    i,j=0,0
    res=[]
    while i<len(L1) or j<len(L2):
        if(key(L1)<=key(L2)):
            res.append(L1[i])
            i+=1
        else:
            res.append(L2[j])
            j+=1
    return res



q1=ExamQuestion(1,3,1)
q2=ExamQuestion(2,2,4)
q3=ExamQuestion(3,1,2)
q4=ExamQuestion(4,4,1)
q5=ExamQuestion(5,5,4)
q6=ExamQuestion(6,6,2)
q7=ExamQuestion(7,7,1)
q8=ExamQuestion(8,8,4)
q9=ExamQuestion(9,9,2)
exam_questions=[q1,q2,q3]
exam_questions2=[q4,q5,q6]
exam_questions3=[q7,q8,q9]
exam_questions=sorted(exam_questions,key=lambda n:n.difficulty)
exam_questions2=sorted(exam_questions2,key=lambda n:n.difficulty)
questingiaosdn=[exam_questions,exam_questions2,exam_questions3]
print(mergeing(questingiaosdn))

