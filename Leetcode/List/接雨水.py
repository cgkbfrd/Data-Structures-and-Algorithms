class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """方法一【递归】"""
        """
        递归是通过先找最大值，再找第二大的值，根据第二大的值计算两者之间所夹的面积，再减去两者之间已有的数值，就得到能注入的雨水的值。
        然后去除两者之间的数据，并保留第二大的值作为新的数组的最大值，以此进行迭代，直到数组元素剩余两个或者少于两个时结束迭代。
        """
        def recursion(height):
            if len(height) < 3:
                return 0
            tmp = [i for i in height]
            Max1 = max(height)
            while Max1 in tmp:
                tmp.remove(Max1)
            Max2 = max(tmp)
            p1 = [i for i, v in enumerate(height) if v == Max1]
            p2 = [i for i, v in enumerate(height) if v == Max2]
            if len(p1) > 1:
                area = (((max(p1) - min(p1)) - 1) * height[max(p1)] - sum(height[min(p1)+1:max(p1)]))
                height = height[0:min(p1)] + height[max(p1):]
                return  area + recursion(height)
            elif len(p1) == 1:
                if len(p2) > 1:
                    if min(p2) < p1[0] and max(p2) > p1[0]:
                        area = (height[max(p2)]*(max(p2) - p1[0] - 1))-sum(height[p1[0]+1:max(p2)]) +(height[min(p2)]*(p1[0]-min(p2) - 1))-sum(height[min(p2)+1:p1[0]])
                        height = height[0:min(p2)] + height[max(p2):]
                        return  area + recursion(height)
                    if min(p2) > p1[0]:
                        area = (height[max(p2)] * (max(p2) - p1[0] - 1))-sum(height[p1[0]+1: max(p2)])
                        height = height[0:p1[0]] + height[max(p2):]
                        return  area + recursion(height)
                    if max(p2) < p1[0]:
                        area = (height[min(p2)] * (p1[0] - min(p2) - 1))-sum(height[min(p2)+1:p1[0]])
                        height = height[0:min(p2)+1] + height[p1[0]+1:]
                        return  area + recursion(height)
                elif len(p2) == 1:
                    if p2[0] > p1[0]:
                        area = (height[p2[0]] * (p2[0] - p1[0] - 1)) - sum(height[p1[0]+1:p2[0]]) 
                        height = height[0:p1[0]] + height[p2[0]:]
                        return area + recursion(height)
                    else:
                        area = (height[p2[0]] * (p1[0] - p2[0] - 1)) - sum(height[p2[0]+1:p1[0]])
                        height = height[0:p2[0]+1] + height[p1[0]+1:]
                        return area + recursion(height)
                    
        return recursion(height)
      
      """【值得借鉴的方法二】"""
      """
      该方法通过先把最大值找出来，然后从左右两边分别进行遍历，每次都去最大的值，依次往前进行，如果前面的数值比这个小，则它们俩的差值就是要盛的雨水量，
      如果前面的数大，则更换最大值，直到到达最高点结束
      """
      
      def trap(self, height: List[int]) -> int:
          if len(height) == 0:
              return 0
    
          m =height.index(max(height))         
          res, l, r = 0, 0, 0
          for h in height[:m]:
              l = max(l, h)
              res = res + l - h
            
          for h in height[m + 1:][::-1]:
              r = max(r, h)
              res = res + r -h
        
          return res
            
