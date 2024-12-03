# positive meaning right, negative meaning left

class Solution:
    def asteroidCollision(self, asteroids):
        
        stack = []

        for i in asteroids:
            while stack and i<0 and stack[-1]>0:
                if stack[-1] < abs(i):
                    stack.pop()
                elif stack[-1] == abs(i):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(i)

        return stack


asteroids = [10,2,-5]
sol = Solution()
ans = sol.asteroidCollision(asteroids)
print(ans)
        