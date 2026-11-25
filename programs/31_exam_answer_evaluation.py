answer_key = "ABCD"
student_answers = [("S01", "ABXD"), ("S02", "ABCC"), ("S03", "XXXX")]

for student_id, answers in student_answers:
    correct = 0
    incorrect = 0
    unanswered = 0
    for position in range(len(answer_key)):
        if answers[position] == "X":
            unanswered = unanswered + 1
        elif answers[position] == answer_key[position]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    score = correct * 4 - incorrect
    print(student_id, "correct:", correct, "incorrect:", incorrect, "unanswered:", unanswered, "score:", score)
