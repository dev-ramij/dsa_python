class Solution:

    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.

    def removeDuplicate(self, wind, hashMap):
        pass

    def smallestWindow(self, s, p):
        ns = len(s)
        np = len(p)
        if np > ns:
            return -1
        l = 0
        r = 0
        minl = l
        minR = r
        hashMap = {}
        initHashMap = {}
        count = 0
        hasFirst = False
        wind = ""
        minLength = 9999999999999
        for i in range(np):
            if p[i] not in initHashMap:
                initHashMap[p[i]] = 1
            else:
                initHashMap[p[i]] += 1
            hashMap[p[i]] = 0
        while l < ns and r < ns:

            if count == np:
                if r - l < minLength:
                    minl = l
                    minR = r
                    minLength = r - l
                if s[l] in p:
                    hashMap[s[l]] -= 1
                    if hashMap[s[l]] == initHashMap[s[l]]-1:
                        count -= initHashMap[s[l]]
                l += 1
            else:
                if s[r] in p:
                    if hashMap[s[r]] == initHashMap[s[r]]:
                        count += initHashMap[s[r]]
                    hashMap[s[r]] += 1
                r += 1
            print(l, r, count,hashMap)
        while count == np:
            print("enter")
            if r - l < minLength:
                minl = l
                minR = r
                minLength = r - l
            if s[l] in p:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == initHashMap[s[l]]:
                    count -= 1
            l += 1

        return s[minl:minR]


ob = Solution()
# print(
#     ob.smallestWindow(
#         "bdheedcfeeafhijabdbehhfaigjghiijabcfagjgcedbjhhehajgbgbiechagdfeaffejdhhihdhjjahbcgcgdfbfdadhdgefghchdhdigbjciehiebgahbahddhiidebcfaieefjgefaafhbfiabgdbjcfbaedgfhigbgibegjfjjgicjcgciccfdhehcgjdeccbfehdgcddighgagfbeheaccahgfggdbgeaiajeahegbcjadehajafjfcdbbjfgahhcjbaigfbfiifdegiafeejibcfbdecfeicbjgabhbhfdgebfjjjjbggfgcibhehchhffhcebcbdbcedbadjehffjihhdichhebajjgbehjacbbidagihdijjecfcjeibfadbdaehcfjfbjhgbdgbhdjggiajfgjfdifafgebdbjghbehceaiedabebhgigagehcfegjeaiehbfgedaddegiaahgacigafihahegefjgjhhijjfgbddhiafhbjiicjaaigeeeiiadj",
#         "cdaehaihiejehfcfajjcidcdhghfjejbgibadbbgbjegfhgggfgaefaaabcbgdiffdejdijebfebejhaccffehff"
#     ))


print(ob.smallestWindow("timetopractice","toc"))