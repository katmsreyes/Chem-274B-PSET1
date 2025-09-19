
class Solution:
    def valid_symbols(self, s: str) -> bool:
        # TODO: Implement
        checking_pair = []
        opening_chars = ["(","[","{"]
        closing_chars = ([")","]","}"])
        pair = dict(zip(")]}", "([{"))


        for i in s:
            if i in opening_chars:
                checking_pair.append(i)
            elif i in closing_chars:
                if not checking_pair or s.pop() != pair[s]:
                    return False
                
        return len(checking_pair) == 0
    

    #solution references the Week3_async.pdf slide on Stack: iterative solution
