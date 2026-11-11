class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
            
        def build(nums):
            if not nums: return None
            mid = len(nums) // 2
            return TreeNode(nums[mid], build(nums[:mid]), build(nums[mid+1:]))
            
        return build(vals)