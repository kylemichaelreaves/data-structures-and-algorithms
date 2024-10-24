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

def kth_largest_level_sum(root, k)
  level_sums = []
  bfs_queue = []
  bfs_queue << root

  until bfs_queue.empty?
    size = bfs_queue.size
    sum_val = 0

    size.times do
      node = bfs_queue.shift
      sum_val += node.val
      bfs_queue << node.left if node.left
      bfs_queue << node.right if node.right
    end

    level_sums << sum_val
  end

  return -1 if level_sums.size < k

  level_sums.sort.reverse[k - 1]
end# frozen_string_literal: true

