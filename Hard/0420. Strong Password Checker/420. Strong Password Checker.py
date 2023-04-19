class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_type = 3
        if any('a' <= c <= 'z' for c in password):
            missing_type -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_type -= 1
        if any(c.isdigit() for c in password):
            missing_type -= 1

        change = 0
        mod_one = mod_two = 0
        p = 2
        while p < len(password):
            if password[p] == password[p-1] == password[p-2]:
                length = 2
                while p < len(password) and password[p] == password[p-1]:
                    length += 1
                    p += 1

                change += length // 3
                if length % 3 == 0:
                    mod_one += 1
                elif length % 3 == 1:
                    mod_two += 1
            else:
                p += 1

        if len(password) < 6:
            return max(missing_type, 6 - len(password))
        elif len(password) <= 20:
            return max(missing_type, change)
        else:
            delete = len(password) - 20

            change -= min(delete, mod_one)
            delete -= min(delete, mod_one)
            change -= min(delete, mod_two * 2) // 2
            delete -= min(delete, mod_two * 2)
            change = max(0, change - delete // 3)

            return len(password) - 20 + max(missing_type, change)