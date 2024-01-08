class Sorting:

    def __init__(self, arr: list) -> None:
        self.arr = arr
    
    def bubble_sort(self) -> list:
        arr_len = len(self.arr)
        for i in range(arr_len-1, 0, -1):
            for j in range(i):
                if self.arr[j] > self.arr[j+1]:
                    temp = self.arr[j+1]
                    self.arr[j+1] = self.arr[j]
                    self.arr[j] = temp

        return self.arr
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        j = -1
        lastSeen = {}

        for i, c in enumerate(s):
            j = max(j, lastSeen.get(c, -1))
            ans = max(ans, i - j)
            lastSeen[c] = i

        return ans



if __name__ == "__main__":
    lst = [4,2,6,5,1,3]
    sort = Sorting(lst)
    # print(sort.bubble_sort())
    print(sort.lengthOfLongestSubstring("abcabcbb"))
