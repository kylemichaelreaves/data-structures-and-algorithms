class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end
# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}

class Solution
  def kth_largest_level_sum(root, k)
    level_sums = []
    bfs_queue = []
    bfs_queue << root

    until bfs_queue.empty?
      size = bfs_queue.size
      level_sum = 0

      size.times do
        node = bfs_queue.shift
        level_sum += node.val
        bfs_queue << node.left if node.left
        bfs_queue << node.right if node.right
      end

      level_sums << level_sum
    end

    return -1 if level_sums.size < k

    sorted_sums = level_sums.sort.reverse

    sorted_sums[k - 1]
  end
end
# frozen_string_literal: true

