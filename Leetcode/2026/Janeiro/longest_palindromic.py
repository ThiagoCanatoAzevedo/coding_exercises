def longestPalindrome(s):
    if not s:
        return ""

    maior = ""

    for left in range(len(s)):
        for right in range(left, len(s)):
            str_atual = s[left:right+1]

            if str_atual == str_atual[::-1]:
                if len(str_atual) > len(maior):
                    maior = str_atual

    return maior
print(longestPalindrome("alv"))