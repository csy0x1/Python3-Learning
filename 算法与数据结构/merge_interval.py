'''
合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。

提示：
intervals[i][0] <= intervals[i][1]
'''
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0]) #先按第一维升序进行排序
        merged=[] #存储最终列表
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]: #列表为空或与上一区间不重合，直接添加
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1]) #merged[-1][1]:上一区间的右端点，interval[1]:当前区间右端点
        return merged
        
