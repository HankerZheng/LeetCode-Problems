# A password is considered strong if below conditions are all met:

# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
# Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

# Insertion, deletion or replace of any one character are all considered as one change.

class Solution(object):
    def strongPasswordChecker(self, s):
        """
        There are mainly three kinds of problem:
            1. length problem:  6 <= len(s) <= 20
                                if too long, can be solved by delete
                                if too short, can be solved by insert
            2. repeat problem:  '...aaaaaa...' is illegal
                                can be solved by delete, insert and replace
            3. other problem:   uppercase, lowercase, digit
                                can be solved by insert and replace
        """
        # init the problem
        start, end = 0, 0
        length_change = 0
        if len(s) < 6:
            length_change = 6 - len(s)
        if len(s) > 20:
            length_change = len(s) - 20
        lower_flag = 1
        upper_flag = 1
        digit_flag = 1
        repeats = []
        # find the repeating parts
        while end < len(s):
            while end < len(s) and s[start] == s[end]:
                if s[end].isdigit(): digit_flag = 0
                elif s[end].isupper(): upper_flag = 0
                elif s[end].islower(): lower_flag = 0
                end += 1
            if end - start >= 3:
                repeats.append(end-start)
            start = end
        repeats.sort()

        # number of `other problem`
        other_change = lower_flag + upper_flag + digit_flag

        # first handle problem could be solved by DELETE
        length_repeat = 0
        if len(s) > 20:
            # an delete operation could solve both `lenght problem` and `repeat problem`
            while repeats and length_change:
                # it is the same to delete whether in the middle or in the begining
                # once apply an delete, the length of one repeating part decreased by one
                length_repeat += 1  # make one delete, count increment by 1
                repeats[0] -= 1     # repeats part decrement by 1
                length_change -= 1  # solve one `length problem`
                if repeats[0] < 3:
                    repeats.pop(0)  # if length of repeating part is less than 3, this part is totally solved
        if len(s) < 6:
            # an insert operation could slove both `length problem` and `repeat problem`
            while repeats and length_change:
                # we insert a new string into the repeating part every 2 character
                # e.g. for "aaaaa", we make it "aabaaa" for the first insertion, then "aabaaba"
                # Meanwhile, every insertion could solve one `other problem`
                length_repeat += 1    # make one insert, count increment by 1
                repeats[0] -= 2       # repeats part decrement by 2
                length_change -= 1    # solve one `length problem`
                if other_change > 0:  # solve one `other problem`
                    other_change -= 1
                if repeats[0] < 3:    # if length of repeating part is less than 3, this part is totally solved
                    repeats.pop(0)
        # till now, we are sure that we have solved at least one of `repeat problem` or `length problem`
        # if there is still `repeat problem` left, count it and solve it with replace operation
        repeat_left = 0
        for repeat in repeats:
            repeat_left += repeat / 3

        # what left is length_repeat(fixed), other_change(replace/ins), length_change(ins/del) or repeat_left(replace)
        if len(s) > 20:
            # length_change could only be solved by deletion
            if length_change:
                return length_repeat + other_change + length_change
            else:
                return length_repeat + max(other_change, repeat_left)
        else:
            # length_change could be solved by ins
            if length_change:
                return length_repeat + max(other_change, length_change)
            else:
                return length_repeat + max(other_change, repeat_left)

if __name__ == '__main__':
    sol = Solution()
    print sol.strongPasswordChecker("ABABABABABABABABABAB1") == 2
    print sol.strongPasswordChecker("") == 6
    print sol.strongPasswordChecker("01010101aaaABABABABA01") == 2
    print sol.strongPasswordChecker("aaaaaa") == 2
    print sol.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa") == 7