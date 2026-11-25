# Case 31: String-Based Examination Answer Evaluation

**Data note:** Sample values are illustrative; they are not real-time or official records.

## Problem statement
Compare answer strings against an answer key, count correct, incorrect, and unanswered responses, apply negative marking, and produce student-wise results.

## Objectives
Compare each answer string with the key and calculate scores using explicitly stated illustrative marks.

## Assumptions
- Each character position represents one question; X means unanswered.
- Illustrative scoring is +4 correct, -1 incorrect, 0 unanswered; these are not supplied institutional rules.
- Each answer string has the same length as the key.

## Algorithm
1. Set answer key and student responses.
2. Compare each character position.
3. Count correct, incorrect, unanswered.
4. Calculate score from the example marks and print.

## Flowchart

```text
Start → Set key and responses → Compare position → X? unanswered → Matches key? correct → Otherwise incorrect → Calculate score → Print → End
```

## Pseudocode

```text
FOR each answer string
    set counters to zero
    FOR each question position
        IF X: unanswered += 1
        ELSE IF equal key: correct += 1
        ELSE: incorrect += 1
    score = 4*correct - incorrect
    PRINT counts and score
```

## Python source code

```python
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
```

## Test cases and observed output

The following is stdout from executing the program with its embedded sample data. The PNG capture is in `../output_screenshots/31_exam_answer_evaluation.png`.

```text
S01 correct: 3 incorrect: 0 unanswered: 1 score: 12
S02 correct: 3 incorrect: 1 unanswered: 0 score: 11
S03 correct: 0 incorrect: 0 unanswered: 4 score: 0
```

## Conclusion
The program gives counts and scores under the example marking rule. A real examination must use the teacher-supplied key and policy.
