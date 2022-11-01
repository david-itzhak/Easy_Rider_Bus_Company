# # The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
subjects_set = set()
subjects_set.update(Belov, Smith, Sarada)

print(len(subjects_set))