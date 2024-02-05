from itertools import permutations
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

for case in permutations(user_id, len(banned_id)):
    print(set(case))