
import time

def matchingSentence(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score =0

    for word in words1:
        for word2 in words2:
            if word.lower() == word2.lower():
                score +=1
    return score

if __name__ == '__main__':
    t1 = time.time()

    # matchingSentence
    listt= ["python for absolute bigners","python tutes","java", "python intermediate", "java course", "flask", "python flask "]
    search = input("search here : ")
    result = [matchingSentence(search,sentence) for sentence in listt]
    # print(result) 

    sortedSentScore =  [sentScore for sentScore in sorted(zip(result,listt), reverse=True) if sentScore[0] !=0]
    print(f"\nOut of( {len(sortedSentScore)} searches) Result found!")
    t2 =time.time()
    finalTime = t2 - t1
    print(f" Result found in {finalTime} miliseconds")
    # print(" Result Found!")
    
    for score, item in sortedSentScore:
        if score>0:
            print(f" \"{item}\": maches with {score}")
        